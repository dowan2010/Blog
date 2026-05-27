import uvicorn
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

if __name__ == "__main__":
    # 스크립트를 직접 실행할 때만 서버 구동
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)