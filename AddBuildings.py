import MySQLdb
import os

# Create a connection to the database
db = MySQLdb.connect(host="localhost",user="root", passwd = "100515", db ="dbproject")

# Create cursor object
cursor = db.cursor()


print 'Creating Buildings'
# name
building_list = ['Seman Center']


for name in building_list:

    sql = "Insert INTO building (Name) VALUES ('{}');".format(name)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "Failed"
        print sql
        db.rollback()

db.close()