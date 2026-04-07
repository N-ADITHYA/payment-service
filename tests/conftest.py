import pytest
from database import fakeDb
from services import handlers

@pytest.fixture(autouse=True)
def resetDb():
    fakeDb.db.clear()
    handlers.order_id = 0
    yield
