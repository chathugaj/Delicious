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
- As a developer I need to implement a footer so that I can provide contact information, copyrights, social media links

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
