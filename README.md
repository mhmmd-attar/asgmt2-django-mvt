# PBP Django Project Template

Platform-Based Programming (CSGE602022) - Organized by the Faculty of Computer Science Universitas Indonesia, Odd Semester 2022/2023

*Read this in other languages: [Indonesian](README.id.md), [English](README.md)*

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

## Introduction

This repository is a template that is designed to help students who take the Platform-Based Development/Programming Course (CSGE602022) to know the structure of a Django Web application project, including the files and configurations that are important in running the application. You can freely copy the contents of this repository or utilise this repository as a learning material and also as a starting code to build a Django Web application project.

## How to Use

If you want to use the code template in this repository as a starter code for
developing a Django Web application:

1. Open the GitHub page of the code template repository and click "**Use this template**"
   button to make a copy of the repository into your own GitHub account.
2. Clone the new Django template repository from your GitHub account to a
   location in the filesystem of your local development environment by using
   Git:

   ```shell
   git clone <URL to your repository on GitHub> <path in local development environment>
   ```
3. Go to the location where the cloned repository is located in the local
   development environment:

   ```shell
   cd <path to the cloned repository>
   ```
4. Create a Python virtual environment named `env` inside the cloned repository
   by using Python's `venv` module:

   ```shell
   python -m venv env
   ```
5. Activate the virtual environment:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```
6. Verify the virtual environment has been activated by looking at the prompt
   of your shell. Make sure there is a `env` prefix in your shell. For example:

   ```shell
   # Windows using `pwsh` shell
   (env) PS C:\Users\RickeyAstley\my-django-app
   # Linux/Unix, e.g. Ubuntu using `bash` shell
   (env) rickeyastley@ubuntu:~/my-django-app
   ```

   > Note: You can use [Visual Studio Code][] (with Python extension) or [PyCharm][]
   > to open the source code directory that has a virtual environment directory.
   > Both will detect the virtual environment and use the correct Python virtual
   > environment. Furthermore, you can also run your shell directly in both text
   > editor/IDE.
7. Install the dependencies needed to build, test, and run the application:

   ```shell
   pip install -r requirements.txt
   ```
8. Run the Django Web application using local development server:

   ```shell
   python manage.py runserver
   ```
9. Open http://localhost:8000 in your favourite Web browser to see if the Web
   application is running.

## Deployment Example

The code template provided a GitHub workflow to deploy the sample Django Web
application to [Heroku][], which is a Platform-as-a-Service (PaaS) provider
that lets you to build and run a Web application on their infrastructure. You
can read the instructions at [Tutorial 0][] to figure out how to configure the
GitHub Actions to run the provided workflow in your repository.

For reference, the deployed Django Web application example from the original
code template repository can be found at: https://django-pbp-template.herokuapp.com.

## Next Actions

If you have successfully created your own repository and set up the Django Web
application project, you can start working on the weekly tutorials and assignments
related to Django Web application development. 

If you found any issues or have ideas to improve the code template, feel free
to discuss your proposal via the [issue tracker](https://github.com/pbp-fasilkom-ui/django-pbp-template/issues)
and create a Pull Request (PR) containing your changes to the code template.

## Credits

This template was based on [PBP Odd Term 2021/2022](https://gitlab.com/PBP-2021/pbp-lab) written by 2021 Platform Based Programming Teaching Team ([@prakashdivyy](https://gitlab.com/prakashdivyy)) and [django-template-heroku](https://github.com/laymonage/django-template-heroku) written by [@laymonage, et al.](https://github.com/laymonage). This template is designed in such a way so that students can use this template as a starter and reference in doing assignments and their work.

[Heroku]: https://www.heroku.com/
[Tutorial 0]: https://pbp-fasilkom-ui.github.io/ganjil-2023/en/assignments/tutorial/tutorial-0
[Visual Studio Code]: https://code.visualstudio.com/
[PyCharm]: https://www.jetbrains.com/pycharm/

## Misc

HTTP Request --------> URLS (urls.py)
                              |
                              V
Model (models.py) <--> View (views.py) ---> HTTP Response (HTML)
                              Ʌ
                              |
                     Template ( .html)

