desc = """top N rows of query"""

notes = """
This selects the first N rows of a query. If you are looking for the SELECT...LIMIT clause, this is the format.
Note that ROWNUM starts at 1 and not 0
"""

import sys
import cx_Oracle


def demo(conn, curs):
    # the first 5 rows of the subquery

    curs.execute("""select * from (
                        select * from DIM_AGENCY order by AGCY_ID
                    ) where rownum <=5""")
    for r in curs:
        print(r[0], r[1], r[2])


def filterTable(conn, curs, table, columnToFilter, filterValue):
    curs.execute("""select * from DIM_AGENCY order by AGCY_ID""")


def parameterizedTable(conn, curs, tableName):
    curs.execute('select * from :table order by AGCY_ID', table=tableName)
    print("Counting total rows in {} table".format(tableName))
    count = 0;
    for i in curs:
        count += 1
    print("Total Rows: {}".format(count))


def parameterizedSQL(conn, curs, x, y):
    print(x, y)
    curs.execute('select :x * :y from dual', x=x, y=y)
    for r in curs:
        print(r[0])


def countRows(conn, curs):
    curs.execute("""select count(*) as count
                    from DIM_CLAIM C,
                         FACT_LOSS_TRAN F
                    where C.CLAIM_ID = F.CLAIM_ID and ROWNUM <=5""")

    for r in curs:
        print("Toral Row Count: {}".format(str(r[0])))

if __name__ == '__main__':
    connstr = 'IC_8_TEST_CI_8_1/gw@dmdboracle1:12101/emerasc'
    conn = cx_Oracle.connect(connstrm)
    curs = conn.cursor()
    # demo(conn,curs)
    # filterTable(conn, curs, 'DIM_AGENCY', 'SOURCE_SYSTEM', 'GWPC')
    # parameterizedSQL(conn, curs, 2, 5)
    # parameterizedTable(conn,curs,'DIM_AGENCY')
    countRows(conn, curs)
    conn.close()
