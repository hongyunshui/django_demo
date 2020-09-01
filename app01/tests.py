from django.test import TestCase

# Create your tests here.
import sqlite3
cn = sqlite3.connect('../db.sqlite3')
cur = cn.execute('select * from common')
print(cur.fetchmany(2))
