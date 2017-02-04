#!/usr/bin/python3
# -*- utf8 -*-
#導入PyMySQL庫
import pymysql as mariadb
#測試連接MariaDB數據庫
try:
    conn = mariadb.connect(
        host='localhost',
        user='root',
        passwd='firstbank',
        db='firstbank',
        charset='utf8'
    )
    #設置cursor
    cursor = conn.cursor()
    #撰寫SQL語句
    sql = "select version()"
    #執行SQL語句
    cursor.execute(sql)
    #獲取SQL語句返回內容
    #fetchall, fetchone
    data = cursor.fetchone()
    print('Database Version is %s' % data)
    #關閉cursor
    cursor.close()
    #關閉數據庫連接
    conn.close()
except Exception as e:
    print('Connection Failed!\nError Code is %s;\nError Content is %s;' % (e.args[0],e.args[1]))
