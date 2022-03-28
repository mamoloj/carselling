# CarSelling APP
  

# running the app on developement server :

**first setup email server :** <br />

  - just uncomment this information on settings.py and add your **EMAIL_HOST_USER** and **EMAIL_HOST_PASSWORD** for email notification<br /><br />
    DEFAULT_TO_EMAIL = ['mike@example.org']\
    DEFAULT_FROM_EMAIL = '<paste your gmail account here>'\
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'\
    EMAIL_HOST = 'smtp.gmail.com'\
    EMAIL_HOST_USER = '<paste your gmail account here>'\
    EMAIL_HOST_PASSWORD = '<paste Google password or app password here>'\
    EMAIL_PORT = 587\
    EMAIL_USE_TLS = True
  
**Running the app on developement server :**<br />
    - cd to the root directory of the folder : cd:\<other>\<path>\carselling-main <br />
    - activate the virutal env: env\Scripts\activate(Windows) or source venv/bin/activate(Linux/Mac) <br />
    - run the development server : python carselling/manage.py runserver <br />
    - access the app on your browser : http://127.0.0.1:8000/cars/ <br />
