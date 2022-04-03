"""main module, run fastapi uvicorn"""
from fastapi import FastAPI
from .api import router


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Authorisation'
    },
    {
        'name': 'operations',
        'description': 'Work with operations'
    },
    {
        'name': 'reports',
    'description': 'get reports csv'
    }
]

app = FastAPI(
    title='Workshop',
    description='Service save or.....',
    openapi_tags=tags_metadata,
)
app.include_router(router)
