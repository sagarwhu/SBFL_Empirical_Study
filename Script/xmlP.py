#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.dom import minidom
import MySQLdb as mdb

# Database connection
host = 'localhost'
user = 'root'
password = 'root'
database = 'SBFL'
connection = mdb.connect(host, user, password, database)
try:
    cursor = connection.cursor()
    print "Connected successfully"
except:
    print "Unable to connect"
# try:
#     insert_query = """INSERT INTO Statement (statementNumber, statementHitNumber, testcaseID) VALUES (4,1,4)""")
#     cursor.execute(insert_query)
#     connection.commit();
# except:
#     print "problem found"
# connection.close()



doc = minidom.parse("tc4_S.xml")

# doc.getElementsByTagName returns NodeList
testcaseID = 4
linesNumber = doc.getElementsByTagName("line")
for linesNumberofStatement in linesNumber:
        hitsofEachStatement = linesNumberofStatement.getAttribute("hits")
        statementNumber = linesNumberofStatement.getAttribute("number")
        print("Statement Number:%s, Hit:%s" %
              (statementNumber, hitsofEachStatement))
        # try:
        #     insert_query = ("INSERT INTO Statement (statementNumber, statementHitNumber, testcaseID) VALUES (%s,%s,%s)", (statementNumber,hitsofEachStatement,testcaseID))
        #     cursor.execute(insert_query)
        #     connection.commit();
        # except:
        #     print "problem found"
