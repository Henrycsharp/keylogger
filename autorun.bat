schtasks /create /tn "MyPythonScript" /tr "pythonw.exe C:\path\to\your\script.py" /sc onlogon /f
echo %autorun created%
