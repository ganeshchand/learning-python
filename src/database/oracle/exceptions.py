desc = """Handling an oracle exception"""

notes = """
cx_Oracle will throw cx_Oracle.DatabaseError exceptions.  Here's how
to extract the oracle error code and error message.
"""

output = """
   Exception: ORA-01476: divisor is equal to zero
   ErrorCode: 1476
ErrorMessage: ORA-01476: divisor is equal to zero
"""

import sys
import cx_Oracle


def demo(conn, curs):
    try:
        curs.execute('select 1/0 from dual')
    except cx_Oracle.DatabaseError, e:
        print ("Exception: {}".format(e))
        errorObj = e.args
        print("Error Code: {}".format(errorObj.code))
        print("Error Messsage: {}".format(errorObj.message))

if __name__ == "__main__":
    constr = ""
    print(sys.argv)
    if len(sys.argv) < 2:
        constr = 'IC_8_TEST_CI_8_1/gw@dmdboracle1:12101/emerasc'
    else:
        constr = sys.argv[1]

    conn = cx_Oracle.connect(constr)
    curs = conn.cursor()
    demo(conn, curs)
    conn.close()
