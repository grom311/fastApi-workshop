
from .app import app
from .api.auth import router as auth_router
from .api.operations import router as operation_router

from fastapi.testclient import TestClient
import pytest
import sys, asyncio

if sys.platform == "win32" and (3, 8, 0) <= sys.version_info < (3, 9, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here

# client = TestClient(app)

# {
#   "detail": "Could not validate credentials"
# }

# {
#   "email": "string",
#   "username": "string",
#   "id": 0
# }

def test_read_item_bad_token(test_app):
    response = test_app.get(f'{operation_router.prefix}/')
    
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}
