<h1 align=center>GetFit</h1> 

<h2 align=center>Introduction</h2> 

<p align=center>GetFit is a website dedicated to sharing, creating and interacting with workout routines or daily routines like eating for fat loss, build muscle and over all staying active and healthy . Whether you are a beginner, intermediate or an advance gym "rat" looking to share your "bro science" with less experienced lifters out there, or are looking for something different to add to your workout routine or even daily eating habits, GetFit has got you covered! <br><br>Browse through the website for a bit of inspiration, tips and tricks or if you are a veteran lifter, share your thoughts and opinion with others to help get them in the best shape of their lifes!</br><br> Users have the ability to read about workout routines and eating habits registered users can create, update and delete comments on and like the admins workouts and daily routines.SuperUser is able to approve, edit and delete workouts from the website itself and also via the admin panel.</br><br>GetFit has been built using the Django framework in Python, HTML and CSS, and provides user authentication and full CRUD functionality for workout routines and also user can add goals in the users dashboard.</p>

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
* I can click on a workout rotine to see the exercise and number of reps for differnt fitness goals.
* I can navigate easily around the site to find what I am looking for.


<strong>As a Registered Site User:</strong>

* I can register for an account to enable me to utilise the functionality available for registered users.
* I can create and share my own tips for workout routines in the comments section for others users to view.
* I can edit my comments.
* I can comment on the  Superusers workouts to interact with the content probably have questions and tips.
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


### Features planned

* Intuitive and simple design
* Visually appealing site 
* Intuitive navigation across all pages
* Role-based navigation for different users 
* Workouts routines   - Registered users can create, read, update and delete their Goals in the dashboard
* Users can create goals into their dashboard they can edit update and delete them 
* Comments & Likes - Registered Users can comment and like 
* User Sign Up and Log in/Out

## The Structure Plane
<hr>

## Functional Scope

### Flowchart

![GetFit Flowchart]()


## Database Schema

Two custom models were created for the website, Routines and Comments and Django AllAuth was utilised for user authentication.  The below ERD was created using [DrawSQL](https://drawsql.app/home) although limitations of the app meant that textarea and Cloudinary fields were not available to use.

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

### Imagery

For the landing page banner I used an image sourced from [Unsplash](unsplash.com) of a barbell and a slogan that I modified in photoshop.  It is grey coloured and gives the impression of a hardcore raw type of gym content. 

![Background Image]()

I also sourced an image from [Pexels](pexels.com) to use as a placeholder image if the user does not have their own image to upload when creating a workout routine.  This image was a guy lifting a barbell.

## Features

### Navigation Bar

I used the navbar from the Codestar tutorial which is the Bootstrap regular navbar without the search option

There are two role-based versions of the navigation bar depending on the user:

* Navbar 1 - General users


This navbar has a logo that shows a kettlebell and a bodybuilder gives the users the option to visit the homepage, log in or register.  There is also a quote to the left hand side of the screen .  All users have access to the Home Page and other posts posted by the Admin


### Footer

The footer is borrowed again from the codestar walkthru kept simple and clean incorporating social media links to encourage users to visit other social media sites related to the main web site.

### Other Features

* Home page - This has a banner-image, title and slogan, brief description of the website and a call to action - Sign Up or Log In if not already logged in    Underneath the hero image, the latest six workouts will be displayed as workout cards. 
* Add Workout/Routine - Uses summernote to enable basic styling, including bold and underlined text 
* My Re - Users are able to see a paginated list of the recipes they have added in with the most recently added recipes showing at the beginning of the list.  Buttons are included on the recipe cards here so the user can edit or delete the recipes as they see fit.  Pressing the delete button here take the user to a confirmation page to ensure they really want to delete the recipe before proceeding to prevent recipes from being accidentally deleted.
* Log in / Sign up / Log out - Django AllAuth has been utilised to allow users to securely log into the the website and gain access to functionality only available to registered users.
* Recipe Search - Users are able to search for recipes using a keyword.   The Recipe database will be searched against the Title, Description and Ingredients for each recipe.
* Recipe Cards - All recipes appear on the site as recipe cards, and when clicked into will link to a recipe detail page.  The Recipe cards summarise the recipe with the Recipe Name, Recipe Image, Author, Date Added, Number of Likes and a brief description of the recipe.
* Recipe Detail - When a recipe card is clicked this opens the recipe detail page which shows all of the information included on the recipe card and additionally the ingredients, method, comments and a comments box which can be used if the user is logged in.


### Future Features/Development

* Better functionality and use of Django AllAuth.  I would like to implement more features of AllAuth in the future, including the ability to change the password or reset the password if forgotten.  I would also like to implement email verification and confirmation.

* I would like to add the ability for the super user to approve comments through the website rather than just the admin panel.  Unfortunately, this was out of scope for this sprint. 

* I would like to include JavaScript so that the like button toggles on and off without the page being refreshed each time.  This was out of scope for this project.
