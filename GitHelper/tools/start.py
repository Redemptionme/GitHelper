#!/usr/bin/env python3
import os
import sys
import platform
import csv
import time
import re
import git
from git import *
import shutil



# os.system("pip install PyQt5")
# os.system("pip install PyQt5-tools")
 
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个应用

    w = QWidget()  # 在这个应用条件下创建一个窗口
    w.resize(500, 150)  # 重新设置大小
    w.move(100, 100)  # 移动下距离
    w.setWindowTitle("Hello world!")  # 设置标题
    w.show()  # 显示这个窗口

    sys.exit(app.exec_())  # 将app的退出信号传给程序进程，让程序进程退出

global bError
bError = False 

def printErr(parm):
    global bError
    bError = True
    print(parm)


global platformName
platformName = platform.system()

def isWin():
    return platformName == "Windows" 
def isMac():
    return platformName == "Darwin"

def openFiles(path):
    if isWin():
        os.system("start explorer %s" % path)
    elif isMac:
        #TODO mac
        print("TODO openFiles")

# 安装准备软件，目前只支持Windows
# git lfs install
def prepareGitPython(ptName):     
    print("--------安装GitPythonGitPython-----------")
    if isWin():
        os.system("pip install GitPython")    
        os.system("python -m pip install --upgrade pip") 
        
    elif isMac():
        os.system("#curl https://bootstrap.pypa.io/get-pip.py | python3")
        os.system("pip3 install GitPython")
    print("--------安装GitPythonGitPython Done---------------------")

# 将\\换/
def replacePathChar(path,oldchar,newchar):
    return eval(repr(path).replace(oldchar, newchar))

def changePath(path):
    return replacePathChar(path,'\\\\', '/')
    
def replaceRightFileName(path):
    path = eval(repr(path).replace('\\', '_'))
    path = eval(repr(path).replace('/', '_'))
    path = eval(repr(path).replace(':', '_'))
    path = eval(repr(path).replace('*', '_'))
    path = eval(repr(path).replace('?', '_'))
    path = eval(repr(path).replace('"', '_'))
    path = eval(repr(path).replace('<', '_'))
    path = eval(repr(path).replace('>', '_'))
    path = eval(repr(path).replace('|', '_'))
    return path

def iniCsvCfgKey(filesPath,csvName,csvTable):
    if not os.path.exists(filesPath):
        os.makedirs(filesPath)
    fileName = filesPath +'/' + csvName
    fileName = changePath(fileName)
    if not os.path.exists(fileName):        
        file = open(fileName,'w')
        #time_local = time.localtime(time.time())
        #转换成新的时间格式(2016-05-05 20:28:54)
        #curTime = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
        
        file.close()        
        with open(fileName, 'w',newline='',encoding='utf-8') as csvfile:        
            headers = csvTable
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            csvfile.close()
 
# 写入
def writeCsvByRow(filePath,headers,valueList): 
    if os.path.exists(filePath): 
        allList = []
        
        with open(filePath, 'r',newline='',encoding='utf-8') as csvfile:  
            f_csv = csv.reader(csvfile)
            curheaders = next(f_csv)       
            for row in f_csv:
                allList.append(row)
        if curheaders != headers:
            print('head not equal')

        allList.append(valueList)
                
        with open(filePath, 'w',newline='',encoding='utf-8') as csvfile:    
            f_csv = csv.writer(csvfile)
            f_csv.writerow(headers)
            f_csv.writerows(allList)
            csvfile.close()

def writeCsvByDict(filePath,headers,rows):
    with open(filePath, 'w',newline='',encoding='utf-8') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)
        f.close()
    

def readConfig(filepath,csvName,mainKey):
    outList = {}
    with open(filepath + '/' + csvName) as f:
        f_csv = csv.DictReader(f)
        #print(f_csv)                
        for row in f_csv:
            #outList.append(row)
            #print(row) 
            outList[row[mainKey]] = row
            
        #f_csv.# %%
    return outList
 
