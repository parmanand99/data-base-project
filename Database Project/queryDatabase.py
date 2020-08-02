import sqlite3


def getBusBwStations(source, destination):
    try:
        connection = sqlite3.connect('myTable.db')
        cursor = connection.cursor()
        # source=input("Enter your query Source : ").upper()
        # destination= input("Enter you destination : ").upper()
        cursor.execute(f'select DISTINCT bus_no, total_seats, departure_time from bus where source =="{source}" and destination=="{destination}"');
        result=cursor.fetchall()
        print(f"Total {len(result)} bus found between {source} and {destination} ")
        for i in result:
            print(f"Bus No. {i[0]} has {i[1]} seats available and will depart at {i[2]} ")
        print()
        cursor.close()
        connection.close()
        return result, source
    except:
        print("Check the details and try again")

def getBusRoute(busNo,source):
    try:
        connection = sqlite3.connect('myTable.db')
        cursor = connection.cursor()
        # busNo=input(f"Enter the bus No. from above list to know the route : ").upper()
        source=str(source).upper()
        cursor.execute(f'Select distinct pickup_point,drop_point from route where bus_no =="{busNo}"')
        result=cursor.fetchall()
        print(busNo,result,source)
        for i in result:
            if i[0]==source:
                print()
                print(f"The Journey of Bus No. {busNo} you enquired for, starts from {i[0]} and ends at {i[1]}.")
        cursor.close()
        connection.close()
        print()
    except:
        print("Check the details and try again")

def getBusDetails(busNo):
    try:
        connection = sqlite3.connect('myTable.db')
        cursor = connection.cursor()
        cursor.execute(f'Select gst_no from bus_belongsto where bus_no =="{busNo}"')
        gstNo=cursor.fetchall()
        result=cursor.execute(f'select agency_name, state from travel_agency where gst_no=="{gstNo[0][0]}"')
        result=result.fetchall()
        print()
        print(f"The queried bus No.{busNo} has GST number {gstNo[0][0]} belongs to {result[0][0]} agency, {result[0][1]} ")
        print()
    except:
        print("Check the details and try again")

    cursor.close()
    connection.close()

