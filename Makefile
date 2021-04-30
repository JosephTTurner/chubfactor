PROJECT_ROOT=${PWD}
VENV_PATH=${PROJECT_ROOT}/venv
VENV_ACTIVATE=${VENV_PATH}/bin/activate
APP_ROOT=${PROJECT_ROOT}/app
PYTHON_PATH=${VENV_PATH}/bin/python3
REQ_IN=${PROJECT_ROOT}/requirements.in
REQ_TXT=${PROJECT_ROOT}/requirements.txt

venv:
	if [ ! -z venv ]; then	\
		virtualenv venv; \
	fi
	rm requirements.txt; \
	pip-compile --output-file=${REQ_TXT} ${REQ_IN}; \
	. venv/bin/activate; \
	pip install -r requirements.txt;

web: venv
	. venv/bin/activate; \
	python app/app.py

clean:
	rm -rf venv


