from fastapi import APIRouter, Request
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import models
from fastapi import Depends
from dependencies import get_current_user
import markdown

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# 포스트 호출
@router.get('/')
async def index(request: Request, current_user=Depends(get_current_user)):
	posts = models.get_all_posts()
	is_admin = current_user.get("is_admin") if current_user else False
	return templates.TemplateResponse("index.html", {"request": request, "posts": posts, "is_admin": is_admin})

@router.get('/posts/search')
async def search_posts(q: str, request: Request, current_user=Depends(get_current_user)):
	posts = models.search_post(q)
	is_admin = current_user.get("is_admin") if current_user else False
	return templates.TemplateResponse("index.html", {"request": request, "posts": posts, "is_admin": is_admin})


@router.get('/posts/new')
async def new_post(request: Request, current_user=Depends(get_current_user)):
	is_admin = current_user.get("is_admin") if current_user else False
	return templates.TemplateResponse("post_form.html", {"request": request, "is_admin": is_admin})


@router.get('/posts/{id}')
async def get_post(id: int, request: Request, current_user=Depends(get_current_user)):
	post = models.get_post(id)
	post["content"] = markdown.markdown(
		post["content"],
		extensions=["fenced_code", "codehilite", "tables"]
	)
	is_admin = current_user.get("is_admin") if current_user else False
	comments = models.get_comments(id)
	return templates.TemplateResponse("post_detail.html",
	                                  {"request": request, "post": post, "comments": comments, "is_admin": is_admin,
	                                   "current_user": current_user})

@router.post('/posts')
async def create_post(title: str = Form(...), content: str = Form(...), current_user=Depends(get_current_user)):
	is_admin = current_user.get("is_admin") if current_user else False
	if not is_admin:
		return RedirectResponse(url='/', status_code=303)
	post = models.create_post(title, content)
	return RedirectResponse(url='/', status_code=303)

@router.get("/posts/{id}/edit")
async def edit_post(id: int, request: Request, current_user=Depends(get_current_user)):
	post = models.get_post(id)
	is_admin = current_user.get("is_admin") if current_user else False
	return templates.TemplateResponse("post_form.html", {"request": request, "post": post, "is_admin": is_admin})

@router.post('/posts/{id}/edit')
async def update_post(id: int, title: str = Form(...), content: str = Form(...),
                      current_user=Depends(get_current_user)):
	is_admin = current_user.get("is_admin") if current_user else False
	if not is_admin:
		return RedirectResponse(url=f'/posts/{id}', status_code=303)
	post = models.update_post(id, title, content)
	return RedirectResponse(url=f'/posts/{id}', status_code=303)

@router.post('/posts/{id}/delete')
async def delete_post(id: int, request: Request, current_user=Depends(get_current_user)):
	is_admin = current_user.get("is_admin") if current_user else False
	if not is_admin:
		return RedirectResponse(url=f'/posts/{id}', status_code=303)
	post = models.delete_post(id)
	return RedirectResponse(url='/', status_code=303)

@router.get('/about')
async def about(request: Request, current_user=Depends(get_current_user)):
	is_admin = current_user.get("is_admin") if current_user else False
	return templates.TemplateResponse("about.html", {"request": request, "is_admin": is_admin})
