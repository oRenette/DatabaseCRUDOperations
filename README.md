# DatabaseCRUDOperations
Provides Create, Read, Update, Delete operations to the Database it connects to.
## Setup
* Launch pgadmin4
* Locate the databaseSetup folder
  * Open the createTable.sql file and execute it
    * If creating through pgadmin4, name the DB 'Assignment3' and remove the 'CREATE DATABASE' querey from the file before executing
  * Open the insertValues.sql file and execute it
    * This will create and inject the 'Assignment3' database to its init state
* Locate the code folder
  * Open the databaseManipulator.py in your prefered IDE
  * Run the script
  * Interact with the IDE shell to use application
    * Instructions shown in the application
* Please note that the program assumes default values for the DB port, name, and hostname
  * These values must be altered in the setup() function if they have been changed by the user
## Credit
* psycopg2 online library - connection the the postgres database server
* Located in .\code\externalLib
* https://psycopg.org/
## Author
* Owen Renette
