import mysql.connector as msqc
import numpy as np

db = msqc.connect(
    host="localhost",
    username="root",
    password="  ",
    database="hotel",
)
cur = db.cursor(buffered=True)


class Roomavailable:

    def __init__(self, Date, Nbed, Name, Members, intime, contact_no, Day):
        self.Date = Date
        self.Nbed = Nbed
        self.Name = Name
        self.Members = Members
        self.intime = intime
        self.contact_no = contact_no
        self.Day = Day

    def bed(self):
        if (self.Nbed == 1):

            def get_room():
                ss = 'SELECT one_bed ,Available_one_bed from rooms where Available_one_bed = "A" '
                cur.execute(ss)
                available_room = cur.fetchone()[0]
                return available_room

            ro_no = get_room()
            print(ro_no)

            book_in = (self.Date, self.intime, self.Nbed, self.Name,
                       self.Members, self.contact_no, self.Day,
                       1500 * self.Day, ro_no)

            def book_room():
                s = 'UPDATE rooms SET Available_one_bed = "N/A" WHERE one_bed = ' + str(
                    ro_no)
                cur.execute(s)
                data_entry = 'INSERT INTO booking_details VALUES(%s , %s , %s , %s , %s , %s , %s , %s , %s)'
                cur.execute(data_entry, book_in)
                db.commit()

            book_room()

        if (self.Nbed == 2):

            def get_room():
                ss = 'SELECT two_beds , Available_two_bed from rooms where Available_two_bed = "A" '
                cur.execute(ss)
                available_room = cur.fetchone()[0]
                return available_room

            ro_no = get_room()
            print(ro_no)
            book_in = (self.Date, self.intime, self.Nbed, self.Name,
                       self.Members, self.contact_no, self.Day,
                       1500 * self.Day, ro_no)

            def book_room():
                s = 'UPDATE rooms SET Available_two_bed = "N/A" WHERE two_beds = ' + str(
                    get_room())
                cur.execute(s)
                data_entry = 'INSERT INTO booking_details VALUES(%s , %s , %s , %s , %s , %s , %s , %s , %s)'
                cur.execute(data_entry, book_in)
                db.commit()

            book_room()

        if (self.Nbed == 3):

            def get_room():
                ss = 'SELECT three_beds ,Available_three_bed from rooms where Available_three_bed = "A" '
                cur.execute(ss)
                available_room = cur.fetchone()[0]
                return available_room

            ro_no = get_room()
            print(ro_no)
            book_in = (self.Date, self.intime, self.Nbed, self.Name,
                       self.Members, self.contact_no, self.Day,
                       1500 * self.Day, ro_no)

            def book_room():
                s = 'UPDATE rooms SET Available_three_bed = "N/A" WHERE three_beds = ' + str(
                    get_room())
                cur.execute(s)
                data_entry = 'INSERT INTO booking_details VALUES(%s , %s , %s , %s , %s , %s , %s , %s , %s)'
                cur.execute(data_entry, book_in)
                db.commit()

            book_room()


class Person_search:

    def __init__(self, Name):
        # self.Room_no = Room_no
        self.Name = Name

    def search(self):
        ss = 'SELECT * FROM booking_details'
        cur.execute(ss)
        data = cur.fetchall()
        for enteries in data:
            if (enteries[3] == self.Name):
                print(enteries)
