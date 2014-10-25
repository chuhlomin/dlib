readhub
====

## INSTALLATION

### Install pip

Download https://bootstrap.pypa.io/get-pip.py

Run: sudo python get-pip.py

### Install python libs

Run: `sudo pip install django==1.5.8 pyyaml`

### Update DB

Run: `python manage.py syncdb`

### Populate DB

Run: `python manage.py loaddata books.yaml`

### Run server

Run: `python manage.py runserver`

### Install NodeJS

Install nodejs: http://nodejs.org
On Ubuntu additionaly: `sudo ln -s /usr/bin/nodejs /usr/bin/node`

### Install required node-packages

Run: `npm install`

### Install Bower

Run: `sudo npm install -g bower`

### Install Grunt

Run: `sudo npm install -g grunt-cli`

### Download JS-dependencies

Run: `bower install`

### Execute Grunt default task

Run: `grunt`

### Open site

URL: http://127.0.0.1:8000/
