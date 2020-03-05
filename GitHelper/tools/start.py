import os
print("--------安装GitPythonGitPython-----------")
os.system("pip install GitPython")
os.system("-----------------------------")
os.system("pause")


#!/usr/bin/env python3

import os
import sys
import platform

#from git import Repo
#curl https://bootstrap.pypa.io/get-pip.py | python3

os.system("pip3 install GitPython") 
os.system("pip install GitPython") 
#os.system("pip3 --version")
#print(sys.platform)
#print(platform.system())
print("11111")
print(os.getcwd())
print(sys.path[0])
print(__file__)
print(os.path.abspath(__file__))
print(os.path.realpath(__file__))
print(os.path.split(os.path.realpath(__file__)))

from git.repo import Repo
from git.repo.fun import is_git_dir
Repo.init('/data/test2') # 创建一个git文件夹
# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo(self.rorepo.working_tree_dir)
assert not repo.bare


# 选择已有仓库
#repo = git.Repo('https://github.com/Redemptionme/TestSokect.git') 
 
# 在文件夹里新建一个仓库，如果已存在git仓库也不报错不覆盖没问题
#repo = git.Repo.init(path='文件夹地址')
 
# 克隆仓库
#repo = git.Repo.clone_from(url='git@github.com:USER/REPO.git', to_path='../new')

print("111111")
