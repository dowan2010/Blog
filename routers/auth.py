from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import models

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

router = APIRouter()
templates = Jinja2Templates(directory="templates")
pwd_context = CryptContext(schemes=["bcrypt"])

@router.get('/auth/register')
async def register(request: Request):
	return templates.TemplateResponse("register.html", {"request": request})

# 비번 해시 저장
@router.post('/auth/register')
async def register(request: Request, username: str = Form(...), password: str = Form(...)):
	hashed_password = pwd_context.hash(password)
	try:
		models.create_user(username, hashed_password)
	except:
		return templates.TemplateResponse("register.html", {
			"request": request,
			"error": "이미 사용 중인 아이디입니다."
		})
	return RedirectResponse(url="/auth/login", status_code=303)

@router.get('/auth/login')
async def login(request: Request):
	return templates.TemplateResponse("login.html", {"request": request})

@router.post('/auth/login')
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
	user = models.get_user(username)
	admin = models.admin(username)
	expire = datetime.utcnow() + timedelta(hours=5)

	if not user:
		return templates.TemplateResponse("login.html", {
			"request": request,
			"error": "존재하지 않는 아이디입니다."
		})

	else:
		if not pwd_context.verify(password, user["password"]):
			return templates.TemplateResponse("login.html", {"request": request, "error": "비밀번호가 틀렸습니다."})

		is_admin = True if admin else False
		# 토큰 생성
		token = jwt.encode(
			{"sub": username, "exp": expire, "is_admin": is_admin},
			SECRET_KEY,
			algorithm=ALGORITHM
		)

		response = RedirectResponse(url="/", status_code=303)
		response.set_cookie(key="access_token", value=token)
		return response

@router.post('/auth/logout')
async def logout(request: Request):
	response = RedirectResponse(url="/", status_code=303)
	response.delete_cookie(key="access_token")
	return response
