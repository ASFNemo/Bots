import psycopg2

class DB(object):

    '''
        This class is for the database connectivity:
        - inputing yaks (and oter info about it)
        - deleting yaks
        - recovering specific yak,
        - recovering random yak
    '''

    def __init__(self):
        self.connection = psycopg2.connect(database="testdb", user="asherfischbaum", password="123",
                                           host="127.0.0.1", port="5432")
        print "db opened successfully"

        cursor = self.connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS yaks" +
                       "ID      SERIAL  PRIMARY KEY," +
                       "yak     TEXT    NOT NULL" +
                       "imgurl  TEXT"+
                       "upvotes INT     NOT NULL")

        print "table created successful"

        self.connection.commit()

    def add_yak(self, yak, image, upvotes):
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO yak(yak, imgurl, upvotes)" +
                       "(\'"+yak+"\', \'"+image+"\', "+upvotes+")")
        self.connection.commit()

