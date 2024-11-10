import mysql.connector
from mysql.connector import Error
import sys
import random
# connect to database


def showTable():
    cursor.execute("SHOW TABLES")
    for count in cursor:
        print(count[0])


try:
    connection = mysql.connector.connect(
    host ='localhost',
    user ='root',
    database ='mineSweeper')

# display error message and quit if not connected
except Error as e:
    print(e)
    sys.exit()
    # stop the program
else:
    cursor = connection.cursor()
    gameStart = False
    login = input("To register type 'R' or to log in to an account type 'L': ")
    while not gameStart:
        login = login.upper()
        if login == "L":
            userName = input("please input your username:")
            while len(userName) == 0 or len(userName) > 8:
                print("A maximum off 8 characters")
                userName = input("please input your username:")
            Password = input("please input your password:")
            while len(Password) == 0 or len(Password) > 8:
                print("A maximum off 8 characters")
                Password = input("please input your password:")
            query = f"SELECT * FROM users WHERE userID = '{userName}' AND userPassword = '{Password}'"
            cursor.execute(query)
            result = cursor.fetchall()
            if cursor.rowcount == 0:
                print("not valid log in dataBase?")
                query = f"SELECT * FROM users WHERE userID = '{userName}'"
                cursor.execute(query)
                result = cursor.fetchall()
                if cursor.rowcount == 0:
                    print("username does not exist")
                elif result[0][0] == userName:
                    print("userName Exists but password is wrong")
            else:
                print("the game starts!")
                gameStart = True

        elif login == "R":
            userName = input("please input your new username:")
            while len(userName) == 0 or len(userName) > 8:
                print("A maximum off 8 characters")
                userName = input("please input your username:")
            Password = input("please input your new password:")
            while len(Password) == 0 or len(Password) > 8:
                print("A maximum off 8 characters")
                Password = input("please input your password:")
            Password2 = input("please confirm your password:")
            while len(Password2) == 0 or len(Password2) > 8:
                print("A maximum off 8 characters")
                Password2 = input("please input your password:")
            query = f"SELECT * FROM users WHERE userID = '{userName}'"
            cursor.execute(query)
            result = cursor.fetchall()
            if cursor.rowcount == 0 and Password2 == Password:
                query = f"INSERT INTO users VALUES ('{userName}', '{Password}');"
                cursor.execute(query)
                connection.commit()
                print("added to database")
                print("the game starts!")
                gameStart = True
            elif Password2 != Password:
                print("passwords dont match")
            else:
                print("username already exists")

        else:
            print("That is not a valid input")
            login = input("To register type 'R' or to log in to an account type 'L': ")

    print("this is the game")
    score = random.randint(5, 100)

    query = "SELECT MAX(gameID) FROM game"
    cursor.execute(query)
    result = cursor.fetchall()
    if cursor.rowcount == 0:
        gameNumber = 1

    else:
        gameNumber = result[0][0]+1
        query = f"INSERT INTO game VALUES ('{gameNumber}');"
        cursor.execute(query)
        query = f"INSERT INTO ranking VALUES ('{gameNumber}', '{userName}', '{score}');"
        cursor.execute(query)
        connection.commit()
