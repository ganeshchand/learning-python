import cx_Oracle

# connection = raw_input("Enter Oracle DB connection (uid/pwd@database) : ")
connection = cx_Oracle.connect('IC_8_TEST_CI_8_1/gw@dmdboracle1:12101/emerasc')
# orcl = cx_Oracle.connect(connection)
# curs = orcl.cursor()
curs = connection.cursor()

printHeader = True  # include column headers in each table output

sql = "select * from DIM_AGENCY"  # get a list of all tables
curs.execute(sql)

# -- simple one-row fetch.
# -- returns None when there is no more data

print(curs.fetchone())

# -- iterating over a cursor
# -- best way to loop over a results set

curs.execute('select AGCY_CD,AGCY_STATE_CD  from DIM_AGENCY')
for row in curs:
    print row

print("With Predicates")
# -- fetch all rows in one call
curs.execute("""select AGCY_CD,AGCY_STATE_CD  from DIM_AGENCY where AGCY_CD not in('?',' ') AND AGCY_STATE_CD not in('?',' ')""")
for row in curs:
    print row
print(len(curs.fetchall()))
# for column1, column2 in curs.fetchall():
#     print column1, "\t", column2, "\t"

# print(curs.fetchall())
# print()
# pairs = [('?', '?'), (' ', ' ')]
# print(pairs)
# print(type(pairs))
# print(len(pairs))


# Using positional parameters
print("Looking for agents in CA only")
caAgents = curs.execute("""select AGCY_CD,AGCY_STATE_CD
                from DIM_AGENCY
                where AGCY_CD not in('?',' ') AND AGCY_STATE_CD not in('?',' ')
                AND AGCY_STATE_CD = :AGCY_STATE_CD""", AGCY_STATE_CD='CA')
for row in caAgents:
    print row
print("Total Agents in CA: {}").format(len(caAgents.fetchall()))



