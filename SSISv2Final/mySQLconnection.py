import mysql.connector
import configparser

configFilePath = r"C:\Users\Romeo B. Aclo\Desktop\SSISv2Final\mySQLInfo.ini"
config = configparser.ConfigParser()
config.read(configFilePath)

connection = mysql.connector.connect(
    host=config.get('mysql', 'host'),
    user=config.get('mysql', 'user'),
    password=config.get('mysql', 'password'),
    database=config.get('mysql', 'database')
)

cursor = connection.cursor()

def insertTable(values, choice):
    if choice == 0:
        sql = "INSERT INTO student_table(studentID, name, gender, yearLevel, courseCode) VALUES (%s, %s, %s, %s, %s)"
    elif choice == 1:
        sql = "INSERT INTO course_table(courseCode, course) VALUES (%s, %s)"
    else:
        print("no choice selected")
        return

    #print(values)
    cursor.execute(sql, values)
    connection.commit()

def deleteTableRow(values, choice):
    print(values)
    if choice == 0:
        sql = "DELETE FROM student_table WHERE studentID = %s"
    elif choice == 1:
        sql = "DELETE FROM course_table WHERE courseCode = %s"
    else:
        print("no choice selected")
        return
    
    print(values)
    if len(values) != 0 :
        for item in values:
            cursor.execute(sql, (values,))
            connection.commit()

def queryTable(choice):
    print(choice)
    if choice == 0:
        sql = "SELECT * FROM student_table"
    elif choice == 1:
        sql = "SELECT * FROM course_table"
    else:
        print("no choice selected")
        return

    cursor.execute(sql)
    rows = cursor.fetchall()
    #print(rows)
    return rows

def editTable(columnName, list, choice):
    #print(columnName)
    #print(list)
    if choice == 0:
        sql = f"UPDATE student_table SET {columnName} = %s WHERE studentID = %s"
    elif choice == 1:
        sql = f"UPDATE course_table SET {columnName} = %s WHERE courseCode = %s"

    cursor.execute(sql,list)
    connection.commit()

def closeConnection():
    cursor.close()
    connection.close()
