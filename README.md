# **Sam's Bistro**

The Sam's Bistro app, "Boky-pp5" was designed to make dining experiences more efficient and enjoyable. It offers users the ability to book or cancel table reservations with ease while checking real-time availability. The app also allows for rescheduling reservations, ensuring flexibility for both diners and restaurant staff.

Beyond table bookings, It provides features for exploring upcoming events at the restaurant and sharing them with others, fostering engagement and community and vise versa where the user can share their experience. With its user-friendly interface, Boky-pp5 streamlines operations for Sam's Bistro and enhances convenience for customers, creating a seamless dining journey.

The backend is implemented using Django Rest Framework API. It is designed to support both web and future mobile applications providing robust and secure APIs for the frontend application, ensuring seamless integration and future scalability.


LIVE LINK : https://boky-pp4-d51abfaa1de4.herokuapp.com/


## Table of contents

- [Project](#project)
- [Planning](#planning)
  - [Project Overview](#project-overview)
  - [Objectives](#objectives)
  - [Timeline](#timeline)
- [Frameworks, Libraries, and Dependencies](#frameworks-libraries-and-dependencies)
  - [Django Framework and Extensions](#django-framework-and-extensions)
  - [Database Management](#database-management)
  - [Authentication and Security](#authentication-and-security)
  - [Storage and Image Handling](#storage-and-image-handling)
  - [Application Server](#application-server)
  - [Utility Libraries](#utility-libraries)
- [Testing and Validating](#testing-and-validating)
  - [Manual Testing](#manual-testing)
  - [Browser Testing](#browser-testing)
  - [Bugs](#bugs)
- [Validation](#validation)
  - [Lighthouse](#lighthouse)
- [Deployment](#deployment)
  - [1. GitHub](#1-github)
  - [2. Gitpod](#2-gitpod)
  - [3. Heroku](#3-heroku)
  - [4. ElephantSQL](#4-elephantsql)
  - [5. Cloudinary](#5-cloudinary)
  - [Deployment Steps](#deployment-steps)
- [Cloning and Forking](#cloning-and-forking)
  - [Cloning the Repository](#cloning-the-repository)
  - [Forking the Repository](#forking-the-repository)
  - [Languages](#languages)
  - [Frameworks Libraries Programs](#frameworks-libraries-programs)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
- [Acknowledgements](#acknowledgements)
  - [Inspiration](#inspiration)




# Project 

# Planning

I love hanging out with friends and family to try new reasturant.I also work in service therefore I decided to create a reasturant table booking and where people will be able to share there posts too.

## Project Overview

The reasturant is called Sam's bistro.The project is a platform that includes features like my booking and events.

## Objectives

1.Develop a robust backend API using Django Rest Framework to handle data management and user authentication.
2.Build an intuitive and responsive frontend using bootstrap to provide a creative user experience.
3. Integrate key features such as user profiles, posts, comments, likes, challenges, and daily routines.

## Timeline
Timeline
1.Week 1: Project Setup and Initial Development

- Set up backend and frontend repositories.
- Configure Django Rest Framework for the backend.
- Initialize React project for the frontend.
- Set up initial project structure and environment configurations.

2.Week 2: User Authentication and Profile Management

- Implement user registration, login, and logout functionality.
- Develop user profile creation and editing features.
Ensure secure password handling and authentication processes.

3.Week 3: Core Features Development

- Develop the functionality for creating, editing, and deleting posts.
- Implement comments and likes features for posts.
- Develop daily routines and challenges features, including creation and management.

4.Week 4: Frontend Integration and Styling

- Integrate backend API with the frontend.
- Develop responsive and user-friendly UI components.
- Apply consistent styling using CSS modules or a CSS framework.

5.Week 5: Testing and Debugging

- Conduct thorough testing of all features.
- Fix any bugs or issues identified during testing.
- Perform user acceptance testing (UAT) to ensure the platform meets user needs.

6.Week 6: Deployment and Documentation

- Deploy the backend API to a cloud service (e.g., Heroku, AWS).
- Deploy the frontend application to a hosting service (e.g., Netlify, Vercel).
- Write comprehensive documentation, including setup instructions, API documentation, and user guides.

# Frameworks, Libraries, and Dependencies

The Fit&Fine project leverages a variety of frameworks, libraries, and dependencies to ensure robust functionality and performance. Below is a detailed list of the key components used:

### Django Framework and Extensions

1. **Django** (`Django==3.2.25`):
   - A high-level Python web framework that encourages rapid development and clean, pragmatic design. Django handles much of the complexity of web development, allowing developers to focus on writing their app without needing to reinvent the wheel.

2. **Django REST Framework** (`djangorestframework==3.15.1`):
   - A powerful and flexible toolkit for building Web APIs in Django. It provides various features such as serialization, authentication, and view sets that simplify API development.

3. **Django Allauth** (`django-allauth==0.44.0`):
   - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

4. **Django REST Auth** (`dj-rest-auth==2.1.9`):
   - Provides a set of REST API endpoints for handling user registration and authentication tasks. It’s built on top of Django Allauth and Django REST Framework.

5. **Django Filter** (`django-filter==2.4.0`):
   - Simplifies the process of filtering querysets in Django REST Framework.

6. **Django CORS Headers** (`django-cors-headers==4.3.1`):
   - A Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS).

### Database Management

7. **dj-database-url** (`dj-database-url==0.5.0`):
   - Allows you to utilize the DATABASE_URL environment variable to configure your Django application.

8. **psycopg2** (`psycopg2==2.9.9`):
   - PostgreSQL database adapter for Python.

### Authentication and Security

9. **djangorestframework-simplejwt** (`djangorestframework-simplejwt==4.7.2`):
   - Provides JSON Web Token (JWT) authentication for Django REST Framework.

10. **oauthlib** (`oauthlib==3.2.2`):
    - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python.

11. **requests-oauthlib** (`requests-oauthlib==2.0.0`):
    - OAuthlib support for Python-Requests, the ubiquitous HTTP library for Python.

12. **PyJWT** (`PyJWT==2.8.0`):
    - A Python library which allows you to encode and decode JSON Web Tokens (JWT).

### Storage and Image Handling

13. **Pillow** (`Pillow==8.2.0`):
    - Python Imaging Library (PIL) fork that supports opening, manipulating, and saving many different image file formats.

14. **Cloudinary** (`cloudinary==1.40.0`):
    - A library that integrates your application with the Cloudinary service for managing media assets such as images and videos.

15. **django-cloudinary-storage** (`django-cloudinary-storage==0.3.0`):
    - Facilitates the integration of Django with Cloudinary for storing media files.

### Application Server

16. **Gunicorn** (`gunicorn==22.0.0`):
    - A Python WSGI HTTP Server for UNIX that serves your Django application and allows it to handle multiple requests simultaneously.

### Utility Libraries

17. **asgiref** (`asgiref==3.8.1`):
    - A reference implementation of ASGI, the emerging Python standard for asynchronous web servers and applications.

18. **sqlparse** (`sqlparse==0.5.0`):
    - A non-validating SQL parser for Python.

19. **python3-openid** (`python3-openid==3.2.0`):
    - A set of Python packages to support OpenID authentication.

20. **pytz** (`pytz==2024.1`):
    - World timezone definitions, modern and historical.

This combination of frameworks, libraries, and dependencies ensures that Fit&Fine is robust, scalable, and secure, providing a seamless user experience for managing fitness routines and social interactions.

# Testing and Validating
### Manual Testing

Testing was done throughout the process while developing the project by the use of Django debug pages and printing statements to check that the code functioned accordingly. In addition, thorough testing has been performed and is described below, it contains manual test to check that all user stories and acceptance criteria are met, as well as testing and validating the code with different online tools as presented below.

### Browser Testing
Testing has been carried out on the following browsers:

- Google Chrome
- Firefox
- Safari

The site was constantly tested during the process of creating the site in the Gitpod Environment and the deployed site on Heroku was also tested in terms of user experience. The available functionality and user experience is reflected in the table below.

| Goals and Actions | As a Guest | As a User | Comment |
| -------- | -------- |  -------- | -------- |
| I can use the menu and navigate through the pages   | X | X | Click on items
| I can see events, posts and comments made by users  | X | X | Can only view as guest
| I can see the Home Page   | X | X | Click on items
| I can see the Registration Page  | X |  | Click on items and this disappears from the nav bar once registered
| I can see the Bookings Page |   | X | Need to be authorized to see
| I can see the My Bookings page  |  | X | Need to be authorized to see
| I can see the Sign Up Page | X | X | Click on items
| I can see the Login/Logout Pages | X | X | You see one or the other depending on if you are logged in or logged out
| I can complete the Registration form  | X |  | Click on items
| I can complete the Sign In form  | X | X | Click on items
| I can make a booking for a particular time and date booked |  | X | Need to be authorized to do
| I can delete a particular booking,Post and comment made in the event page |   | X | Need to be authorized to do and be main user
| I can edit a particular booking,Post and comment made in the event page |   | X | Need to be authorized to do and be main user
| I can see if I have made a booking successfully  |   | X | Need to be authorized to do
| I can see if I have already made a booking for a session  |  | X | Need to be authorized to do


### Bugs
- Heruko setup took a while but fixed with the help og a tutor.

## Validation

### Lighthouse

<img src="static/images/readme-images/light house.png" width="350" title="hover text">
  

## Deployment

- The deployment process for Sam's Bistro involves multiple platforms, including GitHub, Gitpod, Heroku,  CI Postgresql, and Cloudinary. Below is a detailed explanation of how each platform fits into the deployment process along with the respective URLs for the platforms and services used in deploying and managing the Fit and Fine DRF API.

### 1. GitHub

- **Purpose:** 
  - Version control and collaboration.

- **Process:**
  - The source code for Sam's Bistro is hosted on GitHub. Developers can collaborate, track changes, and manage different versions of the application.
  - The repository is used as the central hub for the project, where all updates and changes are committed and pushed.

- **URL:**
  - [GitHub Repository](https://github.com)

### 2. Gitpod

- **Purpose:**
  - Online IDE for development.

- **Process:**
  - Gitpod is used for development and testing. It provides a cloud-based development environment that is pre-configured with the necessary tools and dependencies.
  - Developers can open the GitHub repository in Gitpod and start coding immediately without worrying about local setup.

- **URL:**
  - [Gitpod Workspace](https://gitpod.io/)

### 3. Heroku

- **Purpose:**
  - Platform as a Service (PaaS) for hosting the application.

- **Process:**
  - The Bistro application is deployed on Heroku. Heroku manages the server, deployment, and scaling of the application.
  - Continuous deployment is set up from the GitHub repository to Heroku, ensuring that any changes pushed to the main branch are automatically deployed to the live site.

- **URL:**
  - [Heroku Dashboard](https://dashboard.heroku.com/)

- **Setting up on Heroku:**
  1. Create a new app on Heroku.
  2. Connect the Heroku app to the GitHub repository.
  3. Set up Config Vars in Heroku including `DATABASE_URL`, `SECRET_KEY`, `CLOUDINARY_URL`, `ALLOWED_HOST`  and `DISABLE_COLLECTSTATIC=1` (this is temporary and can be removed for the final deployment).
  4. Deploy the main branch using the Heroku dashboard or enable automatic deployments for every push to the main branch.

- **For deployment, Heroku needs two additional files in order to deploy properly:**
    - `requirements.txt`
    - `Procfile`

- You can install this project's requirements (where applicable) using:
  - `pip install -r requirements.txt`

- If you have your own packages that have been installed, then the requirements file needs to be updated using:
  - `pip freeze --local > requirements.txt`

- **The Procfile can be created with the following command:**
  - `echo web: gunicorn app_name.wsgi > Procfile`

- Then add these lines to Procfile

  - `web: gunicorn app_name.wsgi`

  - `release: python manage.py makemigrations && python manage.py migrate`

- Replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located.

### 4.  Code Insistute Postgresql

- **Purpose:**
  - Database as a Service for PostgreSQL.

- **Process:**
  - Code Insistute provided the PostgreSQL database for the application. The database is used to store all application data, including user information, posts, comments, and other relevant data.
  - Heroku is configured to use the postgresql database through environment variables.

To obtain your own PostgreSQL Database from Code insistute you need to be a student and they will provide database linked to your student email, where they will email you database URL.

### 5. Cloudinary

- **Purpose:**
  - Media management and storage.

- **Process:**
  - Cloudinary is used for storing and managing media files, such as images and videos uploaded by users.
  - The application is configured to upload media files directly to Cloudinary, where they are stored and served.

- **URL:**
  - [Cloudinary Dashboard](https://cloudinary.com/users/login)

- **Integration:**
1. Set up a Cloudinary account.
2. Configure the Cloudinary settings in the Django settings file with the API keys provided by Cloudinary.
3. Use Django’s storage backend for Cloudinary to handle media uploads.

### Deployment Steps

1. **Clone the Repository:**
   - Clone the GitHub repository to your local machine or open it in Gitpod for development.

2. **Configure Environment Variables:**
   - Set up the necessary environment variables in your local `.env` file or in the Heroku dashboard. These include database URL (ElephantSQL), Cloudinary API keys, and other sensitive information.

3. **Install Dependencies:**
   - Install the required dependencies using `pip install -r requirements.txt`.

4. **Run Migrations:**
   - Apply database migrations using `python manage.py migrate` to set up the PostgreSQL database schema.

5. **Test the Application:**
   - Run the application locally or in Gitpod to ensure it works as expected.

6. **Deploy to Heroku:**
   - Push the changes to the GitHub repository, which triggers the continuous deployment to Heroku.
   - Ensure that the Heroku app is properly configured with the necessary environment variables and add-ons (such as Postgresql).

7. **Manage Media Files:**
   - Configure Cloudinary in the Django settings and ensure that media files are uploaded and managed correctly.

# Cloning and Forking
### Cloning the Repository

**Local Setup:**
1. Clone the repository: [GitHub repository](https://github.com/Sammy92dec/boky-pp4). 
   - `git clone https://github.com/Sammy92dec/boky-pp4`
2. Navigate into the project directory: `cd boky-pp4`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up local environment variables in a `.env` file.
5. Run migrations: `python manage.py makemigrations`and`python manage.py migrate`
6. Start the development server: `python manage.py runserver`


### Forking the Repository

**For Contributions:**
1. Fork the repository on [GitHub repository](https://github.com/Sammy92dec/boky-pp4).
2. Clone your forked repository to your local machine.
3. Follow the local setup steps as above.
4. Make changes and push them back to your fork.
5. Create a pull request from your fork back to the original repo.

By following these steps and utilizing the aforementioned platforms, the deployment and management of the boky-pp4 application are streamlined and efficient, ensuring a robust and scalable application.

## Languages

- Python
- HTML
- CSS

## Frameworks Libraries Programs

- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [CI-PostgreSQL] was used as the database for this project.
- [Heroku](https://dashboard.heroku.com/login) - was used as the cloud-based platform to deploy the site on.
- [AmIResponsive?](https://ui.dev/amiresponsive) - Used to verify the responsiveness of my website on different devices.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and using lighthouse.
- [Font Awesome](https://fontawesome.com/) - Used for icons in the three-reasons section.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [CI Python Linter](https://pep8ci.herokuapp.com/) - used to validate all the Python code
- [Summernote](https://summernote.org/): A WYSIWYG editor to allow users to edit their posts
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to manage Django Forms
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images
- [Bootstrap v5.3.2](https://getbootstrap.com/docs/5.3/getting-started/introduction/): CSS Framework for developing responsiveness and styling

# Credits

### Code

- [Code Institute](https://codeinstitute.net/), for teaching me the languages needed to create this page.
- [w3schools](https://www.w3schools.com/), for so many helpful pages and tools to support learning the languages.
- [Django](https://docs.djangoproject.com/en/4.0/) and [Bootstrap v5.3.2](https://getbootstrap.com/docs/5.3/getting-started/introduction/) docs, for a lot of helpful information.
- [Stack Overflow](https://stackoverflow.com/), for a lot of help, especially regarding bug fixes.
- [Youtube Tutorial](https://www.youtube.com/@IonaFrisbee/featured), for providing a step by step guide of how to create with django.
- [Chatgpt](https://chatgpt.com/), for alot of advices , especially providing with the texts and prices since I am based in Sweden.

### Media

The following sites were used to gather the photographic media used:
- [Font Awesome](https://fontawesome.com/) Social Media Icons located in the footer.
- [Images](https://media.gettyimages.com) for the huge images added to home page and about page.

# Acknowledgements

- My sister for keeping up with me.
- Thanks to my Code Institute mentors and my fellow students for constantly inspiring me on Slack.

### Inspiration

- This project was inspired by the instruction of the project as an idea from [Code Institude](https://codeinstitute.net/) .Also that I work in the service field that made it interesting to dive in.
