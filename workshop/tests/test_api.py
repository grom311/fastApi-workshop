from ..app import app
from ..api.auth import router as auth_router

from fastapi.testclient import TestClient

client = TestClient(app)

# {
#   "detail": "Could not validate credentials"
# }

# {
#   "email": "string",
#   "username": "string",
#   "id": 0
# }

def test_read_item_bad_token():
    response = client.get(f'{auth_router.prefix}/user/')
    assert response.status_code == 401
    assert response.json() == {"detail": "Could not validate credentials"}
