REM help: schtasks /Create /?
REM In Windows, the command line program with the lovely name schtasks is responsible
REM for creating, querying, and deleting tasks, and does even more.


REM creates a livelog that is written every minute:
schtasks /Create /SC MINUTE /TN Livelog /TR job.bat

REM run twice every week, at 4 o’clock in the morning
schtasks /Create /SC WEEKLY /D TUE,SAT /ST 04:00 /TN PerformAction /TR job.bat

REM Query running tasks

schtasks /Query /TN Livelog

schtasks /Query /TN PerformAction

REM Delete tasks
schtasks /Delete /TN Livelog
schtasks /Delete /TN PerformAction

