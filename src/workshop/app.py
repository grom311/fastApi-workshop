from datetime import datetime
from fastapi import FastAPI
# import uvicorn
# from settings import settings
from api import router

import time

app = FastAPI()
app.include_router(router)

# @app.get('/root')
# def get_root():
#     return 'First Root'

# @app.get('/')
# def root():
#     json_text = {
#         'start': time.localtime(),
#         'end': 123
#     }
#     return json_text

# @app.get('/root/{number}')
# def root_int(number: int):
#     json_text = {
#         'start': number,
#         'end': datetime.now()
#     }
#     return json_text

# @app.get('/root/{string}')
# def root_str(string: str):
#     json_text = {
#         'start': string,
#         'end': datetime.now()
#     }
#     return json_text

# uvicorn.run(app)