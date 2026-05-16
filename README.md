# 📝 Dowan's Dev Blog

FastAPI와 MariaDB로 직접 만든 개인 기술 블로그입니다.

---

## 🧑‍💻 만든 계기

개발을 공부하면서 배운 것들을 정리할 공간이 필요했습니다.
Tistory나 Velog 같은 플랫폼도 있지만, **직접 만들어보는 것 자체가 공부**라는 생각에 시작하게 됐습니다.

FastAPI를 처음 배우는 시점이었고, ORM 없이 raw SQL을 직접 작성해보고 싶었습니다. (SQLD 준비 겸)
JWT 인증, 쿠키 처리, 마크다운 렌더링까지 하나씩 붙여나가면서 풀스택 흐름을 직접 익혔습니다.

> **백엔드(Python/FastAPI/SQL)는 직접 작성했으며, 프론트엔드(HTML/CSS)는 Claude AI와 협업하여 제작했습니다.**

---

## 🛠️ 기술 스택

| 분류 | 기술 |
|------|------|
| Backend | Python, FastAPI |
| Database | MariaDB (홈서버), pymysql (raw SQL) |
| Frontend | Jinja2, HTML/CSS (Claude AI 협업) |
| 인증 | JWT (python-jose), bcrypt |
| 배포 | Cloudflare Tunnel |

---

## ✨ 주요 기능

- **글 CRUD** — 작성, 수정, 삭제, 목록 조회
- **마크다운 렌더링** — 코드 블록 문법 하이라이팅 (pygments)
- **JWT 인증** — 쿠키 기반 로그인/로그아웃
- **관리자 권한** — 글 작성/수정/삭제는 관리자만 가능
- **댓글 시스템** — 로그인 사용자 댓글 작성, 본인 댓글 수정/삭제
- **검색** — 제목 및 내용 키워드 검색
- **다크모드** — 라이트/다크 테마 토글

---

## 📁 프로젝트 구조

```
blog/
├── main.py              # FastAPI 앱 진입점
├── database.py          # DB 연결 설정
├── models.py            # SQL 쿼리 함수 모음
├── dependencies.py      # JWT 인증 의존성
├── routers/
│   ├── posts.py         # 글 관련 라우터
│   ├── comments.py      # 댓글 관련 라우터
│   └── auth.py          # 로그인/회원가입 라우터
├── templates/           # Jinja2 HTML 템플릿
└── static/              # CSS 등 정적 파일
```

---

## 🚀 로컬 실행 방법

```bash
# 1. 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate

# 2. 패키지 설치
pip install -r requirements.txt

# 3. .env 파일 생성
cp .env.example .env
# .env에 DB 정보 및 SECRET_KEY 입력

# 4. 서버 실행
uvicorn main:app --reload
```

---

## 📌 향후 계획

- [ ] 페이지네이션 (글 목록 페이지 나누기)
- [ ] 이미지 업로드
- [ ] 태그/카테고리 분류
- [ ] 도메인 연결 및 정식 배포
- [ ] 방문자 수 통계

---

## 💡 배운 것들

- FastAPI의 라우터 구조와 의존성 주입(Depends)
- ORM 없이 raw SQL로 CRUD 구현하는 방법
- JWT 토큰을 쿠키에 저장하고 인증하는 흐름
- Jinja2 템플릿으로 서버사이드 렌더링하는 방식
- POST 후 리다이렉트 패턴 (PRG 패턴)
