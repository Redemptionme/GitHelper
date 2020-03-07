#!/usr/bin/env python3
import os
import sys
import platform
import csv
import time

platformName = platform.system()

def prepareGitPython(ptName):     
    print("--------安装GitPythonGitPython-----------")
    if ptName == "Windows" :
        os.system("pip install GitPython")    
        os.system("python -m pip install --upgrade pip") 
        
    else:
        os.system("#curl https://bootstrap.pypa.io/get-pip.py | python3")
        os.system("pip3 install GitPython")
    print("--------安装GitPythonGitPython Done---------------------")


def changePath(path):
    return eval(repr(path).replace('\\\\', '/'))

def initConfig(confiPath):    
    if not os.path.exists(newFiles):
        os.makedirs(newFiles)

    if not os.path.exists(confiPath):
        os.makedirs(confiPath)

    fileName = confiPath +'/cfg.csv'
    fileName = changePath(fileName)

    if not os.path.exists(fileName):        
        file = open(fileName,'w')
        time_local = time.localtime(time.time())
        #转换成新的时间格式(2016-05-05 20:28:54)
        curTime = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
        
        file.close()        
        with open(fileName, 'w',newline='',encoding='utf-8') as csvfile:        
            headers = ['Project','IsMainGit','ProjectName','ProjectPath','GitPath','Branch']
            rows = [(newFiles, 1, 'TFather', newFiles, 'http', 'feature/develop')]
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows) 
            csvfile.close()

def readConfig(filepath):
    with open(filepath) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print(row)

prepareGitPython(platformName)
pyPath = sys.path[0] 
newFiles = pyPath[: - 26] + "/test"
newFiles = changePath(newFiles)
initConfig(pyPath + "/config")
readConfig(pyPath + "/config/cfg.csv")

  
# print(os.getcwd()) #d:\workplace\Qt\GitHelper\GitHelper\tools
# print(sys.path[0])

# print(__file__) #D:\workplace\Qt\GitHelper\GitHelper\tools\start.py
# print(os.path.abspath(__file__))
# print(os.path.realpath(__file__))

# print(os.path.split(os.path.realpath(__file__))) #('D:\\workplace\\Qt\\GitHelper\\GitHelper\\tools', 'start.py')


import git
from git import *

gitFiles = newFiles + "/.git"
bGitFiles = False
if os.path.exists(gitFiles): 
    bGitFiles = True

if bGitFiles:
    repo = Repo(newFiles)
else:    
    repo = git.Repo.clone_from('https://gitlab.skyunion.net/hanlinhe/tfather.git', newFiles, branch='master')

remote = repo.remote()
remote.fetch()
import re


subModuleList = []
modulesTag = 1
with open(newFiles + "/.gitmodules",'r') as modulesFile:
    subModuleData = {'submodule': '', 'path': '', 'url': '','branch':''}
    for line in modulesFile.readlines():
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        line = re.sub(r"\s+", "", line) #去掉空格
        if modulesTag == 1:
            line = line.replace('[submodule"','')
            line = line.replace('"]','')
            modulesTag += 1
            subModuleData['submodule'] = line
        elif modulesTag == 2:
            line = line.replace('path=','')
            modulesTag += 1
            subModuleData['path'] = line
        elif modulesTag == 3:
            line = line.replace('url=','')
            modulesTag += 1
            subModuleData['url'] = line
        elif modulesTag == 4:
            line = line.replace('branch=','')
            modulesTag == 1
            subModuleData['branch'] = line
            subModuleList.insert(subModuleData) 

#获取本地分支
print([str(b) for b in repo.branches])
#获取远端分支
print(repo.git.branch('-r'))
for ref in repo.git.branch('-r').split('\n'):
    print(ref)


remote.pull()

# 判断分支是否存在
# does_exist = True
# try:
#     repo.git.checkout('branch_name')
# except repo.exc.GitCommandError:
#     does_exist = False

# print(does_exist)


# os.system("pause")    
