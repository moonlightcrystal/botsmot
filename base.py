import pymysql.cursors  

mySQLServer = "localhost"
myDatabase = "db_kcorie"
myPwd = "1"
myUserId = "kris"


def connect():
    connection = pymysql.connect(host='localhost',
                             user='kris',
                             password='1',                             
                             db='testkri',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection


def create_table():
    try:
        connection = connect()
        with connection.cursor() as cursor:

            sql = """
            CREATE TABLE IF NOT EXISTS users (
            user_id int PRIMARY KEY NOT NULL,
            username varchar(255),
            firstname varchar(255),
            lastname varchar(255),
            about text,
            phone VARCHAR(15) UNIQUE)
            """

            cursor.execute(sql)

    finally:    
        connection.close()

request = """
            INSERT INTO users (user_id, username, firstname, lastname, phone)
			VALUES (%s, %s, %s, %s, %s)
            """
			# ON CONFLICT (user_id) DO NOTHING
			# username	= EXCLUDED.username,
			# firstname	= EXCLUDED.firstname,
			# lastname	= EXCLUDED.lastname,
            # phone       = EXCLUDED.phone


def feel_it(arrayUsers):
    connection = connect()
    with connection.cursor() as cursor:
        for user in arrayUsers:
            user = user.to_dict()
            aboutUser = (user['id'], user['username'], user['first_name'], user['last_name'], user['phone'])
            cursor.execute(request, aboutUser)

    connection.commit()
    connection.close()

# user = [{
#     'id' : 12324,
#     'username' : 'jokey',
#     'first_name' : 'htghofh', 
#     'last_name' : 'gfhfgjh',
#     'phone' : '124235346'
# },
# {
#     'id' : 12325,
#     'username' : 'jokey2',
#     'first_name' : 'htghofh2', 
#     'last_name' : 'gfhfgjh2',
#     'phone' : '1242353462'
# }
# ]

# feel_it(user)

# def insertToDB(dateVal):
# 	connection = pymysql.connect(host='localhost',
# 	                             user='smorty',                             
# 	                             db='db_smorty',
# 	                             charset='utf8mb4',
# 	                             cursorclass=pymysql.cursors.DictCursor)
# 	cursor = connection.cursor()
# 	sql = "INSERT INTO testbot (day, month, year) VALUES (%s, %s, %s)"
# 	val = (dateVal.day, dateVal.month, dateVal.year)
# 	cursor.execute(sql, val)
# 	connection.commit()
# 	connection.close()
# 	print("date inserted (probably)")