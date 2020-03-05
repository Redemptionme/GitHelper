import os
print("install GitPython")
os.system("pip install GitPython")
print("test")
se = input()
print(se)

from git import Repo
os.system("pause")
# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo(self.rorepo.working_tree_dir)
os.system("pause")
# 创建版本库对象
repo = git.Repo(r'D:\workplace\IGG_WORK\Star2\Star2_Code')

print(repo.active_branch)

os.system("pause")