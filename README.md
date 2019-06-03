## Blog

## Name
Andrew Mwangi

## Description
website where you can create and share your opinions and other users can read and comment on them. Users can subscribe to the blog to get the latest updates on articles.

The blog supports comments from readers and blog writers can determine whether to delete the comments or not. Users can also delete blog posts at their discretion.They can also vote onthe blogs.

After the writer has posted a new blog post, subscribers will receive an email notification with a link to the blog post.

## Specifications
Get the specs here

# Set-up and Installation
Clone the Repo

Run the following command on the terminal: git clone https://github.com/ngishjonathan/Personal-Blog.git && cd Personal-Blog

Install Postgres

Create a Virtual Environment
Run the following commands in the same terminal: '''bash

sudo apt-get install python3.6-venv python3.6 -m venv virtual source virtual/bin/activate '''

Install dependancies
Install dependancies that will create an environment for the app to run pip install -r requirements

Prepare environment variables
export DATABASE_URL='postgresql+psycopg2://<your-username>:<your-password>@localhost/blog'
export SECRET_KEY='Your secret key'
export DATABASE_URL_TEST='postgresql+psycopg2://<your-username>:<your-password>@localhost/blogtest'
export MAIL_SERVER='smtp.googlemail.com'
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-email>
export MAIL_PASSWORD=<your-password>
``

Run Database Migrations
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
Running the app in development
In the same terminal type: python3 manage.py server

Open the browser on http://localhost:5000/
## Prerequiites
- Python 3.6
- Ubuntu software


## Known bugs
 the application has no known bugs

## Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- JavaScript
- Heroku
- Postgresql

## Support and contact details
contact me through my email.balozimwash@gmail.com

## License
Copyright (c) license
Andrew Mwangi