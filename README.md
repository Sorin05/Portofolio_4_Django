<h1 align=center>GetFit</h1> 

<h2 align=center>Introduction</h2> 

<p align=center>GetFit is a website dedicated to sharing, creating and interacting with workout routines or daily routines like eating for fat loss, build muscle and over all staying active and healthy . Whether you are a beginner, intermediate or an advance gym "rat" looking to share your "bro science" with less experienced lifters out there, or are looking for something different to add to your workout routine or even daily eating habits, GetFit has got you covered! <br><br>Browse through the website for a bit of inspiration, tips and tricks or if you are a veteran lifter, share your workouts  with others to help get them in the best shape of their lifes!</br><br> Users have the ability to post workout routines registered users can create, update and delete their own workouts as well as comment on and like other users workouts and daily routines. The site provides role-based permissions and the SuperUser is able to approve, edit and delete recipes from the website itself and also via the admin panel.</br><br>GetFit has been built using the Django framework in Python, HTML and CSS, and provides user authentication and full CRUD functionality for workout routines and also user can add goals in the users dashboard.</p>

[Visit the live site on Heroku]()

![Multi Device Website Mockup Generator Screenshot]() 


## UX - User Experience Design

## The Strategy Plane
<hr>

### Concept

This project has been developed as part of the [Code Institute's](https://codeinstitute.net/) Diploma in Full-Stack Software Development. The aim is to create a full-stack that will demonstrate the skills I have learnt in Python, Django , HTML, CSS

The main aim of the website is to provide a space for those looking to improve their physique and overall mental health.  When logged in, users will be able comment on workouts routines share their experience, like workouts and have full CRUD functionality of their own workouts.  A SuperUser will be able to approve, edit and delete user routines to allow them to manage the content of the site.

The sites target audience is:
* Fitness Enthusiasts and people looking for inspiration for workout routines, .
* People who are looking to get into fitness and have a healthy lifestyle.
* People who are looking to increase their productivty in fitness and day to day life.

### User Stories

<strong>As a General Site User:</strong>

* I can set a goal delete or edit.
* I can view a paginated list of workouts so I can select one to try.
* I can view the comments on workouts so I can see tips and suggestions.
* I can click on a workout rotine to see the ecercise and number of reps for differnt fitness goals.
* I can navigate easily around the site to find what I am looking for.


<strong>As a Registered Site User:</strong>

* I can register for an account to enable me to utilise the functionality available for registered users.
* I can create and share my own tips for workout routines for others users to view.
* I can edit my workouts so that I can keep them up to date and other user can see what bodyparts Im focusing next.
* I can comment on other users workouts to interact with the content probably have questions and tips.
* I can like workouts and share my experience  so I can interact with the content.

<strong>Agile Methodology</strong>

All functionality and development of this project were managed using GitHub Projects Kanban Board which can be found here:

[GetFit Workouts Sharing - USER STORIES]()

## The Scope Plane
<hr>

### Site Goals

* To provide user with a space to search for fitness routines and tips to get in better shape and stay healthy 
* To provide users with a visually pleasing website that is intuitive to use and easy to navigate
* To provide a website where the purpose is immediately clear
* To provide role-based permissions that allows user to create, edit and delete their own workout routines and goals admin to approve, edit and delete workouts.

### Features planned

* Intuitive and simple design
* Visually appealing site 
* Intuitive navigation across all pages
* Role-based navigation for different users 
* Workouts routines   - Registered users can create, read, update and delete their workout routines
* Users can create goals into their dashboard they can edit update and delete them 
* Comments & Likes - Registered Users can comment and like 
* User Sign Up and Log in/Out

## The Structure Plane
<hr>

## Functional Scope

### Flowchart

![GetFit Flowchart]()


## Database Schema

Two custom models were created for the website, Recipes and Comments and Django AllAuth was utilised for user authentication.  The below ERD was created using [DrawSQL](https://drawsql.app/home) although limitations of the app meant that textarea and Cloudinary fields were not available to use.

![Database Schema]()


## The Skeleton Plane

## Wireframes 

I used [Balsamiq](https://balsamiq.cloud/) to create low fidelity wireframes which helped me to stay on track during the development process.

Some modifications were made to the initial design during the development process based on user feedback and continuous testing.

<details>
<summary>Home Page Wireframes for Mobile, Tablet and Desktop</summary>
<br>

![Homepage Wireframes]()
</details>

<br>

<details>
<summary>Alternative Navbar Wireframes for Mobile, Tablet and Desktop</summary>
<br>

![Navbar Wireframes]()
</details>

<br>

<details>
<summary>All Workouts Page Wireframes for Mobile, Tablet and Desktop</summary>
<br>

![All routine Wireframes]())
</details>

<br>

<details>
<summary>Routine Details Wireframes for Mobile, Tablet and Desktop</summary>
<br>

![Routine Detail Wireframes]()
</details>

<br>

<details>
<summary>Add Routine Wireframes for Mobile, Tablet and Desktop</summary>
<br>

![Add Routine Wireframes]()
    
</details>

<br>