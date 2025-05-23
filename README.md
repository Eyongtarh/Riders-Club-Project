# Riders-Club-Project

[Link to Riders-Club-Project](https://riders-club-project-013aecf05a65.herokuapp.com/)



## About

Riders-Club-Project is a club designed for a community of cyclists and motorcyclists. They can book training and improve
on their skills.

## User Experience Design

### Target Audience

The website was developed to meet the need to improve skills for:
  * Cyclists.
  * Motorcyclists.

### User Stories


#### Site Developer Goal

| Issue ID    | User Story |
|-------------|-------------|
|[#1](https://github.com/users/Eyongtarh/projects/8/views/1?pane=issue&itemId=108992563&issue=Eyongtarh%7CRiders-Club-Project%7C1)| As a site developer, I want to set up both development and production environments, so that I can build and deploy a reliable Riders club website. |


#### Site User Goals

| Issue ID    | User Story |
|-------------|-------------|
|[#2](https://github.com/users/Eyongtarh/projects/8/views/1?pane=issue&itemId=108992635&issue=Eyongtarh%7CRiders-Club-Project%7C2)|As a site user, I want to register and log in to an account so that I can book club training sessions.|
|[#3](https://github.com/users/Eyongtarh/projects/8/views/1?pane=issue&itemId=108992665&issue=Eyongtarh%7CRiders-Club-Project%7C3)|As a logged-in site user, I want to create, view detail, update, and delete my booked trainings so that I can manage my training schedule effectively.|
|[#4](https://github.com/users/Eyongtarh/projects/8/views/1?pane=issue&itemId=108992698&issue=Eyongtarh%7CRiders-Club-Project%7C4)|As a site user, I want to fill out and submit a contact form to express my interest in collaborating with the club, So that the club can review my request and get in touch with me for further communication.|


#### Site Owner Goals

| Issue ID    | User Story |
|-------------|-------------|
|[#5](https://github.com/users/Eyongtarh/projects/8/views/1?pane=issue&itemId=108992724&issue=Eyongtarh%7CRiders-Club-Project%7C5)|As a site owner I can update home page so that I can make users to better understand the purpose of the club.|
|[#6](https://github.com/users/Eyongtarh/projects/8/views/1?pane=issue&itemId=108992750&issue=Eyongtarh%7CRiders-Club-Project%7C6)|As a site owner I can add information to contact page so that I can make it easier for users to reach site owner.|

---

## Technologies used

- ### Languages:
    
    + [Python 3.12.8](https://www.python.org/downloads/release/python-385/): the primary language used to develop the 
      server-side of the website.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.

- ### Frameworks and libraries:

    + [Django](https://www.djangoproject.com/): python framework used to create all the logic.

- ### Databases:

    + [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.

- ### Other tools:

    + [Git](https://git-scm.com/): the version control system used to manage the code.
    + [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
    + [Gunicorn](https://gunicorn.org/): the webserver used to run the website.
    + [Spycopg2](https://www.python.org/dev/peps/pep-0249/): the database driver used to connect to the database.
    + [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
    + [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of
      Django forms.
    + [GitHub](https://github.com/): used to host the website's source code.
    + [Whitenoise](https://whitenoise.readthedocs.io/en/latest/): used to adically simplify static file serving for Python web apps.
    + [VSCode](https://code.visualstudio.com/): the IDE used to develop the website.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
    + [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.
    + [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
    + [PEP8](https://pep8.org/): was used to validate Python code for the website.
    + [Compress JPEG](https://compressjpeg.com/) was used to compress JPEG images.
    + [IMGonline.com.ua](https://www.imgonline.com.ua/eng/resize-image.php) was used to resize images.
    + [FAVICON GENERATOR](https://favicon.io/) was used to generate the favicon.
    + [Bytes](https://ui.dev/amiresponsive?url=https://eyongtarh.github.io/Eyongtarh-Tennis-Club/" ) was used to test website wireframes.



---

## Features

Please refer to the [FEATURES.md](FEATURES.md) file for all features-related documentation.


---

## Design

The design of the website is based on the Material Design principles.

### Wireframes

Please refer to the [WIREFRAMES.md](WIREFRAMES.md) file for all features-related documentation.


---

## Information Architecture

### Database

* The database was created using PostgreSQL.

### Entity-Relationship Diagram

* The ERD was created using [Lucidchart](https://www.lucidchart.com/).

- [Database Scheme](documentation/diagrams/db_scheme.png)

### Data Modeling

1. #### Bookings

a. ***AvailableSlot***

This represents bookable time slots.
Extends Allauth's User model.

| Name          | Database Key  | Field Type    | Validation           |
| ------------- | ------------- | ------------- | ---------------------|
| Id            | id            | AutoField     | Pk                   |
| Date          | date          | DateField     | required             |
| Time          | time          | TimeField     | required             |
| Location      | location      | CharField     | max length 100       |



```Python

Validation Rule:

- unique(date, time, location)

This prevents duplication of slots at same place and time.

- Ordered is done by date, then time.

```

b. ***Booking***

This represents a booking made by a user.
Extends Allauth's User model.

| Name          | Database Key  | Field Type    | Validation                       |
| ------------- | ------------- | ------------- | ---------------------------------|
| Id            | id            | AutoField     | Pk                               |
| User id       | user_id       | ForeignKey    | User, on_delete=CASCADE          |
| Slot id       | slot_id       | ForeignKey    | AvailableSlot, on_delete=CASCADE |
| Notes         | notes         | TextField     | max length 250, optional         |
| Created at    | created_at    | DateTime      | auto_now_add=True             |
| Status        | status        | Int           | choices=0: Pending, 1: Confirmed, 2: Cancelled, default=0: Pending|


```Python

Validation rule ensures:
- A booking must have a valid slot
- There is no double booking of same slot.
- User can not book slots in the past.
- It automatically confirms a slot if no pending booking exists.

Ordering:
The ordering is done from the most recent first.

```

2. #### Contact

This stores contact form submissions.

| Name          | Database Key  | Field Type    | Validation                       |
| ------------- | ------------- | ------------- | ---------------------------------|
| Id            | id            | AutoField     | Pk                               |
| Name          | name          | CharField     | max length 100, required         |
| Email         | email         | EmailField    | required                         |
| Messagees     | message       | TextField     | max length 250, required         |
| Created at    | created_at    | DateTime      | auto_now_add=True                |


---
## Testing

Please refer to the [TESTING.md](TESTING.md) file for all test-related documentation.

---

## Deployment

Please refer to the [DEPLOYMENT.md](DEPLOYMENT.md) file for all deployment-related documentation.

---

## Credits

- [GitHub](https://github.com/) for giving the idea of the project's design.
- [Django](https://www.djangoproject.com/) for the framework.
- [Font awesome](https://fontawesome.com/): for the free access to icons.
- [Heroku](https://www.heroku.com/): for the free hosting of the website.
- [Icons8](https://icons8.com/): for providing free access to amazing icons and illustrations.
- [Postgresql](https://www.postgresql.org/): for providing a free database.
- [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en): for providing a free platform to test website responsiveness
- [GoFullPage](chrome://extensions/?id=fdpohaocaechififmbbbbbknoalclacl): for allowing to create free full web page screenshots;
 - [Compress JPEG](https://compressjpeg.com/) was used to compress JPEG images.
 - [IMGonline.com.ua](https://www.imgonline.com.ua/eng/resize-image.php) was used to resize images.
 - [FAVICON GENERATOR](https://favicon.io/) was used to generate the favicon.
 - [bytes](https://ui.dev/amiresponsive?url=https://eyongtarh.github.io/Eyongtarh-Tennis-Club/" ) was used to test website 
   responsiveness.


*All names are fictional (the majority of the names were taken from "The Simpsons" and "Rick and Morty" cartoons), and any resemblance to actual events or locales or persons, living or dead, is entirely coincidental.*


---

## Acknowledgments


- [Tim Nelson](https://github.com/TravelTimN) was a great supporter of my bold idea of a project. Tim helped me to understand the concept of a database for the school app and greatly motivated me to do my best throughout the whole development stage.
- [Aleksei Konovalov](https://github.com/lexach91), my husband and coding partner, who assisted me greatly in understanding AJAX implementation and helped me to stay sane.
- My current workplace for providing me with the main idea for the project and incentivizing me to work on it.

## Acknowledgments

- [Code Institute](https://codeinstitute.net/) tutors and Mentor for their continues support.
- [Hot Air Tools](https://www.hotairtools.com/) content for welding page.


