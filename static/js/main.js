// ===== 다크모드 =====
function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    document.getElementById('theme-icon').setAttribute('data-lucide', next === 'dark' ? 'sun' : 'moon');
    lucide.createIcons();
}

// 페이지 로드 시 테마 아이콘 초기화
if (document.documentElement.getAttribute('data-theme') === 'dark') {
    document.getElementById('theme-icon').setAttribute('data-lucide', 'sun');
}
lucide.createIcons();


// ===== 댓글 수정 폼 토글 =====
function toggleEditForm(commentId) {
    const form = document.getElementById('edit-form-' + commentId);
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
}
