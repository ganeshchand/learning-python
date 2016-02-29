import ConfigParser
import cx_Oracle
import datetime
# Read Property File to get Database Information
config = ConfigParser.RawConfigParser()
config.read('config/config.cfg')
user = config.get('OracleDB', 'user')
password = config.get('OracleDB', 'password')
server = config.get('OracleDB', 'server')
port = config.get('OracleDB', 'port')
service = config.get('OracleDB', 'service')

# Create connection to Oracle DB
connStr = "{}/{}@{}:{}/{}".format(user, password, server, port, service)
print(connStr)
conn = cx_Oracle.connect(connStr)


sql ="""
SELECT
    DT_VAL
FROM
    DIM_DATE
WHERE rownum <=5
"""

dateValues = conn.cursor().execute(sql).fetchall()
print("Got following dates")
for dtime in dateValues:
    print(str(dtime[0].date()))  # convert datetime.datetime to datetime.date and convert to string
    # print(dtime) # prints datetime.datetime object


sql1 = "select sysdate from dual"
dates = conn.cursor().execute(sql1).fetchall()
for d in dates:
    # print d # prints datetime.datetime
    print str(d[0].date())
    # print(datetime.datetime.strptime(str(d[0]), "%m/%d/%Y"))







