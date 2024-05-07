# Solution to db thick client task

## Task 
1. Modify the Employees table
   * Insert two (2) new employees to the Employees table
   * Use 'UPDATE' to update last name of one of the employees
   * commit the changes as a transation
2. Modify the Orders table
   * in loop add 10 new orders using 'INSERT' by using modified copies of existing orders
   * commit the changes as a transaction

## cnf.ini
The missing file ``cnf.ini`` contains the database login information. It has the following contents
```ini
[mssqlDB]
server = 127.0.0.1:port
db = Nothwind
user = username
pass =  userpass
```