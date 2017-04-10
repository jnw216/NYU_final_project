# NYU_final_project


# GIT Commands
``` bash

git checkout <branch>
git add <foo> <bar>
git commit -m "message"
git push origin master


```



# For Development

``` bash

setup_dev_environment () {
    #sudo apt install virtualenv postgresql
    #virtualenv dev  #from home directory
    sudo apt install python3.5 python3-pip python3-venv postgresql git
    cd ~
    python3 -m venv dev  #from home directory
    cd -
    activate_dev
}

remove_dev_environment () { # remove just in case
    rm -r ~/dev
}

activate_dev () {
    source ~/dev/bin/activate # creates function in environment called "deactivate"
}

pip_install_requirements () {
    git_clone_project
    pip3 install -r ~/NYU_final_project/project/requirements.txt
}

git_clone_project () {
    cd ~
    git clone https://github.com/jnw216/NYU_final_project.git
    cd -
}

git_pull_project () {
    cd ~/NYU_final_project
    git pull # does git fetch followed by git merge (see docs)
    cd -
}

migrate_db () {
    python manager.py db init
    python manager.py db migrate
    python manager.py db upgrade
}

launch_app () {
    activate_dev
    cd ~/NYU_final_project/project
    python run_server.py
}

```
