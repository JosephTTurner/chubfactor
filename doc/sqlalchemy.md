# SQLAlchemy Integration

Connection string is defined by values in `.env`.

Values are loaded into application memory in `app/config/config.py`.

Values are imported from config into `app/db_engine.py` where the engine and session are defined.
