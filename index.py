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
except Exception as e:
    print('Connection Failed!\nError Code is %s;\nError Content is %s;' % (e.args[0],e.args[1]))
