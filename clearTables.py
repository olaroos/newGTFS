import MySQLdb

DB              = 'VBUSS'
DB_HOST         = '127.0.0.1'
DB_USER         = 'root'
DB_PASSWORD     = 'newpassword'

conn        = MySQLdb.Connection(db=DB, host=DB_HOST, user=DB_USER,passwd=DB_PASSWORD)
c           = conn.cursor()

c.execute("set autocommit = 1")
c.execute("""truncate table VL""")
conn.close()

DB              = 'VBUSS'
DB_HOST         = '188.226.223.188'
DB_USER         = 'root'
DB_PASSWORD     = 'lemmeltagetforti'

conn        = MySQLdb.Connection(db=DB, host=DB_HOST, user=DB_USER,passwd=DB_PASSWORD)
c           = conn.cursor()

c.execute("set autocommit = 1")
c.execute("""truncate table VL""")
conn.close()
