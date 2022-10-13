# PBP Assignment

Platform-Based Programming (CSGE602022) - Organized by the Faculty of Computer Science Universitas Indonesia, Odd Semester 2022/2023

## Application
https://asgmt2-django-mvt.herokuapp.com/todolist/ajax

# Assignment 6
### Describe the difference between asynchronous programming with synchronous programming.
1. Asynchronous is multi-thread, allowing operations or programs to run in parallel. Synchronous is single-thread, allowing only one operation to run at a time.
2. Asynchronous is non-blocking, which means it can send multiple requests to a server simultaneously. Synchronous is blocking, can only send a request one at a time and will wait for a response to that request.
3. Asynchronous allows operations to be run independently, without waiting for the completion of previous operations, excluding those that have dependencies on other operations. Synchronous programming only lets operations start after the previous ones have been completed.
4. Asynchronous programs can produce larger throughput than synchronous ones since multiple operations can run at the same time

### When Implementing Javascript and AJAX, there is an application in the paradigms of Event-Driven Programming. Describe the reasoning for those paradigms and state some examples of its application.
In computer programming, event-driven programming is a programming paradigm in which the flow of the program is determined by events such as user actions (mouse clicks, key presses), sensor outputs, or message passing from other programs or operation threads. This paradigm is applied when implementing Javascript, especially with AJAX, where we want to provide functionalities when users interact with elements in our page. A few examples of this can be seen in this application, implemented with JS and JQuery functions that utilize AJAX, such as, buttons to update and delete the tasks when clicked, modal that reset everytime it is closed, and a form that creates a new object and reloads the page partially when submitted to show the new list of tasks.

### Describe the implementation of asynchronous programming in AJAX.
1. Some elements in the HTML act as certain events' handler that will call a JS function
2. Said function will send a request to a view function to fetch or send data or execute some operations without directing to another new page or reloading the page.
3. The server receives or returns the data sent/requested by the view function
4. The JS function, if it requires the data from the view, will receive it in a certain form, mainly JSON, that is parsed in the view
5. The function can execute the next part that can include processing the received the data, executing the next commands, or call another function.
6. These operations is executed based on their functionalities and will be run without the need to reload the page

### Explain how you would implement the checklist above.
I start with copying the current todolist page, including its html template, view function, and routing, and moodifying it to show a page in `todolist/ajax`. Then I addded JS functions inside the template to show the todolist called `refreshTodolist` with the implementation of AJAX in the Javascript code. I added a JS function and a view function to get the data in JSON format and a routing to this function. The previously said JS function will fetch the data with this view function and will process the html to show the list of tasks. I added this function's call at the end so that it will be called when the page is loaded the first time. Both are created following the example in the template of the fifth tutorial.
I modified the buttons in the cards to call new JS functions that will asynchronously update and delete the task objects. I needed to create a new view function to do this and routings for each function. When the buttons are clicked, the respective JS function will be called, which will call the view function to update or delete the task object and then call the JS function `refreshTodolist` to display the newly updated tasks
I then added a modal from a template in the internet and modified it to contain my form to create a new task. I created a view function following the example from the given template for the fifth tutorial and a JS function in the html. When the form is submitted, the JS function will be called, which will send the POST request to the view function. The view function will get the input from the form, create the new Task object, and save it to the database. The JS function will then call `refreshTodolist` to display the new task
Lastly, I added a JQuery function that will be called everytime the modal is closed. This function will reset the input fields in the form everytime the form is submitted or closed.

## References
https://www.mendix.com/blog/asynchronous-vs-synchronous-programming/

<br>
<br>
