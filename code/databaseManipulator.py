import socket
import sys
sys.path.append('./externalLib')
import psycopg2

#Author Owen Renette 101223576
#Version March 18, 2024

#Credit to (https://psycopg.org/) for postgres connection service

def setup(db_user: str, db_pass:str):
    """
    Initializes the connection to the database.
        Parameters:
            db_user (str): The username to the postgres server
            db_pass (str):The password to the postgres server
        Returns:
            cursor: an object connected to the database
    """    
    db_name = "Assignment3"
    db_host = "localhost"
    db_port = 5432
    conn = psycopg2.connect(database= db_name,
                           host = db_host,
                           user = db_user,
                           password = db_pass,
                           port = db_port)
    #Return the item to control database actions
    return conn.cursor()

def commands():
    """
    Prints out valid commands
    """       
    print("Supported commands:\n\t- setup(db_user, db_pass) #CUsed to connect to desired database\n\t- commands() #Displays the valid commands\n\t- getAllStudents()\n\t- addStudent(first_name : str, last_name : str, email : str, enrollment_date : str)\n\t- updateStudentEmail(student_id : int, new_email : str)\n\t- deleteStudent(student_id : int)")

def getAllStudents():
    """
    Prints all the student information
        Returns: list of all the student tuples
    """    
    cursor.execute("SELECT * FROM students;")
    new_table= cursor.fetchall()
    for row in new_table:
        print(row)
    return new_table
    
def addStudent(first_name : str, last_name : str, email : str, enrollment_date : str):
    """
    Adds the desired student and prints out a confirmation message
        Parameters:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            email (str): The email of the student
            enrollment_date (str): The date of enrollment in format YYYY-MM-DD
    """      
    values = "('{}', '{}', '{}', '{}')".format(first_name, last_name, email, enrollment_date)
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES " + values + ";")
    print("Insertion success!")
    
def updateStudentEmail(student_id : int, new_email : str):
    """
    Updates the desired student based off id and prints out a confirmation message
        Parameters:
            student_id (int): The students id in which to update
            new_email (str): The new email of the student
    """       
    cursor.execute("UPDATE students\nSET email = '{}'\nWHERE student_id = {};".format(new_email, str(student_id)))
    print("Update success!")
    
def deleteStudent(student_id : int):
    """
    Deletes the desired student based off id and prints out a confirmation message
        Parameters:
            student_id (int): The students id in which to update
    """      
    cursor.execute("DELETE FROM students\nWHERE student_id = {};".format(str(student_id)))
    print("Delete success!")


#print program info and commands
print("#########################################################################")
print("Welcome to the Python database manipulator!")
print("CREDIT TO ONLINE PACKAGE 'psycopg2' (https://psycopg.org/) WHICH ALLOWS THE DATABASE CONNECTION")
print("!!!THIS PROGRAM ASSUMES THAT THE PORT, HOSTNAME, AND DATABASE_NAME WERE NOT ALTERED!!!\n\t If they were altered, please adjust the setup() function before use...")
print("Supported commands:\n\t- setup(db_user, db_pass) #Prompted off of execution\n\t- commands() #Displays the valid commands\n\t- getAllStudents()\n\t- addStudent(first_name : str, last_name : str, email : str, enrollment_date : str)\n\t- updateStudentEmail(student_id : int, new_email : str)\n\t- deleteStudent(student_id : int)")
print("Enter the DB server's name and passowrd to connect:")

#Prompt for name and pasword of the postgres server that should be connected
name = input("\tEnter the DB server username: ")
password = input("\tEnter the DB server password: ")
cursor = setup(name, password)
print("Connection success! Call the functions above to manipulate the database...\n")
