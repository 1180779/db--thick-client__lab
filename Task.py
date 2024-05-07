from db_connection import cnx_mssql
from random import randint

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

        self.cursor.execute("SELECT * FROM Orders")
        rows = self.cursor.fetchall()
        for i in range(1, 11):
            order = self.__getrandomvalues(rows)
            print("new order = " + order)
            self.cursor.execute("INSERT INTO Orders VALUES " + order)

        print("log: Added ten (10) random orders")
        self.Print2()
        cnx_mssql.commit()

    def __concatenate(self, values) -> str:
        res = ''
        for value in values:
            temp = value
            if isinstance(value, str):
                temp = value.replace('\'', '\'\'')
            res += '\'' + str(temp) + "\',"
        return '(' + res[:-1] + ')'

    def __getrandomvalues(self, rows):
        items = len(rows[0])
        values = []
        for i in range(1, items):
            val = rows[self.__getrandominx(rows)][i]
            while val == None:
                val = rows[self.__getrandominx(rows)][i]
            values.append(val)
        return self.__concatenate(values)
        
    def __getrandominx(self, rows) -> int:
        max = len(rows)
        return randint(1, max) - 1
