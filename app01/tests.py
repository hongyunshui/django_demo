from django.test import TestCase

# Create your tests here.
import sqlite3
cn = sqlite3.connect('../db.sqlite3')
cur = cn.execute('select * from "餐饮巡查台账"')

print(cur.fetchmany(2))