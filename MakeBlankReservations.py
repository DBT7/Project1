import MySQLdb
import datetime

DEBUG = False

# Create a connection to the database
db = MySQLdb.connect(host="localhost",user="root", passwd = "100515", db ="dbproject")

# Create cursor object
cursor = db.cursor()

######################################################################################
# For purposes of getting the syntax correct for imputing back into the database
######################################################################################
if DEBUG == True:
    sql = 'SELECT Reservation_id, Reservation_dt, Duration, reservation_comment_id, ' \
          'resource_id, Room_Room_id, user_user_id FROM reservation'
    try:
        # Execute sql command
        cursor.execute(sql)

        # Fetch all the results
        results = cursor.fetchall()
        print results

    except:
        print 'ERROR: Unable to fetch data'

else:
    # Create all new reservations appointments
    print 'Creating all new blank reservations'

    # Insert two weeks of blank reservations so that there can be something in the views
    #INSERT INTO `dbproject`.`reservation` (`Reservation_id`, `Reservation_dt`, `Room_Room_id`) VALUES ('4', '2015-11-20 08:00:00.000000', '2');

    #make sql query
    current_number_rooms = 2
    start_date = datetime.date.today()
    date_increment = datetime.timedelta(days = 14)
    end_date = start_date + date_increment
    start_datetime = datetime.datetime(year=start_date.year, month=start_date.month, day=start_date.day, hour=8 )
    end_datetime = datetime.datetime(year=end_date.year, month=end_date.month, day=end_date.day, hour=17)
    time_increment = datetime.timedelta(minutes=30)

    reservation_id = 1

    for room in range(1, current_number_rooms+1):
        time = start_datetime
        while time < end_datetime:

            if time.day < 5:
                sql = "INSERT INTO reservation (Reservation_id, Reservation_dt, Room_Room_id) VALUES ( '{}', '{}', '{}' );".format(reservation_id, time, room)
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    print "Failed"
                    print sql
                    db.rollback()


                # Increment the reservation_id
            reservation_id+=1

            # Increment the time
            print time
            time += time_increment

# Disconnect from the database
db.close()