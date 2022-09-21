# PBP Django Project Template

Platform-Based Programming (CSGE602022) - Organized by the Faculty of Computer Science Universitas Indonesia, Odd Semester 2022/2023

## Application
https://asgmt2-django-mvt.herokuapp.com/katalog/

# Assignment 2
### Create a diagram containing client request to the Django web application and its response. Also explain the flow of the diagram and how the urls.py, views.py, models.py and HTML files connected each other.

![image](https://user-images.githubusercontent.com/108500770/189872675-b9b2d97c-c239-4640-9644-ab06c2e7f5b5.png)

1. Client puts out a request to the Django web application
2. The URLS component, urls.py, sends out a request object as a function call to the View component according to the path requested
3. The View component will fetch the HTML template for the response that will be shown to the user as a webpage
4. If needed, the View component will also request the model component (models.py) to fetch some data to be shown on the webpage
5. The View component will then return a response in the form of an HTML webpage

### Explain why do we use virtual environments? Let's say, if we do not use the virtual environments, can we still create a Django web application?
Virtual environments allow us to separate our projects into an environment of their own. These virtual environments help manage dependencies by isolating each project from the others. Virtual environments are useful especially when you have multiple projects or ones that will be maintained for a long time. Without this separation of concern principle, when you update a dependency on your system, some of your projects that utilize that dependency may not be compatible with the newer version, making them unrunnable.

### Explain how did you implement the steps on point 1 to point 4 above.
1. In views.py, the function I created accepts a request object as its argument. This function constructs a dictionary that consists of data, including a QuerySet fetched from models.py. This function then returns a function object called render(), with the request object, the HTML template, and the dictionary as its arguments
2. urls.py contains a list of path functions that map the requested path to its appropriate function in views.py
3. The data that has been returned to the function in views.py are used as arguments for the render function. This render function returns an HttpResponse object that contains a string translated by a function in the Django library, render_to_string()
4. Deploying the Django app starts with creating a new app in Heroku. I then created some files, namely Procfile, dpl.yml, and .gitignore, then added some configurations in settings.py. Then, I added two repository secrets that contain my Heroku account's API key and the name of the newly created app in Heroku. After all that, I just had to rerun the deployment of my app on GitHub
<br>
<hr>

## Misc

HTTP Request --------> URLS (urls.py)
                              |
                              V
Model (models.py) <--> View (views.py) ---> HTTP Response (HTML)
                              Ʌ
                              |
                     Template ( .html)