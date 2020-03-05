@echo off
set /p input=是否需要安装前置软件 git gitlfs tortoisegit  输入y/n:

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
echo !!!安装python切记设置环境变量
echo 即勾选 Add Python 3.x to PATH 即可
echo --------------------------------------
set /p input=是否要安装Python3 请输入y/n:
if "%input%"=="y" ( 
	echo %input% 
	echo Starting install python3...
	start /wait ./python-3.8.2.exe
) 