from database.DB_connect import DBConnect
from model.airport import Airport


class DAO():

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * from airports a order by a.AIRPORT asc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(**row))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getFlightsOrigin(numero):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select f.ORIGIN_AIRPORT_ID
from flights f
group by f.ORIGIN_AIRPORT_ID 
having count(distinct (f.AIRLINE_ID)) >= %s"""

        cursor.execute(query,(numero,))

        for row in cursor:
            result.append(int(row["ORIGIN_AIRPORT_ID"]))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getFlightsDestination(numero):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select f.DESTINATION_AIRPORT_ID
from flights f
group by f.DESTINATION_AIRPORT_ID 
having count(distinct (f.AIRLINE_ID)) >= %s"""

        cursor.execute(query,(numero,))

        for row in cursor:
            result.append(int(row["DESTINATION_AIRPORT_ID"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getFlights():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct f.ORIGIN_AIRPORT_ID ,f.DESTINATION_AIRPORT_ID
from flights f
where f.ORIGIN_AIRPORT_ID < f.DESTINATION_AIRPORT_ID 
order by f.ORIGIN_AIRPORT_ID asc"""

        cursor.execute(query)

        for row in cursor:
            result.append((int(row["DESTINATION_AIRPORT_ID"]),int(row["ORIGIN_AIRPORT_ID"])))

        cursor.close()
        conn.close()
        return result