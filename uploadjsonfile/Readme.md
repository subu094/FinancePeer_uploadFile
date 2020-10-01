The Application is developed only on Python and Django

Libraries used:
1) import_export
2) for authentication used 2 types
    a) In django template is_authenticated
    b) In the views.py file used a decorator
        from django.contrib.auth.decorators import login_required
        @login_required        
3) Created a resource a file where to save the data in the database using the created model
4) using import-export library the uploaded json file will be read and saved in the database 
    the code is written in views.py file

How to run application
1) get the zip file or pull the code from master in git
2) install all the necessary libraries(import_export,etc)
3) run the server and try to check the working application.
        
