# Alembic Integration

Alembic is the defacto migration management tool for sqlalchemy. It was built by the same developer(s) as sqlalchemy and at is maintained in parallel.

On venv:
```
pip install alembic
alembic init app/webapp/migrations
```

In generated `alembic.ini` file:

```ini
...
file_template = %%(year)d%%(month).2d%%(day).2d%%(hour).2d%%(minute).2d%%(second).2d_%%(slug)s
...
prepend_sys_path = app
...
```

In generated `app/webapp/migrations/env.py`:

```py
...
import webapp.models.chub_factor_model
import webapp.models.color_model
import webapp.models.brew_model
import webapp.models.brewer_model
import webapp.models.recipe_model
from models.base_model import Base
from db_engine import engine, connection_string
...

target_metadata = Base.metadata
...

def run_migrations_offline():
    ...
    url = connection_string
...

def run_migrations_online():
    ...
    connectable = engine
...
```
