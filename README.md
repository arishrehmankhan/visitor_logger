[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# Visitor Logger

## About Repo
Contains the code of screening task of FOSSEE Summer Fellowship 2020 - Spoken Tutorial Event Logs and Analytics System - Create a Spoken Tutorial Analytics System for capturing and visualizing log events (https://spoken-tutorial.org/stfellowship2020/analyticssystem/)

## About my project
This project consists of two webpages (exclusive 'admin' pages) - '/homepage' and '/dashboard'.
Each time a user visits '/homepage', the request (log) is saved in the database using a django middleware.
The log which is saved contains data such as :
```
"path_info": "/homepage/",
"browser_info": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
"request_data": "{}",
"method": "GET",
"event_name": "GET /homepage/",
"visited_by": "arish",
"location_city": "Lucknow",
"location_region": "Uttar Pradesh",
"location_country": "India",
"ip_address": "202.41.10.64",
"timestamp": "2020-03-01T22:00:05"
```
The analytics of logs are displayed on '/dashboard' page.

## Home page looks like this
![Homepage](/homepage.png)

## Dashboard page looks like this
![Dashboard](/dashboard.png)

## Setting up the project
* Create a virtual environment in recently created directory and activate it:
```
python3 -m venv env
source env/bin/activate ( for linux ) or
source env/Scripts/activate ( for windows )
```

* Clone the repository and enter to the repository:
```
git clone https://github.com/arishrehmankhan/visitor_logger.git
cd visitor_logger
```

* Next, install the dependencies using pip:
```
pip install -r requirements.txt 
```
* Once the dependencies is installed, migrate your database.
```
python3 manage.py migrate
python3 manage.py makemigrations
```

* Then create a superuser account for Django:
```
python manage.py createsuperuser
```

* Finally, you’re ready to start the development server:
```
python manage.py runserver
```
Visit [localhost:8000](http://127.0.0.1:8000/) in your browser to see the project.

## More
If you face any problem regarding the steps described above or any other problem, you can contact me at arish.rehman.khan@gmail.com
