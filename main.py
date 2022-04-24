from fastapi import FastAPI

import list.list_controller

app = FastAPI()

app.include_router(list.list_controller.router)