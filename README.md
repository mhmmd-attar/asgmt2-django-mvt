# PBP Assignment

Platform-Based Programming (CSGE602022) - Organized by the Faculty of Computer Science Universitas Indonesia, Odd Semester 2022/2023

## Application
https://asgmt2-django-mvt.herokuapp.com/todolist/

# Assignment 5
### What is the difference between Inline, Internal, and External CSS? What are the advantages and disadvantages of each style?
- Inline CSS is applied in each HTML element with the style attribute, internal is applied inside the HTML document inside the style tag, and external is created in a new .css file and referenced in the head of the HTML document.
- Inline CSS can be applied to specific elements without affecting other elements with the same selectors. Applying inline CSS also doesn't require us to define classes or id to the HTML elements. But if we want to apply the same CSS to a bunch of HTML elements, inline CSS is not recommended as you will need to apply it repetitively for each one.
- Internal CSS is applied using selectors inside the HTML document, using the `<style>` tag. With selectors, you can apply the same CSS style to elements with the type, id, or class. You can also apply the same CSS to multiple selectors each separated by a comma, `.class, #id { ... }`. Using internal CSS avoids us from having to repetitively type our CSS code for each element, and we won't need to upload multiple files to display our page. However, when we have multiple pages in our project, and we want some elements to have the same design and styling, we will need to copy and paste our CSS into each HTML document/template.
- External CSS is useful when we have multiple pages to display. External CSS holds our CSS in one file that can be referenced by multiple HTML documents. This would significantly reduce repetitions in coding CSS for elements with the same styling or general elements with the same CSS properties. We do have to be careful when creating selectors for HTML elements and designing them to not mix up elements and their styles. We also have to make sure that our CSS file is loaded correctly so our desired web pages will be displayed.

### Describe the HTML5 tags that you know.
1. `<!DOCTYPE>` : defines the document type. Typed in the beginning of HTML documents as `<!DOCTYPE html>`
2. `<html>`     : defines the root of an HTML document
3. `<head>`     : contains metadata of the document
4. `<meta>`     : defines metadata in the `<head>` besides metadata with specific tags
5. `<title>`    : defines the title of the HTML document/page
6. `<link>`     : links other resources/files to be used in the document
7. `<script>`   : contains JS scripts for the document
8. `<style>`    : contains CSS styling for the document
9. `<body>`     : defines and contains the document's body
10. `<header>`  : defines the header of the document
11. `<footer>`  : defines the footer of the document
12. `<div>`     : defines a child section
13. `<h_>`      : contains a text formatted as heading, with multiple sizes specified with numbers
14. `<p>`       : contains a text paragraph
15. `<a>`       : defines a hyperlink
16. `<input>`   : defines an input field with different types
17. `<button>`  : defines a button
18. `<table>`   : defines a table
19. `<tr>`      : defines a row in table
20. `<td>`      : defines a table cell that holds data
21. `<th>`      : defines a table cell that acts as the columns' header
etc.

### Describe the types of CSS selectors you know.
1. .class   : To select elements with the class "class"
2. #id      : To select elements with the id "id"
3. *        : To select all elements
4. elements : To select all elements of "<elements>" type
5. :        : To select elements with certain attributes
6. [attr=vl]: To select elements with attribute "attr" that has the value "vl"

### Explain how you would implement the checklist above.
I integrated Bootstrap and Font Awesome in the `<head>` section inside of base.html. I then searched for templates provided for Bootstrap navigation bar and login or sign up pages in the internet. 
I first added a navbar in base.html and modified it. I added a new Django block so that the content of the navbar can be changed for each page. After modifying the navbar in base.html, I also added a footer without defining a block for it since I want the footer to appear the same in every pages. Then I modified the navbar in each pages to contain different elements and links.
I then started working on the login, registration, and create-task pages. In general, I put the main part of my old template, mainly the form, into sections inside the template from the internet. For the login template, I modified the form section to contain inputs for username and password. For the registration template, I changed the form section to contain the UserCreationForm, generated still with `{{ form.as_table }}`. For the create-task template, however, I do not use the generator `{{ form.as_table }}` and generated the form fields manually inside a card.
Then I moved on to create the main page. For this page, I didn't use any template form the internet, but rather combined parts of the other templates. I constructed the task cards on my own.
After that, I tested my pages when it is displayed in different resolutions in my browser. Since bootstrap classes are mostly already responsive, and since most elements response as needed, I didn't apply any @media

<br>
<br>