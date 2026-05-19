from fastapi import APIRouter, Request
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import models
from fastapi import Depends
from dependencies import get_current_user

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# 댓글 등록
@router.post("/posts/{id}/comments")
async def create_comment(id: int, content: str = Form(...), current_user=Depends(get_current_user)):
	if not current_user:
		return RedirectResponse(url=f'/posts/{id}', status_code=303)
	username = current_user.get("sub")
	models.create_comments(id, username, content)
	return RedirectResponse(url=f"/posts/{id}", status_code=303)

# 댓글 수정
@router.post('/comments/{id}/edit')
#id 받기
async def edit_comment(id: int, content: str = Form(...), current_user=Depends(get_current_user)):
	if not current_user:
		return RedirectResponse(url=f'/posts/{id}', status_code=303)
	comment = models.get_comment(id)
	username = current_user.get("sub")
	if username != comment["username"]:
		return RedirectResponse(url=f'/posts/{id}', status_code=303)
	models.update_comment(id, content)
	comment = models.get_comment(id)
	return RedirectResponse(url=f'/posts/{comment["post_id"]}', status_code=303)

# 댓글 삭제
@router.post('/comments/{id}/delete')
async def delete_comment(id: int, current_user=Depends(get_current_user)):
	if not current_user:
		return RedirectResponse(url=f'/posts/{id}', status_code=303)
	is_admin = current_user.get("is_admin") if current_user else False
	comment = models.get_comment(id)
	username = current_user.get("sub")
	if username != comment["username"] and not is_admin:
		return RedirectResponse(url=f'/posts/{id}', status_code=303)
	models.delete_comment(id)
	return RedirectResponse(url=f'/posts/{comment["post_id"]}', status_code=303)