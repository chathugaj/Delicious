# The Dine Restaurant

The Dine Restaurant is restaurant located in Stockholm, Sweden. This website provides a website and a reservation management 
system for the staff to manage the table reservations. It also provides the ability to manage their own reservations.

[Live Link](https://the-dine-restaurant-73de8861d11f.herokuapp.com/)

# User Experience Design
## The Strategy Plane

### Goals
The two main goals of the web application are;
- To provide a mechanism to customers of the restaurant to do the following in convenient manner;
  - Reserve a tables with time slots
  - View, edit or cancel the reservation
- The staff will be able perform
  - Track the spacing and capacity of the restaurant at a given time
  - Track the reservations
  - Update or cancel the reservations if needed

### Agile planning

Agile methodologies were used when developing the project. A kanban board was created all the user stories were grouped
under Epics. Epics were considered as project milestones in the kanban board. When the project is delivered all the 
milestones should be completed. This is reflected by the completion of user stories, under each milestone.
User stories are provided with an acceptance criteria, so that we know if a user story is complete. 
[Link to the board](https://github.com/users/chathugaj/projects/1/views/1)
TODO image

A separate spreadsheet was created to calculate the value of each user story using, value to the customer
and the importance of the feature.
[Link to the spreadsheet](https://docs.google.com/spreadsheets/d/1lVoxuDBHZh942KbaejMWFaZMcZhB6AS9aBnvEZTukfo/edit?usp=sharing)
TODO Add Image

#### Milestones / Epic 
The project has five main Milestones

##### Milestone 1 - Main setup
Main setup contains stories related to initial setup of the project and other setup tasks.
Without some of the core user stories the application development itself cannot be done.
- As a developer I have to create the main layout using HTML, so that the layout can be reused
- As a developer I need to find suitable images so that website has more visual context
- As a developer I need to add CSS styles so that pages look easthetic
- As a developer I need to add Javascript so that page have more dynamic functionality
- As a devleoper I need to setup the project with necesssary dependencies, so that I can develop the core features
- As a developer I need to implement a navbar so that I can enable navigation in my website
- As a developer I need to implement a footer so that I can provide copyrights, social media links
- As a developer I need to implement a contact and Open hours  so that I can provide contact information and information opening hours

##### Milestone 2 - General feature pages
General features that provides better user experience for the users and common error handling.
- As a user I need to see a 404 error page, if the page I'm trying to access is not available
- As a developer I need to implement a 500 for unrecoverable errors in the system, so that users can be instructed how to proceed
- As a developer I want to redirect unauthorized users to 403 page, so that I can secure my view
- As the restaurant owner I want a home page, so that customers can view information about my restaurant
- As the restaurant owner I want to show the menu, so that customer can view it in the website

##### Milestone 3 - Reservation
This is the core functionality of the application towards customers and the staff.
- As a customer I want to reseve a table for a particular date and time for a number of guests in advanced without payment
- As a customer I want to be able to view my current reservations
- As the restaurant owner I want my staff to be able to view current reservations of the restaurant, so that we can modify, cancel an existing reservation upon customer request

##### Milestone 4 - Security
User stories that cover security aspects of the application.
- As a customer I want to be able to create an account in the restaurant website, so that I can easily reserve tables next time
- As the restaurant owner I want customers to verify their email address via a link sent to thier email account
- As the restaurant owner I want customers to login, to view their reservations
- As the restaurant owner I want my staff to login, to view, modify and cancel customer reservations

##### Milestone 5 - Deployment
Covers all the user stories related to the application deployment
- As a developer I want my application to be deployed in a cloud environment like Heroku
- As a developer I want to configure environment variables properly in Heroku

## The Scope Plane
- Home page with information about the restaurant
- Based on user roles has limited access to features
- Hamburger menu for mobile devices
- Responsive from 390px to up devices
- Create, read, update and delete reservations

## The Structure Plane 
### Features

#### Navigation Menu 

User Story - `As a developer I need to implement a navbar so that I can enable navigation in my website`

- Through the navigation menu provides the capabiliy to browsing through different parts of the website.
- Navigation contains
  - Home - Navigates to the home page
  - Book a table - Navigates to the table reservations
  - Menu - Nvigates to the menu page
  - Reservations - Navigates to a list reservations. Visible to logged in users
  - Sign In
  - Sign Up
  - Sign out - Visible only to a logged in user

TODO Image

#### Home Page
User story - `As the restaurant owner I want a home page, so that customers can view information about my restaurant`

- Provides Information about the restaurant and the owner to the users
- Contains a hero image about, and about the restaurant owner

TODO Image

#### Footer
User story = `As a developer I need to implement a footer so that I can provide copyrights, social media links`

- Provides social media linkes to facebook, twitter, Instagram
- Also contains copyright information
TODO image

#### Contact Us. Opening Hours
User story - `implement a contact and Open hours  so that I can provide contact information and information opening hours`

- Provides contact information and information on opening hours of the restaurant
TODO image

#### Menu Page
User story - `As the restaurant owner I want to show the menu, so that customer can view it in the website`

- Provides the menu that is served by the restaurant. Customers can navigate and view the menu before making decision to 
TODO imag

#### Book a Table
User story - `As a customer I want to reseve a table for a particular date and time for a number of guests in advanced without payment`

- Provides the capabiliy to reserve a table for the date and time. 
- Any customer can make a  reservation, even the unauthorised

TODO images

#### Reservation
User story - `As a customer I want to be able to view my current reservations`
User story - `As the restaurant owner I want my staff to be able to view current reservations of the restaurant, 
so that we can modify, cancel an existing reservation upon customer request`

- Only authenticated can access reservations page. 
- Customers will see their reservations and will be able to edit or cancel
- The staff will be able see reservations for any customer 

TODO images

#### Edit Reservation
User story - `As the restaurant owner I want my staff to be able to view current reservations of the restaurant, 
so that we can modify, cancel an existing reservation upon customer request`

- Customer or the staff member is allowed to edit the reservations

TODO image

#### Delete Reservation 
User story - `As the restaurant owner I want my staff to be able to view current reservations of the restaurant, 
so that we can modify, cancel an existing reservation upon customer request`

- Customer or the staff member is allowed to delete / cancel the reservations

TODO image

### Error pages

Error pages provide a mechanism to fallback if a user encountrs an error.

User story - `As a user I need to see a 404 error page, if the page I'm trying to access is not available`
User story - `As a developer I need to implement a 500 for unrecoverable errors in the system, so that users can be instructed how to proceed`
User story - `As a developer I want to redirect unauthorized users to 403 page, so that I can secure my view`

- 404 error page is used to indicate a broken link
- 403 error page is used, when authorization error occurres
- 500 error page is a general error page for all other types of errors

### Features left to implement
- Ability to edit the restaurant menu.
- Favicon

## The Skeleton Plane
### Design

TODO images

### Database Design

The database model is designed to hold necessary data for customers to create reservations. If they want to they can 
create an account and view their reservations. It also helps to manage the capacity of the restaurants at a given time.

Customer, Reservationslinked through foriegn keys. This allows users to view and update reservations later on.
Reservations are also linked to tables which gives the capability to track the capacity of the restaraunt and manage the crowd.

Entity Relationship diagram is created using DBeaver.

### Security
Views are secured by django class based view mixins. Data access was restricted based on whether the user
is a staff member or not.

Environment variables are store in env.py for local development. During heroku deployments configurations 
were added to the heroku configurations. This secures the keys and passwords, by not having to be commited
to a public code repo.

### Technologies
- HTML, CSS, Bootstrap - Content structure was created using HTML and CSS combined with Bootstrap is used to style the website
- Python, Django - Django framework is used to create the application structure and python was used as the main programming language
- VSCode - IDE used in developing the web app
- GitHub, Git - Git is used as the source code versioning system on the Github cloud platform to store the code
- Figma - Figma is used to create the prelimineray website design

#### Python modules used
- crispy-bootstrap5==2023.10 - Styling the forms with bootstrap
dj-database-url==0.5.0 - Parsing the db urls using environment variables
Django==4.2.8 - Main runtime framework for the web application
django-allauth==0.60.0 - Authentication module
django-crispy-forms==2.1 - Module that handles the bootstrap styling of forms
django-formtools==2.5.1 - Multi step form wizard

### Testing
Testing was performed manually after create a test matrix










































s

