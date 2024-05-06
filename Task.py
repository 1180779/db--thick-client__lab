from db_connection import cnx_mssql
from random import randint
from Decimal import *
from Datetime import *
import re

class Task(object):
    def __init__(self):
        self.cursor = cnx_mssql.cursor()
    
    def Print(self):
        """ print the contents of the table """
        querry = "SELECT EmployeeID, LastName, FirstName FROM Employees"
        self.cursor.execute(querry)
        result = self.cursor.fetchall()
        print("TABLE: ")
        if len(result) == 0:
            print("{empty}")
        for row in result:
            print(row)

    def __getidtochange(self) -> int:
        querry = "SELECT EmployeeID FROM Employees"
        self.cursor.execute(querry)
        res = self.cursor.fetchall()
        IDs = []
        max = len(res)
        for entry in res:
            entry = str(entry)
            ID = int(entry[1:-2])
            IDs.append(ID)
        selected = randint(1, max)
        return IDs[selected - 1]

    def Task1(self):
        """ execute task 1 """
        print("log: Executing task 1")
        self.Print()
        self.cursor.execute("INSERT INTO Employees (LastName, FirstName) VALUES ('Kowalski', 'Janusz')")
        self.cursor.execute("INSERT INTO Employees (LastName, FirstName) VALUES ('Mentzen', 'Sławomir')")
        print("log: Inserted two (2) new employees")
        self.Print()

        id = self.__getidtochange()
        self.cursor.execute("UPDATE Employees SET LastName = 'Changed surname' WHERE EmployeeID = " + str(id))
        print("log: updated the lastname of one random employee")
        self.Print()

        print("log: commiting...")
        cnx_mssql.commit()
        print("log: commited!")

    def Print2(self):
            """ print the number of orders """
            self.cursor.execute("SELECT COUNT(*) FROM Orders")
            print("number of orders = " + str(self.cursor.fetchall())[2:-3])

    def Task2(self):
        print("log: Executing task 2")
        self.Print2()
        for i in range(1, 11):
            querry = "INSERT INTO Orders VALUES " + self.__getrandomvalues()
            print("querry  = " + querry)
            self.cursor.execute(querry)

        print("log: Added ten (10) random orders")
        self.Print2()
        cnx_mssql.commit()

    def __concatenate(self, values) -> str:
        res = "("
        for value in values:
            res = res + str(value) + ','
        return res[:-1] + ')'

    def __getrandomvalues(self):
        self.cursor.execute("SELECT * FROM Orders")
        rows = self.cursor.fetchall()

        items = len(self.__separatevalues(rows[0]))
        values = []
        for i in range(1, items):
            randomidx = self.__getrandominx(rows)
            string = self.__separatevalues(rows[self.__getrandominx(rows)])[i]
            while isinstance(string, str) and string == 'None':
                idx = self.__getrandominx(rows)
                string = self.__separatevalues(rows[idx])[i]
            if i in [3, 4, 5]:
                # account for datetime
                val = Datetime(string)
                values.append(val)
            elif i == 7:
                # account for decimal ('money' type field) 
                val = Decimal(string)
                values.append(val)
            else:
                values.append(string)

        return self.__concatenate(values)
            
    def __separatevalues(self, row):
        row = str(row)
        row = row[1:-1]
        row = row.replace(' ', '')
        res =  re.split(r',(?![^(]*\))', row)
        return res

    def __getmaxid(self) -> int:
        self.cursor.execute("SELECT OrderID FROM Orders")
        rows = self.cursor.fetchall()
        maxid = 0
        for row in rows:
            row = str(row)
            id = int(row[1:-2])
            if id > maxid:
                maxid = id
        return maxid
        
    def __getrandominx(self, rows) -> int:
        max = len(rows)
        return randint(1, max) - 1


