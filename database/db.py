import pymysql

endpoint = 'db-132.c5m2sk8mo5kg.us-west-1.rds.amazonaws.com'
user = 'jonier'
passw = '12345678'

def connectionSQL():
    try:
        obj_connect = pymysql.connect(
            host=endpoint,
            user=user,
            password=passw
        )
        print("Succesfull connection to a database")
        return obj_connect
    except Exception as err:
        print("Error:", err)
        obj_connect = None

def add_user(id, name, lastname, birthday):
    try:
        instruction_sql = "INSERT INTO db_users.users (id, name, lastname, birthday) VALUES("+id+", '"+name+"', '"+lastname+"', '"+birthday+"')"
        obj_connect = connectionSQL()
        cursor = obj_connect.cursor()
        cursor.execute(instruction_sql)
        obj_connect.commit()
        print("The user was added")
        return True
    except Exception as err:
        print("Error:", err)
        return False

def consult_user(id):
    try:
        instruction_sql = "SELECT * FROM db_users.users WHERE id="+id+";"
        obj_connect = connectionSQL()
        cursor = obj_connect.cursor()
        cursor.execute(instruction_sql)
        result_data = cursor.fetchall()
        print("User consulted")
        return result_data
    except Exception as err:
        print("Error:", err)
        return False
        