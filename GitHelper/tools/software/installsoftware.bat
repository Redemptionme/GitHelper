@echo off
set /p input=�Ƿ���Ҫ��װǰ����� git gitlfs tortoisegit  ����y/n:

if "%input%"=="y" ( 
    echo %input% 
	echo Starting install Git...
	start /wait ./Git-2.25.1-64-bit.exe
	echo Starting install Git LFS...
	start /wait ./git-lfs-windows-v2.10.0.exe
	echo Starting install TortoiseGit...
	start /wait ./TortoiseGit-2.10.0.0-64bit.msi	
	
	)
echo -----------------------------------------------
echo !!!��װpython�м����û�������
echo ����ѡ Add Python 3.x to PATH ����
echo --------------------------------------
set /p input=�Ƿ�Ҫ��װPython3 ������y/n:
if "%input%"=="y" ( 
	echo %input% 
	echo Starting install python3...
	start /wait ./python-3.8.2.exe
) 