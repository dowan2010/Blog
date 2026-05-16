# .env 읽는 법
from dotenv import load_dotenv
import os
import pymysql

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PORT = int(os.getenv("DB_PORT"))
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def get_db():
	return pymysql.connect(
		host=DB_HOST,
		port=DB_PORT,
		user=DB_USER,
		password=DB_PASSWORD,
		database=DB_NAME,
		cursorclass=pymysql.cursors.DictCursor
	)
