import uvicorn
from settings import settings


if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host=settings.server_hort,
        port=settings.server_port,
        reload=True
    )