import errno, os, stat, shutil

def handle_remove_read_only(func, path, exc):
    excvalue = exc[1]
    if func in (os.rmdir, os.remove, os.unlink) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
    else:
      raise 

def removeFiles(path):
    if os.path.exists(path): 
        #shutil.rmtree(path) 
        shutil.rmtree(path, onerror=handle_remove_read_only)
        #os.mkdir(path)  
        #os.removedirs(path)

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
  

def IsFirstCheckOut(path):
    if os.path.exists(path + "/.git"): 
        return False
    return True

def initModule(url,path,branch_name,csvDataList):
    repo = git.Repo.clone_from(url, path, branch=branch_name)
    for submodule in repo.submodules: 
        submodule.update(init=True,recursive=True)
        subrepo = submodule.module()
        row = { keyHeaders[0]: changePath(subrepo.working_dir),
            keyHeaders[1]: replaceRightFileName(subrepo.working_dir),
            keyHeaders[2]: 0,
            keyHeaders[3]: submodule.url,
            keyHeaders[4]: changePath(subrepo.working_dir),
            keyHeaders[5]: submodule.branch_name}
        csvDataList.append(row)

def updateModule(url,path,branch_name,csvDataList):
    repo = Repo(path)
    print(repo.config_reader())
    remote = repo.remote() 

    for submodule in repo.submodules: 
        submodule.update(init=True,recursive=True)
        subrepo = submodule.module()
        row = { keyHeaders[0]: changePath(subrepo.working_dir),
            keyHeaders[1]: replaceRightFileName(subrepo.working_dir),
            keyHeaders[2]: 0,
            keyHeaders[3]: submodule.url,
            keyHeaders[4]: changePath(subrepo.working_dir),
            keyHeaders[5]: submodule.branch_name}
        csvDataList.append(row)

    try:
        remote.pull() 
    except GitCommandError as e:
        printErr(e)  
        


#https://blog.csdn.net/tenfyguo/article/details/7380836
#https://blog.csdn.net/qq_37291064/article/details/100311679
#https://cloud.tencent.com/developer/article/1520592

def commitAll(path):
    repo = Repo(path)
    bNothing = True
    for submodule in repo.submodules: 
        subrepo = submodule.module()
        if subrepo.is_dirty(untracked_files=True):
            bNothing = False
            if isWin():
                batStr = '"TortoiseGitProc.exe" /command:commit /path:' + subrepo.working_dir +' /closeonend:3'
                os.system(batStr)
            elif isMac():
                subrepo.git.commit( m='提交信息' )
     
    if repo.is_dirty(untracked_files=True):
        bNothing = False
        if isWin():
            batStr = '"TortoiseGitProc.exe" /command:commit /path:' + repo.working_dir +' /closeonend:3'
            os.system(batStr)
        elif isMac:
            repo.git.commit( m='提交信息' )
    
    if bNothing:
        print(repo.git.status())   # 返回通常的status几句信息 

def mergeMainBranch():
    print('1')
 
def pullAll(url,path,branch_name,csvDataList):
    repo = Repo(path)
    remote = repo.remote()
    for submodule in repo.submodules: 
        submodule.update(init=True,recursive=True)
        subrepo = submodule.module()
        row = { keyHeaders[0]: changePath(subrepo.working_dir),
            keyHeaders[1]: replaceRightFileName(subrepo.working_dir),
            keyHeaders[2]: 0,
            keyHeaders[3]: submodule.url,
            keyHeaders[4]: changePath(subrepo.working_dir),
            keyHeaders[5]: submodule.branch_name}
        csvDataList.append(row)
        submodule.module().remote().fetch()
        try:
            subrepo.remote().pull()
            print("子模块更新完毕" + subrepo.working_dir)
        except GitCommandError as e:
            printErr(e)
            openFiles(subrepo.working_dir)
            batStr = '"TortoiseGitProc.exe" /command:resolve /path:' + subrepo.working_dir +' /closeonend:3'
            print(batStr)
            os.system(batStr)

    remote.fetch()
    try:
        remote.pull()
        print("主模块更新完毕" + path)
    except GitCommandError as e:
        printErr(e)
        openFiles(path)

