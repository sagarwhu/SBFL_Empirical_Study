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

def testcaseNumberHitInsertFromXml():
    doc = minidom.parse("tc7_F.xml")

    # doc.getElementsByTagName returns NodeList
    testcaseID = 7
    linesNumber = doc.getElementsByTagName("line")
    for linesNumberofStatement in linesNumber:
        hitsofEachStatement = linesNumberofStatement.getAttribute("hits")
        statementNumber = linesNumberofStatement.getAttribute("number")
        print("Statement Number:%s, Hit:%s" %
              (statementNumber, hitsofEachStatement))
        try:
            insert_query = "INSERT INTO Statement (statementNumber, statementHitNumber, testcaseID) VALUES (%s,%s,%s)"
            cursor.execute(insert_query, (statementNumber,hitsofEachStatement,testcaseID))
            connection.commit();
        except:
            print "problem found"

def all_failed_testcases():
    """Listing all the failed testcases(a11+a01) from the database """
    cursor.execute("SELECT COUNT(*) FROM Testcase WHERE testcaseStatus = 0")
    data = cursor.fetchone()[0]
    print data



def all_passed_testcases():
    """Listing all the passed testcases(a10+a00) from the database """
    cursor.execute("SELECT COUNT(*) FROM Testcase WHERE testcaseStatus >= 1")
    data = cursor.fetchone()[0]
    return data

#all_failed_testcases()
a10_a00 = all_passed_testcases()
#print a10_a00
