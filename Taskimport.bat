@echo off
echo Importing All Tasks
echo.
schtasks.exe /create /TN "BEE ATTENDANCE" /XML "C:\Attendance Automation\Tasks\BEE ATTENDANCE.xml"
schtasks.exe /create /TN "ED ATTENDANCE" /XML "C:\Attendance Automation\Tasks\ED ATTENDANCE.xml"
schtasks.exe /create /TN "EME ATTENDANCE" /XML "C:\Attendance Automation\Tasks\EME ATTENDANCE.xml"
schtasks.exe /create /TN "ENGLISH ATTENDANCE" /XML "C:\Attendance Automation\Tasks\ENGLISH ATTENDANCE.xml"
schtasks.exe /create /TN "MATHS ATTENDANCE" /XML "C:\Attendance Automation\Tasks\MATHS ATTENDANCE.xml"
schtasks.exe /create /TN "PHYSICS ATTENDANCE" /XML "C:\Attendance Automation\Tasks\PHYSICS ATTENDANCE.xml"
echo.
echo Importing Done
echo.
pause