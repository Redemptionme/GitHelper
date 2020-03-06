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
    else:
        os.system("#curl https://bootstrap.pypa.io/get-pip.py | python3")
        os.system("pip3 install GitPython")
    print("--------安装GitPythonGitPython Done---------------------")


prepareGitPython(platformName)

selfpath = sys.path[0]
 

path = sys.path[0]
path = path[: - 26]

newFiles = path + "/test"
newFiles = eval(repr(newFiles).replace('\\\\', '/'))



if not os.path.exists(newFiles):
    os.makedirs(newFiles)

def initConfig(confiPath):
    if not os.path.exists(confiPath):
        os.makedirs(confiPath)

    fileName = confiPath +'/cfg.csv'

    if not os.path.exists(fileName):        
        file = open(fileName,'w')
        time_local = time.localtime(time.time())
        #转换成新的时间格式(2016-05-05 20:28:54)
        curTime = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
        
        file.close()        
        with open(fileName, 'w',newline='',encoding='utf-8') as csvfile:        
            headers = ['TimeKey','IsMainGit','ProjectName','ProjectPath','GitPath','Branch']
            rows = [(curTime, 1, 'TFather', newFiles, 'http', 'feature/develop')]
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
    
    # with open(fileName, 'w',newline='',encoding='utf-8') as csvfile:       
    # headers = ['Time','IsMainGit','ProjectName','ProjectPath','GitPath','Branch']
    # rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
    #         ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
    #         ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
    #     ]
    # writer = csv.writer(csvfile)
    # writer.writerow(headers)
    # writer.writerows(rows)
    #reader = csv.reader(csvfile)
    #reader = csv.reader(csvfile)
        
    #file.close() 
initConfig(selfpath + "/config")

print(os.getcwd()) #d:\workplace\Qt\GitHelper\GitHelper\tools
print(sys.path[0])

print(__file__) #D:\workplace\Qt\GitHelper\GitHelper\tools\start.py
print(os.path.abspath(__file__))
print(os.path.realpath(__file__))

print(os.path.split(os.path.realpath(__file__))) #('D:\\workplace\\Qt\\GitHelper\\GitHelper\\tools', 'start.py')


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
remote.pull()

# os.system("pause")    
