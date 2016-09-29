import pymysql.cursors
import os

def db_get_students():
# Connect to the database
  connection = pymysql.connect(host='localhost',
                               user='turtle',
                               password='',
                               db='KAI_APP',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

  try:
      with connection.cursor() as cursor:
          # Create a new record
          sql = "SELECT * FROM STUDENTS"
          cursor.execute(sql)
          results = cursor.fetchall()
          return results

  finally:
      connection.close()

def db_get_classes():
# Connect to the database
  connection = pymysql.connect(host='localhost',
                               user='turtle',
                               password='',
                               db='KAI_APP',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

  try:
      with connection.cursor() as cursor:
          # Create a new record
          sql = "SELECT * FROM CLASSES"
          cursor.execute(sql)
          results = cursor.fetchall()
          return results

  finally:
      connection.close()

def db_save_student(student_class_id, student_id, student_first_name, student_last_name, student_grade):
# Connect to the database
  connection = pymysql.connect(host='localhost',
                               user='turtle',
                               password='',
                               db='KAI_APP',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

  try:
      with connection.cursor() as cursor:
          # Create a new record
          sql = "INSERT INTO STUDENTS VALUES (%s, %s, %s, %s, %s)"
          data = student_class_id, student_id, student_first_name, student_last_name, student_grade
          cursor.execute(sql, data)

      # connection is not autocommit by default. So you must commit to save
      # your changes.
      connection.commit()

  finally:
      connection.close()


def db_save_class(class_id, class_name, class_instructor):
# Connect to the database
  connection = pymysql.connect(host='localhost',
                               user='turtle',
                               password='',
                               db='KAI_APP',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

  try:
      with connection.cursor() as cursor:
          # Create a new record
          sql = "INSERT INTO CLASSES VALUES (%s, %s, %s)"
          data = class_id, class_name, class_instructor
          cursor.execute(sql, data)

      # connection is not autocommit by default. So you must commit to save
      # your changes.
      connection.commit()

  finally:
      connection.close()

def db_delete_student(student_id, class_id):
  connection = pymysql.connect(host='localhost',
                               user='turtle',
                               password='',
                               db='KAI_APP',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

  try:
      with connection.cursor() as cursor:
          # Create a new record
          sql = "DELETE FROM STUDENTS WHERE student_id = %s AND class_id = %s"
          data = student_id, class_id
          cursor.execute(sql, data)

      # connection is not autocommit by default. So you must commit to save
      # your changes.
      connection.commit()

  finally:
      connection.close()


def db_delete_class(class_id):
  connection = pymysql.connect(host='localhost',
                               user='turtle',
                               password='',
                               db='KAI_APP',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

  try:
      with connection.cursor() as cursor:
          # Create a new record
          sql = "DELETE FROM CLASSES WHERE class_id = %s"
          data = class_id
          cursor.execute(sql, data)

      # connection is not autocommit by default. So you must commit to save
      # your changes.
      connection.commit()

  finally:
      connection.close()



