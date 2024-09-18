import pymysql

endpoint = 'db-132.c5m2sk8mo5kg.us-west-1.rds.amazonaws.com'
user = 'jonier'
passw = '12345678'

def connectionSQL():
    try:
        pymysql.connect(
            host=endpoint,
            user=user,
            password=passw
        )
        print("Succesfull connection to a database")
    except Exception as err:
        print("Error:", err)

connectionSQL()