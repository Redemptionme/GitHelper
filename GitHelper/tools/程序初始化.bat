@echo off
@set GameFolder="./04_FullProject2" 
 
if exist %GameFolder% ( 
	echo !!!download erro , please delete ./04_FullProject
) else (
	git.exe clone --progress --branch feature/demo -v "https://gitlab.skyunion.net/rd3-project-client/04_FullProject.git" "./04_FullProject"
	echo 更新完毕
)


cd ./04_FullProject

git submodule update --progress --init --merge --remote -- "Demo/Demo_FZ/Demo/Assets/Config"
git submodule update --progress --init --merge --remote -- "Demo/Demo_FZ/Demo/Assets/Scripts/Core"
git submodule update --progress --init --merge --remote -- "Demo/Demo_FZ/Demo/Proto"

cd ./Demo/Demo_FZ/Demo/Assets/Config
git checkout -b feature/demo remotes/origin/feature/demo --

cd ../Scripts/Core
git checkout -b feature/demo remotes/origin/feature/demo --

cd ../../../Proto
git checkout -b feature/demo remotes/origin/feature/demo --


pause