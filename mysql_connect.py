import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='username',
                             port=3306,
                             password='password',
                             db='testdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

if __name__ == '__main__':
	try:
		with connection.cursor() as cursor:
			cursor.execute("SELECT * FROM tablename")
			r = cursor.fetchone()
			print(r)
	finally:
		connection.close()
