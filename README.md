# CarSelling APP
  

# running the app on developement server :

**first setup email server :** <br />

  - just uncomment this information on settings.py and add your **EMAIL_HOST_USER** , **DEFAULT_FROM_EMAIL**  and **EMAIL_HOST_PASSWORD** for email notification<br /><br />
    DEFAULT_TO_EMAIL = ['mike@example.org']\
    DEFAULT_FROM_EMAIL = '<paste your gmail account here>'\
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'\
    EMAIL_HOST = 'smtp.gmail.com'\
    EMAIL_HOST_USER = '<paste your gmail account here>'\
    EMAIL_HOST_PASSWORD = '<paste Google password or app password here>'\
    EMAIL_PORT = 587\
    EMAIL_USE_TLS = True
  </br>
  
**Enable less secure apps to access your gmail account**</br>
    - you need to enable your google account to allow this app(CarSelling) to send email using your gmail account   </br>
       - go to : https://myaccount.google.com/  </br>
       - click Security  </br>
       - under less secure app access  </br>
       - switch the allow less secure apps to ON  </br>
  
  
  
**Running the app on developement server :**<br />
    - cd to the root directory of the folder :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cd:\<other>\<path>\carselling-main <br />
    - activate the virutal env :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;env\Scripts\activate(Windows) or source venv/bin/activate(Linux/Mac) <br />
    - run the development server :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python carselling/manage.py runserver <br />
    - access the app on your browser :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://127.0.0.1:8000/cars/ <br />
