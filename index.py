import pymysql

pymysql.install_as_MySQLdb()

import MySQLdb
db = MySQLdb.connect("localhost" , "root" , "firstbank")