def mergeAll(url,path,branch_name,csvDataList):    
    # repo.remote().fetch()
    # remoteMaster = repo.git.branch('-r')['origin/master'] 
    # repo.index.merge_tree(remoteMaster)
 
    repo = Repo(path)
    remote = repo.remote()
    remote.fetch()

    for submodule in repo.submodules: 
        submodule.update(init=True,recursive=True)
        subrepo = submodule.module()
        row = { keyHeaders[0]: changePath(subrepo.working_dir),
            keyHeaders[1]: replaceRightFileName(subrepo.working_dir),
            keyHeaders[2]: 0,
            keyHeaders[3]: submodule.url,
            keyHeaders[4]: changePath(subrepo.working_dir),
            keyHeaders[5]: submodule.branch_name}
        csvDataList.append(row)
        submodule.module().remote().fetch()
        if isWin():
            batStr = '"TortoiseGitProc.exe" /command:merge remotes/origin/'+ submodule.branch_name + ' /path:' + repo.working_dir +' /closeonend:3'
            print(batStr)
            os.system(batStr)
        elif isMac():
            # master = repo.heads.master
            # other = repo.create_head('other', 'HEAD^')
            # other.checkout()
            # repo.index.merge_tree(master)
            # repo.index.commit('Merge from master to other')
            # current = subrepo.active_branch
            # t = subrepo.branches
            # #current = repo.branches ['feature'] 
            # master = subrepo.branches ['Branch_master'] 
            # base = subrepo.merge_base（current，master）
            # subrepo.index.merge_tree（master，base = base ）
            # remoteBranch = subrepo.git.branch('-r')['origin/' + submodule.branch_name] 
            # subrepo.index.merge_tree(remoteBranch)
            print(isMac)
    t = repo.branches[0]
    t = repo.git.branch('-r')
    t3 = repo.heads[0]
    
    git = repo.git
    git.status()
    git.checkout('HEAD', b="my_new_branch")
    git.branch('another-new-one')
    git.branch('-D', 'another-new-one')

    master = repo.heads.master
    other = repo.create_head('other', 'HEAD^')
    other.checkout()
    repo.index.merge_tree(master)
    repo.index.commit('Merge from master to other')
    remoteBranch = repo.git.branch('-r')['origin/' + branch_name] 
    repo.index.merge_tree(remoteBranch)


def revertAll(url,path,branch_name,csvDataList):
    repo = Repo(path)
    remote = repo.remote()
    for submodule in repo.submodules: 
        submodule.update(init=True,recursive=True)
        subrepo = submodule.module()
        row = { keyHeaders[0]: changePath(subrepo.working_dir),
            keyHeaders[1]: replaceRightFileName(subrepo.working_dir),
            keyHeaders[2]: 0,
            keyHeaders[3]: submodule.url,
            keyHeaders[4]: changePath(subrepo.working_dir),
            keyHeaders[5]: submodule.branch_name}
        csvDataList.append(row)
        submodule.module().remote().fetch()
        submodule.module().remote().pull()

    remote.fetch()
    remote.pull()
 
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
     
    #repo.merge_base(list1[3])
    #repo.index.merge_tree(list1[3])
    batStr = '"TortoiseGitProc.exe" /command:merge remotes/origin/master /path:' + repo.working_dir +' /closeonend:3'
    print(batStr)
    os.system(batStr)
    print(repo.git.status())   # 返回通常的status几句信息  
    print(repo.is_dirty())    # 返回是否有改动（包括未add和未commit的）
    
    
    # try:
    #     remote.pull()
    # except git.GitCommandError as exception:
    #     print(exception)
    #     if exception.stdout:
    #         print('!! stdout was:')
    #         print(exception.stdout)
    #     if exception.stderr:
    #         print('!! stderr was:')
    #         print(exception.stderr)

    #获取本地分支
    print([str(b) for b in repo.branches])
    #获取远端分支
    print(repo.git.branch('-r'))
    print(repo.git.branch())
    for ref in repo.git.branch('-r').split('\n'):
        print(ref)
    
    for submodule in repo.submodules: 
        submodule.update(init=True,recursive=True)
        subrepo = submodule.module()
        
        print(subrepo.working_dir)
        submodule.module().remote().pull()
    
    
    print(repo.git.status())   # 返回通常的status几句信息
    print(repo.is_dirty())    # 返回是否有改动（包括未add和未commit的）

    # 添加文件 可以是单个文件名，也可以是`[ ]`数组，还可以是`.`代表全部
    #print(repo.git.add( '文件名' ))
    #还原合并
    #git.exe reset --merge

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
        

