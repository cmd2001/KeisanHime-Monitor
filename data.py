import sqlite3
from utils import unix_timestamp

class Database:
    def __init__(self, path, config_path): # todo: import config
        self.con = sqlite3.connect(path)
        self.execute('CREATE TABLE IF NOT EXISTS Server(ID INT PRIMARY KEY, uid TEXT, detail TEXT, belong INT, last_seen_time INT)')
        self.execute('CREATE TABLE IF NOT EXISTS Cluster(ID INT PRIMARY KEY, detail TEXT)')

    def execute(self, sql, par=()):
        con = self.con
        cur = con.cursor()
        try:
            cur.execute(sql, par)
            con.commit()
        except:
            con.rollback()
        finally:
            cur.close()

    def update_last_seen_time(self, uid):
        self.execute('UPDATE Server SET last_seen_time = ? WHERE uid = ?', (str(unix_timestamp()), uid))

    def get_all_server(self):
        con = self.con
        cur = con.cursor()
        cur.execute('SELECT ID, detail FROM Cluster')
        clusters = cur.fetchall()
        cur.close()
        ret = []
        for cluster in clusters:
            ng = [cluster[1]]
            cur = con.cursor()
            cur.execute('SELECT uid, detail, last_seen_time FROM Server WHERE ')
            cur.close()