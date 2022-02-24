<h2>Django-Ecomm</h2>

<h3>About the Project</h3>
An e-commerce website that lets the user browse through various products of a small enterprise. The idea is to build a catalouge website which will later be turned into an online shopping store.<br>
Currently it has the below features:
<ol>
  <li>Category wise product display
  <li>Sign In / Registration
  <li>Add to cart
  <li>Separate Contact Us and About Us Pages 
</ol>

<h3>Features to be added later:</h3>
<ol>
  <li>Payment Gateway 
  <li>Integrate a basic chatbot
</ol>

<h3>Django app building Steps:</h3>

| Description                          | Command                                 |
|:-------------:                       | :-----:                                 |
| Setup a virtual env                  | python -m venv env                      |
| Activate the virtual environment     | source env/bin/activate                 |
| Install Django                       | python -m pip install django            |
| Start Project                        | django-admin startproject <projname>    |
| Start a Django app                   | python manage.py startapp <appname>     |
| Make migrations                      | python manage.py makemigrations         |
| Apply migrations                     | python manage.py migrate                |
| Run Server                           | python manage.py runserver              |
| Pin your dependencies                | python -m pip freeze > requirements.txt |

<h3>Built With:</h3>
<ul>
  <li>Python
  <li>Django
  <li>HTML
  <li>CSS
  <li>Bootstrap
  <li>SQLite
</ul>

<h3>Steps to execute the app:</h3>
<ul>
  <li>Make a virtual environment using "conda create -n envname python=3.6 pip"
  <li>source activate envname (for mac/linux) | activate envname (for windows)
  <li>Download or clone this repo by git clone https://github.com/pranalibose/Django-Ecomm.git
  <li>pip install -r requirements.txt
  <li>Run the app using python `python manage.py runserver`
<ul>
