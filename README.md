### FOTE

Django app to upload contributions to charity in return for an FOTE download link

After cloning, To set up for development using python 3 (assuming virtualenv is installed):

1. create a virtual environment folder in the project root
`$ virtualenv venv-fote -p python3`
2. pip install requirements to get django2.0 and other packages
`$ pip install -r requirements.txt`
3. use manage.py to build the db (currently just creates a sqlite3 db in the project root)
`$ ./manage.py migrate`
4. create a superuser to access the admin site
`$ ./manage.py createsuperuser`
5. boot the server and login to the admin site... navigate to localhost:8000/admin

In the admin site you can add a test user image submission using the form and view it. The image gets stored in the root media folder for now. Note that if the user is deleted from the database, the image is not deleted fromt he media folder (for now)

We can do all feature branching off of the development and merge into master for deployment

#### TODO

1. hook up the client facing submission form logic
2. see about setting up the admin system with third party mailing list API
3. configure admin mail account in general and email forms/templates that will get sent out
5. All the cool front end design things!
6. Modifying look and layout of admin page as much as possible (?)
7. Look into setting up eventual third party mp3 download hosting
8. Security and unitests
