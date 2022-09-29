# PBP Assignment

Platform-Based Programming (CSGE602022) - Organized by the Faculty of Computer Science Universitas Indonesia, Odd Semester 2022/2023

## Application
https://asgmt2-django-mvt.herokuapp.com/todolist/

# Assignment 4
### What does `{% csrf_token %}` do in the `<form>` element? What happens if there is no such "code snippet" in the `<form>` element?
`{% csrf_token %}` is used as protection againt "Cross Site Request Forgery" attacks. CSRF attacks forces user to execute unwanted actions on the web page and application by exploiting the user's authenticated state to change the user's request to perform actions not intended by the user. csrf_token tag works by generating a token on the server side when rendering the page and cross-checking this token for any requests coming back in. The incoming requests will not be executed if they do not contain the token.

### Can we create the `<form>` element manually (without using a generator like `{{ form.as_table }}`)? Explain generally how to create `<form>` manually
To render form manually in HTML, we use the tag `<form>` and set its `method` attribute with the value of either GET or POST. We can also set its `action` attribute to specify where the data will be sent when the form is submitted, which, when empty or not set, will defaults to the current page URL. Inside the `<form>` tag, we need to have at least one `<input>` tag for a field and another with `type="submit"` as the submit button. We can have more `<input>` for each field in the model class and we can also wrap our input tags with `<table>` and `<tr>` tags to render the form as a table.

### Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.
The `create_task` view function, when accepting a GET request, will return a rendered page of an empty form, rendered with the template containing the form class, to ask the user to create a new task. When the user click the submit button, it sends the data to the same URL, the current page's, and the view function will accept the reqeust. When the request's method is POST, the view function will validate the received form. If it is valid, the view will save the form first without commiting it to the database to save the newly created model object that still has a null value in its `user` attribute into a variable in the view function. Here, `request.user` will be assigned to the object's `user` attribute to store the information of who created the object. Only then the object will be saved to the database. The user will then be redirected to the main page.
In the main page, the view function will filter every model objects in the database that have `user` attribute's value the same as the current user. It will then display the tasks in the main page, rendered in a table 

### Explain how you implement the checklist above.
1. I first created and activated a virtual environment, then I ran `python manage.py startapp todolist` and created a view function and an HTML template to display the main page
2. I added a path for the app in `settings.py` in `project_django`. I created a new file called `urls.py` in `todolist` and added a URL path for the main page
3. Then, I created a model class,`Task`, in `models.py` with 4 attributes. I ran `python manage.py makemigrations` and `python manage.py migrate` to update the change in `models.py`
4. To implement registration and logging in and out for users, I started out by creating view functions for each feature. Then I created routings for each function in `urls.py`. I created HTML templates for the registration page and log in page, and also modified the main page to contain the log out button. I added a decorator function to the main page's view function so users are required to log in. Finally, I added cookies to show the user's last log in time and modified the log out function as well as the main page template.
5. I created a view function and an HTML template, both derived from the register's ones, for the `create-task` page. I added a new file, `forms.py`, and created a form class derived from the `ModelForm` class. I excluded the date and user attribute from the form, set the default value for date to be the current date the model object was created, and modified the `create_task` view function. I modified the function to save the form without committing it first, change the user attribute's value in the view function as `request.user`, the current logged in user, and then save the form.
6. In `todolist`, I added routings for each function in `urls.py`
7. Then, I pushed my work to GitHub and rerun the deployment to Heroku
8. I then created two accounts and three task on each account.

## References
1. https://pbp-fasilkom-ui.github.io/ganjil-2023/en/assignments/tutorial/tutorial-3/
2. https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
3. https://stackoverflow.com/questions/8466768/using-request-user-with-django-modelform
4. https://stackoverflow.com/questions/12848605/django-modelform-what-is-savecommit-false-used-for
5. https://www.educative.io/answers/what-is-a-csrf-token-in-django
6. https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms

## Collaborator
Kaloosh Falito Verrel

<br>
<hr>
