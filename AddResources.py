import MySQLdb
import os

# Create a connection to the database
db = MySQLdb.connect(host="localhost",user="root", passwd = "100515", db ="dbproject")

# Create cursor object
cursor = db.cursor()


print 'Creating Resources'


# { 'title', 'description'}
resource_list = [{'Projector', 'Panasonic Projector'}, {'Computer', 'Desktop Computer'},
                 {'White Board', '10 X 20 Dry Erase Board'}, {'Podium', 'Free Standing Lecturing Podium'}]

for title, description in resource_list:

    #INSERT INTO `dbproject`.`resource` (`Title`, `Description`) VALUES ('projector', 'projector');
    sql = "INSERT INTO resource (Title, Description) VALUES ('{}', '{}');".format(title, description)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "Failed"
        print sql
        db.rollback()

db.close()