import configparser
import pymssql

# parse config 
cnf = configparser.ConfigParser()
cnf.read('cnf.ini')


cnx_mssql = pymssql.connect(user=cnf['mssqlDB']['user'],
                                    password=cnf['mssqlDB']['pass'],
                                    server=cnf['mssqlDB']['server'],
                                    database=cnf['mssqlDB']['db'])

