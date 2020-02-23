import os
import sqlite3

# cd into user folder
os.chdir(os.path.expanduser("~"))

# Initialize connection
DB_NAME = ".qc.sql.db"
conn = sqlite3.connect(DB_NAME)
print("opened %s" % DB_NAME)


def sql(query, params=None):
    c = conn.cursor()
    try:
        c.execute(query, params)
        conn.commit()
    except Exception as e:
        print(e)
