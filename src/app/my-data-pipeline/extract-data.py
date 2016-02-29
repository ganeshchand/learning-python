"""
This script gets data from Oracle database
"""

import csv
import os
import cx_Oracle
import ConfigParser

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

homeownersTranSql = """SELECT
    "DIM_PRODUCT"."CONF_LINE_DIV_SHORT_TEXT" AS "Line_Division",
    "DIM_PRODUCT"."CONF_LOB_SHORT_TEXT" AS "Line_of_Business",
    CASE
        WHEN
            CAST(TO_CHAR("DIM_MONTH_ACCTG_PRD"."YR_NO",'TM9','NLS_NUMERIC_CHARACTERS = ''.,'' ') AS CHAR(4)) IS NULL OR
            "DIM_MONTH_ACCTG_PRD"."MTH_NO" IS NULL
            THEN
                NULL
        ELSE CAST(TO_CHAR("DIM_MONTH_ACCTG_PRD"."YR_NO",'TM9','NLS_NUMERIC_CHARACTERS = ''.,'' ') AS CHAR(4)) || ' - ' || "DIM_MONTH_ACCTG_PRD"."MTH_NO"
    END AS "Accounting_Year_and_Month",
    CAST("DIM_DATE_TRANS_PROC_DT"."DT_VAL" AS DATE) AS "Transaction_Process_Date",
    COUNT(DISTINCT "V_FACT_LOSS_TRAN"."LOSS_TRANS_ID") AS "Transaction_Count",
    SUM("V_FACT_LOSS_TRAN"."TRANS_AMT") AS "Transaction_Amount",
    SUM("V_FACT_LOSS_TRAN"."RSRV_CHNG_AMT") AS "Reserve_Change_Amount"
FROM
    "DIM_DATE" "DIM_DATE_TRANS_PROC_DT"
        INNER JOIN "V_FACT_LOSS_TRAN" "V_FACT_LOSS_TRAN"
        ON "DIM_DATE_TRANS_PROC_DT"."DT_ID" = "V_FACT_LOSS_TRAN"."TRANS_PROC_DT_ID"
            INNER JOIN "DIM_MONTH" "DIM_MONTH_ACCTG_PRD"
            ON "DIM_MONTH_ACCTG_PRD"."MTH_ID" = "V_FACT_LOSS_TRAN"."ACCTG_PRD_ID"
                INNER JOIN "DIM_PRODUCT" "DIM_PRODUCT"
                ON "DIM_PRODUCT"."PRODUCT_ID" = "V_FACT_LOSS_TRAN"."PRODUCT_ID"
WHERE
    "DIM_PRODUCT"."CONF_LOB_SHORT_TEXT" IN (
        'Home Owners' )
GROUP BY
    "DIM_PRODUCT"."CONF_LINE_DIV_SHORT_TEXT",
    "DIM_PRODUCT"."CONF_LOB_SHORT_TEXT",
    CASE
        WHEN
            CAST(TO_CHAR("DIM_MONTH_ACCTG_PRD"."YR_NO",'TM9','NLS_NUMERIC_CHARACTERS = ''.,'' ') AS CHAR(4)) IS NULL OR
            "DIM_MONTH_ACCTG_PRD"."MTH_NO" IS NULL
            THEN
                NULL
        ELSE CAST(TO_CHAR("DIM_MONTH_ACCTG_PRD"."YR_NO",'TM9','NLS_NUMERIC_CHARACTERS = ''.,'' ') AS CHAR(4)) || ' - ' || "DIM_MONTH_ACCTG_PRD"."MTH_NO"
    END,
    CAST("DIM_DATE_TRANS_PROC_DT"."DT_VAL" AS DATE)"""

homeownersTranSql = conn.cursor().execute(homeownersTranSql)
rows = homeownersTranSql.fetchall()
print("fetched {} rows".format(len(rows)))
for row in rows:
    print(row)

fields = ['Line Division','Line of Business','Accounting Year and Month','Transaction Process Date','Transaction Count','Transaction Amount', 'Reserve Change Amount']
# write to a file
outputFile = open("data/input/homeowners-tran.csv", 'wb')
csvWriter = csv.writer(outputFile)
csvWriter.writerow(fields)
csvWriter.writerows(row for row in rows)

outputFile.close()

conn.close()


# Filter



