include Makefile.config

PROJECT_ROOT=${PWD}
VENV_PATH=${PROJECT_ROOT}/venv
VENV_ACTIVATE=${VENV_PATH}/bin/activate
APP_ROOT=${PROJECT_ROOT}/app
PYTHON_PATH=${VENV_PATH}/bin/python$(PYTHON_VERSION)
REQ_IN=${PROJECT_ROOT}/requirements.in
REQ_TXT=${PROJECT_ROOT}/requirements.txt

default: run

venv:
	if [ ! -z venv ]; then	\
		python$(PYTHON_VERSION) -m venv venv; \
	fi
	rm requirements.txt; \
	. venv/bin/activate; \
	pip install --upgrade pip; \
	pip install pip-tools; \
	pip-compile --output-file=${REQ_TXT} ${REQ_IN}; \
	pip install -r requirements.txt; \

correct_venv:
	. venv/bin/activate; \
	pip uninstall -y mysql-connector-python; \
	pip install mysql-connector-python;

reset_venv: clean venv correct_venv

clean_py:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

clean: clean_py
	rm -rf venv

run: venv upgrade_database
	. venv/bin/activate; \
	python$(PYTHON_VERSION) app/app.py


# -----------------------------------------------------------------------------------
# DATABASE
install_mysql:
	sudo apt install mariadb-server;

CREATE_DATABASE=create database if not exists ${MYSQL_DATABASE_NAME}
CREATE_USER=use mysql; create or replace user '${MYSQL_DATABASE_NAME}'@'%' identified by '${MYSQL_PASSWORD}'
GRANT_ALL_PRIVLEGES=grant all privileges on ${MYSQL_DATABASE_NAME}.* to '${MYSQL_DATABASE_NAME}'@'%' with grant option
DROP_DATABASE=drop database ${MYSQL_DATABASE_NAME}
RESET_DATABASE=${DROP_DATABASE}; ${CREATE_DATABASE}; ${CREATE_USER}; ${GRANT_ALL_PRIVLEGES}; flush privileges;

setup_mysql:
	sudo mysql -h ${MYSQL_HOST} -u root -e "${CREATE_DATABASE};";\
	sudo mysql -h ${MYSQL_HOST} -u root -e "${CREATE_USER}; ${GRANT_ALL_PRIVLEGES}; flush privileges;";

init_database: install_mysql setup_mysql upgrade_database

reset_database:
	sudo mysql -h ${MYSQL_HOST} -u root -e "${RESET_DATABASE}";\
	alembic upgrade head;

downgrade_database: venv
	. venv/bin/activate; \
	alembic downgrade base;

upgrade_database: venv
	. venv/bin/activate; \
	alembic upgrade head
# -----------------------------------------------------------------------------------

# PIPELINES(?)
# -----------------------------------------------------------------------------------

update_prod:
	ssh -i ~/.ssh/id_rsa-remote-ssh ${PROD_USER}@${PROD_SERVER} "cd workspace/chubfactor; make update;"

update_prod_bash:
	ssh -i ~/.ssh/id_rsa-remote-ssh ${PROD_USER}@${PROD_SERVER} "~/update;"

update:
	cd ~/workspace/chubfactor/
	eval "$$(ssh-agent -s)"
	ssh-add ~/.ssh/id_rsa
	git pull
	make upgrade_database
	~/restart_nginx
	exit

# -----------------------------------------------------------------------------------
