import threading
from sqlalchemy import create_engine

from core.repository.dal.config import DB_SERVER, DB_NAME

_engine = None


def create_dal_engine():
    global _engine
    if not _engine:
        _engine = create_engine(
            '{}/{}?application_name={}'.format(
                DB_SERVER, DB_NAME, threading.current_thread().ident))
    return _engine
