import pymysql, sys
try:
    db=pymysql.connect(host="localhost", user="root", passwd="", db="foodblog")
except Exception as e:
    sys.exit(e)