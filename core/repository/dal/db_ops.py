from core.repository.dal.base import Base
from core.repository.dal import create_dal_engine


def initialize_database():
    print('Start DB initializing')
    _create_scheme()


def _create_scheme():
    Base.metadata.create_all(create_dal_engine())
    print('DB scheme has been created')
