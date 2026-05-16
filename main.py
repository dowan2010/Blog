from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
from routers import posts, comments, auth
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
	yield


app = FastAPI(lifespan=lifespan)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(auth.router)