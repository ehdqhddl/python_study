# Section 12 
# 데이터베이스 실습 SQLite
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성

now = datetime.datetime.now()

print(now)
print()

now_datetime = now.strftime('%Y-%m-%d %H:%M:%S')

print('nowDateTime:',now_datetime)
print()

# sqlite3
print('sqlite3.version:',sqlite3.version)
print('sqlite3.sqlite_version:',sqlite3.sqlite_version)
print()

# DB 생성 & Auto Commit
conn = sqlite3.connect('C:/python_basic/resource/database.db',isolation_level=None)

# Cursor
c = conn.cursor()
print(type(c))

# 테이블 생성
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text,\
     email text, phone text, website text, regdate text)")

# 데이터 삽입
# c.execute("INSERT INTO users VALUES(1, 'Park', 'Park@naver.com', '000-1234-5678', 'Park.com', ?)", (now_datetime,))
# c.execute("INSERT INTO users (id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", (2, 'Kim', 'Kim@google.com', '010-9876-5432', 'Kim.com', now_datetime))

# 대용량 데이터 삽입(튜플, 리스트)
user_list = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-3333', 'Lee.com', now_datetime),
    (4, 'Ji', 'Ji@naver.com', '010-9999-3333', 'Ji.com', now_datetime),
    (5, 'Cho', 'Cho@naver.com', '010-8888-3333', 'Cho.com', now_datetime)
)

# c.executemany("INSERT INTO users (id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", user_list)

# 데이터 삭제
# c.execute("DELETE FROM users")
# print("user db deleted :",c.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동 반영 (오토커밋)
# c.commit(), c.rollback()

conn.close()
