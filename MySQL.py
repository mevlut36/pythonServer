# from pip._internal import main
# main(['install','mysql-connector-python-rf'])
import mysql.connector
import self as self


class DB:
    """ Creating a DB, (host, user, password, db) """
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def conn(self):
        """ Connection to a database """
        try:
            c = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.db)
            return c
        except:
            print("Connection failed.")
            exit(1)

    def select(self, table, selected):
        """ MySQL SELECT method (SELECT {id} from {table}) """
        cn = self.conn()
        cur = cn.cursor()
        cur.execute("SELECT {0} from {1}".format(selected, table))
        return cur.fetchone()

    def createDB(self, name):
        """ Create a db, (CREATE DATABASE {name}) """
        cn = self.conn()
        cur = cn.cursor()
        if name:
            return False
        else:
            cur.execute("CREATE DATABASE {0}".format(name))

    def checkAllDB(self):
        """ Check all DB """
        cn = self.conn()
        cur = cn.cursor()
        cur.execute("SHOW DATABASES")
        for x in cur:
            return x

    def checkTable(self):
        """ Check all tables """
        cn = self.conn()
        cur = cn.cursor()
        cur.execute("SHOW TABLES")
        for x in cur:
            return x

    def createTable(self, name, arg):
        """ Create table (CREATE TABLE {name} ({element}))"""
        cn = self.conn()
        cur = cn.cursor()
        if name:
            return False
        else:
            cur.execute("CREATE TABLE {0} ({1})".format(name, arg))

    def removeTable(self, name):
        """ Remove a table {name} """
        cn = self.conn()
        cur = cn.cursor()
        cur.execute("DROP TABLE {0}".format(name))

    def update(self, table, arg):
        """ Update table """
        cn = self.conn()
        cur = cn.cursor()
        cur.execute("UPDATE {0} SET {1}".format(table, arg))

    def join(self, table1, table2, how):
        """ Join two tables, how=RIGHT | LEFT """
        cn = self.conn()
        cur = cn.cursor()
        if how == "RIGHT":
            cur.execute("SELECT {0}.name AS user, {1}.name AS favorite FROM {0} RIGHT JOIN {1} ON {0}.fav = {0}.id".format(table1, table2))
        elif how == "LEFT":
            cur.execute("SELECT {0}.name AS user, {1}.name AS favorite FROM {0} LEFT JOIN {1} ON {0}.fav = {0}.id".format(table1, table2))
        else:
            return False
