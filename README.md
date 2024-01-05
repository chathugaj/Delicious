![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. If you are using Gitpod then you need [this template](https://github.com/Code-Institute-Org/gitpod-full-template) instead. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **August 30th, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

# User stories

Epic - Main setup

- As a developer I have to create the main layout using HTML, so that the layout can be reused
- As a developer I need to find suitable images so that website has more visual context
- As a developer I need to add CSS styles so that pages look easthetic
- As a developer I need to add Javascript so that page have more dynamic functionality
- As a devleoper I need to setup the project with necesssary dependencies, so that I can develop the core features
- As a developer I need to implement a navbar so that I can enable navigation in my website
- As a developer I need to implement a footer so that I can provide contact information, copyrights, social media links

Epic - General feature pages

- As a user I need to see a 404 error page, if the page I'm trying to access is not available
- As a developer I need to implement a 500 for unrecoverable errors in the system, so that users can be instructed how to proceed
- As a developer I want to redirect unauthorized users to 403 page, so that I can secure my view
- As the restaurant owner I want a home page, so that customers can view information about my restaurant
- As the restaurant owner I want to show the menu, so that customer can view it in the website

Epic - Reservation

- As a customer I want to reseve a table for a particular date and time for a number of guests in advanced without payment
- As a customer I want to be able to view my current reservations
- As the restaurant owner I want my staff to be able to view current reservations of the restaurant, so that we can modify, cancel an existing reservation upon customer request

Epic - Events

- As the restaurant owner I want to be able to add, modify and remove events hosted by the restaurant, so that customers can view a list of events
- As a customer I want to be able to view events hosted by the restaurant, so that I can attend

Epic - Security

- As a customer I want to be able to create an account in the restaurant website, so that I can easily reserve tables next time
- As the restaurant owner I want customers to verify their email address via a link sent to thier email account
- As the restaurant owner I want customers to login, to view their reservations
- As the restaurant owner I want my staff to login, to view, modify and cancel customer reservations
- As the restaurant owner I want my staff to login, to create, modify and remove events