# 安装预备软件
#prepareGitPython(platformName)
curFileList = os.path.split(os.path.realpath(__file__))
pyFiles = curFileList[0]
pyFiles = changePath(pyFiles)



configPath = pyFiles + "/config"
configName = 'cfg.csv' # 后缀名随便改

# configFilePath = configPath + '/' + configName
keyHeaders = ['ProjectPath','ProjectName','isMain','Url','FilePath','Branch']


 # 输入参数
# gitUrl = 'https://gitlab.skyunion.net/hanlinhe/tfather.git'
# gitProjectName = 'test'
# gitFilePath = pyFiles[: - 26] + '/' + gitProjectName
# gitBranch = 'master'

# iniCsvCfgKey(configPath,'inputCfg.csv',['Key','Value'])
# writeCsvByDict(configPath + '/' + 'inputCfg.csv',['Key','Value'],
#                                                  [{'Key':'gitFilePath','Value':gitFilePath},
#                                                   {'Key':'gitUrl','Value':gitUrl},
#                                                   {'Key':'gitProjectName','Value':gitProjectName},
#                                                   {'Key':'gitBranch','Value':gitBranch},
#                                                  ])

qhCfgName  = 'inputCfg.csv'
inpuDataList = readConfig(configPath,qhCfgName,'Key') 
gitUrl = inpuDataList['gitUrl']['Value']
gitProjectName = inpuDataList['gitProjectName']['Value']
gitFilePath = inpuDataList['gitFilePath']['Value']
gitBranch = inpuDataList['gitBranch']['Value'] 

#removeFiles(gitFilePath)
#removeFiles(configPath)

csvDataList = [] 
row = { keyHeaders[0]: gitFilePath,
        keyHeaders[1]: replaceRightFileName(gitFilePath),
        keyHeaders[2]: 1,
        keyHeaders[3]: gitUrl,
        keyHeaders[4]: gitFilePath,
        keyHeaders[5]: gitBranch}
csvDataList.append(row)

if IsFirstCheckOut(gitFilePath): 
    initModule(gitUrl,gitFilePath,gitBranch,csvDataList)
    iniCsvCfgKey(configPath,configName,keyHeaders)      
else:
    updateModule(gitUrl,gitFilePath,gitBranch,csvDataList)

cfgList = readConfig(configPath,configName,'ProjectPath') 
writeCsvByDict(configPath + '/' + configName,keyHeaders,csvDataList)

#inputCfgList = readConfig(configPath,configName) 
#commitAll(gitFilePath)  #test ok

#pullAll(gitUrl,gitFilePath,gitBranch,csvDataList) test ok


if bError == True:
    os.system("pause")
#mergeAll(gitUrl,gitFilePath,gitBranch,csvDataList)

#_subModuleList = readSubModuleCfg(gitFiles + "/.gitmodules")

#updateSubModule(_subModuleList)






# 判断分支是否存在
# does_exist = True
# try:
#     repo.git.checkout('branch_name')
# except repo.exc.GitCommandError:
#     does_exist = False

# print(does_exist)


#     
