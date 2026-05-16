import database

get_db = database.get_db


def get_all_posts():
	conn = get_db()
	cur = conn.cursor()
	cur.execute("SELECT * FROM post")
	result = cur.fetchall()
	cur.close()
	conn.close()
	return result

def get_post(id):
	conn = get_db()
	cur = conn.cursor()
	cur.execute("SELECT * FROM post WHERE id = %s", (id,))
	result = cur.fetchone()
	cur.close()
	conn.close()
	return result

def create_post(title, content):
	conn = get_db()
	cur = conn.cursor()
	cur.execute("INSERT INTO post (title, content) VALUES (%s, %s)", (title, content))
	conn.commit()
	cur.close()
	conn.close()

def update_post(id, title, content):
	conn = get_db()
	cur = conn.cursor()
	cur.execute("UPDATE post SET title = %s, content = %s, updated_at = NOW() WHERE id = %s", (title, content, id))
	conn.commit()
	cur.close()
	conn.close()

def delete_post(id):
	conn = get_db()
	cur = conn.cursor()
	cur.execute("DELETE FROM post WHERE id = %s", (id,))
	conn.commit()
	cur.close()
	conn.close()

def search_post(q):
	conn = get_db()
	cur = conn.cursor()
	keyword = f"%{q}%"
	cur.execute("SELECT * FROM post WHERE title LIKE %s or content LIKE %s", (keyword, keyword))
	result = cur.fetchall()
	cur.close()
	conn.close()
	return result

def get_comment(id):
	conn = get_db()
	cur = conn.cursor()
	cur.execute("SELECT * FROM comments WHERE id = %s", (id,))
	result = cur.fetchone()
	cur.close()
	conn.close()
	return result

def get_comments(post_id):
	conn = get_db()
	cur = conn.cursor()
	cur.execute("SELECT * FROM comments WHERE post_id = %s", (post_id,))
	result = cur.fetchall()
	cur.close()
	conn.close()
	return result

def create_comments(post_id, username, content):
	conn = get_db()
	cur = conn.cursor()
	cur.execute("INSERT INTO comments (post_id, username, content) VALUES (%s, %s, %s)",(post_id, username, content))
	conn.commit()
	cur.close()
	conn.close()

def update_comment(id, content):
	conn = get_db()
	cur = conn.cursor()
	cur.execute("UPDATE comments SET content = %s WHERE id = %s", (content, id))
	conn.commit()
	cur.close()
	conn.close()

def delete_comment(id):
	conn = get_db()
	cur = conn.cursor()
	cur.execute("DELETE FROM comments WHERE id = %s", (id,))
	conn.commit()
	cur.close()
	conn.close()

def admin(username):
	conn = get_db()
	cur = conn.cursor()
	cur.execute("SELECT * FROM admin WHERE username = %s", (username,))
	result = cur.fetchone()
	cur.close()
	conn.close()
	return result

def create_user(username, password):
	conn = get_db()
	cur = conn.cursor()
	cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
	conn.commit()
	cur.close()
	conn.close()

def get_user(username):
	conn = get_db()
	cur = conn.cursor()
	cur.execute("SELECT * FROM users WHERE username = %s", (username,))
	result = cur.fetchone()
	cur.close()
	conn.close()
	return result

def update_user(id, username, password):
	conn = get_db()
	cur = conn.cursor()
	cur.execute("UPDATE users SET username = %s, password = %s WHERE id = %s", (username, password, id))
	conn.commit()
	cur.close()
	conn.close()