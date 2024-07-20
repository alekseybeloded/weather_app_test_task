# Weather app

### This project has implemented the following:

* The application goes to the API at the following link: ```http://api.worldweatheronline.com/premium/v1/weather.ashx```
* Asks the user to type the city
* Output data in a readable format
* When you visit the site again, the weather will be displayed in the city where the user has already looked earlier
* The application is implemented using gunicorn and nginx, all packed in docker containers

## For developers:

### Install locally:


* Clone repo:
```git clone https://github.com/alekseybeloded/weather_app.git```

* Create file **_.env_** with variables:

```env
SECRET_KEY=<django_secret_key>
DEBUG=<False>
ALLOWED_HOSTS=<127.0.0.1>
API_URL=<API_URL>
API_KEY=<API_KEY>
```
* You can also use this project without .env file with default settings

* Install <a href="https://docs.docker.com/engine/install/" class="external-link" style="text-decoration: none" target="_blank"><strong>Docker</strong></a>

* Pull, build and run docker containers:

``` run commands
docker compose pull
docker compose build
docker compose up -d
```

* Follow link <a href="http://127.0.0.1" class="external-link" style="text-decoration: none" target="_blank"><strong>http://127.0.0.1:8000</strong></a>

* If all steps have been implemented, you will see something like this:
<image src="images/homepage.png" style="max-width: 100%; height: auto">


### Deploy

* Rent virtual maschine with static IP / rent domain

* Create ssh

* Connect to server via ssh

* _Optionally (for rented domain) - add public ip to rented domain in domain settings_

* Install docker (follow <a href="https://docs.docker.com/engine/install/" class="external-link" style="text-decoration: none" target="_blank"><strong>instructions</strong></a> _include_ **_postinstall steps_**)

* Create **.env** file:
    * create variables from section **Install locally/Create file**
    * add public ip/host name and version for variables:

```env
ALLOWED_HOSTS=<www.your_domain,your_domain>
CSRF_TRUSTED_ORIGINS=<https://your_domain,https://www.your_domain>
VERSION=<v*.*.*>
DEBUG=False
```

* Create folders for nginx.conf:
``` run
mkdir nginx
mkdir nginx/conf.d
```

* Copy file **weather_app/deploy/nginx/conf.d/nginx.conf** to folder _nginx/conf.d_
* Replace lines where are specified sportinj domain on your domain in **nginx.conf** file

* Copy **docker-compose.yml** from **weather_app/deploy/**:
* Pull and run docker containers:

```run
docker compose pull
docker compose up -d
```

* Check link <a href="#" class="external-link" style="text-decoration: none" target="_blank"><strong>http://your_domain</strong></a>
