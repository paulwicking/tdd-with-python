Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace USERNAME with actual user name
* replace SITENAME with name of site, e.g. staging.mysite.com

## Systemd service

* see gunicorn-systemd.template.service
* replace USERNAME with actual user name
* replace SITENAME with name of site, e.g. staging.mysite.com

## Directory structure
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
	├── database
	├── source
	├── static
	└── virtualenv

