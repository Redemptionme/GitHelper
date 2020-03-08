#!/usr/bin/env python3
import os
import sys
import platform
import csv
import time
import re
import git
from git import *


platformName = platform.system()

# 安装准备软件，目前只支持Windows
def prepareGitPython(ptName):     
    print("--------安装GitPythonGitPython-----------")
    if ptName == "Windows" :
        os.system("pip install GitPython")    
        os.system("python -m pip install --upgrade pip") 
        
    else:
        os.system("#curl https://bootstrap.pypa.io/get-pip.py | python3")
        os.system("pip3 install GitPython")
    print("--------安装GitPythonGitPython Done---------------------")

# 将\\换/
def changePath(path):
    return eval(repr(path).replace('\\\\', '/'))

# 初始化csv模块
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

# 读取主模块的子模块配置，返回所有子模块的列表
def readSubModuleCfg(path):
    subModuleList = []
    modulesTag = 1
    listTag = 1
    with open(path,'r') as modulesFile:
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
                modulesTag = 1
                subModuleData['branch'] = line
                subModuleList.append(dict(subModuleData)) 
                listTag += 1
    return  subModuleList

# def updateSubModule(repo):
#     for submodule in repo.submodules: 
#         submodule.update(init=True,recursive=True)
#         sub_repo = submodule.module()
#         sub_repo.remote().pull()
#         updateSubModule(sub_repo)

def pullAll(repo):
    repo.remote().pull()
    for submodule in repo.submodules:
        sub_repo = submodule.module()
        pullAll(sub_repo)

def mergeAll():
    print('null')

def mainModule(url,path,branch_name):
    
    bGitFiles = False
    if os.path.exists(path + "/.git"): 
        bGitFiles = True

    if bGitFiles:
        repo = Repo(path)
    else:    
        repo = git.Repo.clone_from(url, path, branch=branch_name)

    remote = repo.remote()
    remote.fetch()
    remote.pull()

    #获取本地分支
    print([str(b) for b in repo.branches])
    #获取远端分支
    print(repo.git.branch('-r'))
    print(repo.git.branch())
    for ref in repo.git.branch('-r').split('\n'):
        print(ref)
    
    for submodule in repo.submodules: 
        submodule.update(init=True,recursive=True)
        submodule.module().remote().pull()
    
    pullAll(repo)
    print(repo.git.status())   # 返回通常的status几句信息
    print(repo.is_dirty())    # 返回是否有改动（包括未add和未commit的）

    # 添加文件 可以是单个文件名，也可以是`[ ]`数组，还可以是`.`代表全部
    #print(repo.git.add( '文件名' ))

    # commit提交
    #print(repo.git.commit( m='提交信息' ))
    # 获取活动分支、未被管理的文件和判断是否有变更
    # repo.is_dirty()  #返回布尔值
    # repo.untracked_files    #返回未被管理的文件列表

    
    #repo=git.Git('/data/test4')
    # repo.checkout('debug')
    # print(repo.status())
    # #所有git支持的命令这里都支持
   
    #repo.create_head('debug') # 创建分支
    #repo.create_tag('v1.0') # 创建tag
    #     3. 回滚
    # repo.index.checkout(['a.txt']) # 回滚缓存区文件
    # repo.index.reset(commit='486a9565e07ad291756159dd015eab6acda47e25',head=True) #回滚版本库文件
        


#prepareGitPython(platformName)
curFileList = os.path.split(os.path.realpath(__file__))
pyFiles = curFileList[0]
pyFiles = changePath(pyFiles)
#pyPath = __file__
newFiles = pyFiles[: - 26] + "/test" 
#initConfig(pyFiles + "/config")
#readConfig(pyFiles + "/config/cfg.csv")
 
mainModule('https://gitlab.skyunion.net/hanlinhe/tfather.git',newFiles,'master')
_subModuleList = readSubModuleCfg(newFiles + "/.gitmodules")

#updateSubModule(_subModuleList)






# 判断分支是否存在
# does_exist = True
# try:
#     repo.git.checkout('branch_name')
# except repo.exc.GitCommandError:
#     does_exist = False

# print(does_exist)


# os.system("pause")    
