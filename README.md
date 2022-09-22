# PBP Django Project Template

Platform-Based Programming (CSGE602022) - Organized by the Faculty of Computer Science Universitas Indonesia, Odd Semester 2022/2023

## Application
https://asgmt2-django-mvt.herokuapp.com/mywatchlist/

# Assignment 3
### Explain the difference between JSON, XML, and HTML!
HTML is developed based on SGML with less strict rules on how tags are used to display content on webpages. This leniency affects the structure of information in a webpage since it’s become more difficult to maintain it without rules of when and where tags can be used.

This led to the development of XML which focuses on maintaining the structure of information, without worrying about the formatting of the contents displayed. XML maintains the strict rules of SGML for the structure and leaves formatting to HTML. XML would be the format of sending and receiving information that is usually stored somewhere separately and HTML would display the formatted content containing the received information. XML, while used mainly as a format for data interchange, is still a markup language, so it still has the capacity to display the data as readable content, unlike JSON.

JSON is an information/data interchange format that has gained more popularity than XML. JSON is derived from Javascript, which helps in interacting easily with Javascripts used in the webpage or even other programming languages. JSON can hold data objects with types: strings, numbers, Booleans, null, and array, while XML holds data in a string format. JSON doesn’t use tags in its syntax like XML and HTML, and while it can’t produce a readable display, JSON files are easier to read and write.

### Explain why we need the data delivery when implementing on a platform!
Webpages and web applications usually fetch and send data to be displayed, processed, or stored. These data may be stored in databases separate from the application and page source and of course, the user who sent the request from their browser. This is where data delivery is needed. Data delivery provides structures and formatted data which helps other components of the webpage and application to use or display it to the user.

### Explain how do you complete the tasks in this assignment!
1. Since I'm using an already existing Django project repository, I started right away with `python manage.py startapp mywatchlist`. In views.py in the app folder, I created a basic view functions that will return an HTTP response with an html template. I created a folder "templates" and an html file "mywatchlist.html" inside
2. Back to mywatchlist folder, I created urls.py and filled in paths for my app. I also added a path for the app in settings.py in the project folder
3. In models.py, I created a Model class with 5 attributs for objects in my app. Then, I ran `python manage.py makemigrations` and `python manage.py migrate`
4. I then created a new folder "fixtures" and a new file inside, "initial_mywatchlist_data.json". In that file, I added 10 data entries, each for an object having 5 attributes. Then, I ran `python manage.py loaddata initial_mywatchlist_data.json`
5. To show the data in different formats, I created view functions for each format that will return the appropriate response. 
6. Then, I need to add paths in views.py for each data format so the can be accesed through mywatchlist/<data_format>/
7. To deploy the app to Heroku, I added the command `python manage.py loaddata initial_mywatchlist_data.json` in Procfile then I pushed my local repository to GitHub and wait for GitHub to redeploy it to Heroku

### Accessing the three URLs to retrieve all variants of mywatchlist data by using [Postman](https://www.postman.com/) or similar tools (e.g. [HTTPie](https://httpie.io/product), [Insomnia](https://insomnia.rest/)).
#### HTML
![image](https://user-images.githubusercontent.com/108500770/191486231-245249b5-5654-4127-8a28-54041a2050a0.png)
#### XML
![image](https://user-images.githubusercontent.com/108500770/191486315-0df18279-34b6-4237-8093-d76209943003.png)
#### JSON
![image](https://user-images.githubusercontent.com/108500770/191486378-4e891890-a9e3-47cd-9737-d7291a1b822e.png)

## References
https://medium.com/@oazzat19/what-is-the-difference-between-html-vs-xml-vs-json-254864972bbb
<br>
<hr>
