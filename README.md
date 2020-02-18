# 2020-Scouting-App

### Required Packages and Software
- [NPM](https://www.npmjs.com/get-npm)
- [Python3](https://www.python.org/downloads/)
- A CLI tool such as [GitBash](https://git-scm.com/downloads), Bash, WSL etc
- Virtualenv (ubuntu install ```sudo apt-get install virtualenv```)

### Getting Started
After cloning the repo, you'll need to do the following to build the individual technologies we're using.
1. In the root directory of the repository run the following to instantiate the Python environment and install Django:
```
virtualenv -p python3 env
source env/bin/activate
pip3 install django djangorestframework
```
2. Navigate to ./frontend/front-end and run ```npm install``` (you may need to elevate permissions with to run this command e.g. ```sudo npm install```)

3. Navigate to ./backend/scoutingAppBackend and run ```python3 manage.py migrate``` to instantiate the sqlite database

4. In the same directory as step 3 run ``` python3 manage.py createsuperuser``` and follow the prompts to create an admin user for yourself in the django database


### Running the applications
1. Open two terminals (gitbash, bash, etc) in one of the two run ```source env/bin/activate``` from the root of the project to enter your python environment

2. navigate to ./backend/scoutingAppBackend with the terminal running your python environment and run ``` python3 manage.py runserver``` to start the django dev server

3. in the other terminal navigate to ./frontend/front-end and run ``` npm start``` to start the React.js dev server.

### Opening the development sites
- [React.js](http://localhost:3000)
- [Django Framework](http://localhost:8000)
- [Django Admin Panel](http://localhost:8000/admin)