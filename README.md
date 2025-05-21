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


#### **Site Developer Goals**

| Issue ID    | User Story |
|-------------|-------------|
|[#1](https://github.com/users/Eyongtarh/projects/8/views/1?pane=issue&itemId=108992563&issue=Eyongtarh%7CRiders-Club-Project%7C1)| As a site developer, I want to set up both development and production environments, so that I can build and deploy a reliable Riders club website. |


#### **Site Developer Goals**

| Issue ID    | User Story |
|-------------|-------------|
|[#2](https://github.com/users/Eyongtarh/projects/8/views/1?pane=issue&itemId=108992635&issue=Eyongtarh%7CRiders-Club-Project%7C2)|As a site user, I want to register and log in to an account so that I can book club training sessions.|
|[#3](https://github.com/users/Eyongtarh/projects/8/views/1?pane=issue&itemId=108992665&issue=Eyongtarh%7CRiders-Club-Project%7C3)|As a logged-in site user, I want to create, view, update, and delete my booked trainings so that I can manage my training schedule effectively.|
|[#4](https://github.com/users/Eyongtarh/projects/8/views/1?pane=issue&itemId=108992698&issue=Eyongtarh%7CRiders-Club-Project%7C4)|As a site user, I want to fill out and submit a contact form to express my interest in collaborating with the club, So that the club can review my request and get in touch with me for further communication.|


#### **Site Owner Goals**

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
    + [bytes](https://ui.dev/amiresponsive?url=https://eyongtarh.github.io/Eyongtarh-Tennis-Club/" ) was used to test website 
      responsiveness.



---

## FEATURES

Please refer to the [FEATURES.md](FEATURES.md) file for all features-related documentation.


---

## Design

The design of the application is based on the Material Design principles.
The central theme of the application is the simplicity of use. Thus, all the components are designed to be easy to use. The minimalistic approach was used to create something meaningful without moving out of focus. As this application is a multifunctional one and consists of many components, the decision to implement white spaces was made as it helps to create a more pleasant user experience. 

### Color Scheme

The color scheme of the application is based on the bold colors:

  ![Color Scheme](documentation/design/color_palette.png)

As it may be noticed, the color scheme is based on the Material Design principles as well. The navbar is green with dark blue text. The background is white with light blue waves, which are almost invisible. There is a dark blue button to guide the user on how to find the menu.
The footer is a dark blue with white text to stand out.

Since the main content has various functions, two different colors were used as the background for the main boxes. The first one is #001D82, which is the color of the navbar text. The decision to use this color for the login/logout/register boxes was made as it shows that the user isn't logged in.
The #93D3FD is the color of the data boxes. This color is consistent with the color scheme throughout the whole application. In addition to this, the blue color is believed to be the preferred color among people and facilitates trust and security.

All buttons except the navbar button are green with the white text editing and cancel functionality and orange for the submission and deletion function.
### Typography

The main font used in the application is Lato. The use of this font is consistent with the color scheme. Needless to say, the Lato font was chosen due to its readability, which increases user experience.

  ![Typography](documentation/design/lato_400.png)

  ![Typography](documentation/design/lato_700.png)

  ![Typography](documentation/design/lato_900.png)

To emphasize the importance of the text, the font-weight was set to 900. To make the accent on the buttons, the font-weight was set to 700. For the rest of the text, the font-weight was set to 400.

### Imagery

- The main background image was generated with the user of the [BGJar](https://www.bgjar.com/) tool. The image was generated with the following settings:

  ![Background](documentation/design/background.svg)

To generate this particular pattern, I used Contour Line Generator with white background and #93D3FD54 as the color of the lines. 

- Images were downloaded from the [icons8](https://icons8.com/) website only for the home page. However, the original images were changed manually to match the color scheme.

- The main part is allocated to the use of icons from the [font awesome](https://fontawesome.com/) website. The use of icons is essential for the user experience when it comes to multifunctional websites.


### Wireframes

- [Desktop Wireframes](documentation/wireframes/pp4_desktop.pdf)
- [Tablet Wireframes](documentation/wireframes/pp4_tablet.pdf)
- [Mobile Wireframes](documentation/wireframes/pp4_mobile.pdf)



---

## Flowcharts

This application is aimed at users with different roles to fulfill their expectations and provide all functionality.

The following flowcharts were created to help to understand the application and its functionality.

The flowcharts were created using [Draw.io](https://www.lucidchart.com/).

- [Flowchart for Bosses](documentation/flowcharts/flowchart_boss.pdf)
- [Flowchart for Sales Managers](documentation/flowcharts/flowchart_sales.pdf)
- [Flowchart for Parents](documentation/flowcharts/flowchart_parent.pdf)
- [Flowchart for Teachers](documentation/flowcharts/flowchart_teachers.pdf)
- [Flowchart for Receptionist](documentation/flowcharts/flowchart_receptionist.pdf)



---

## Information Architecture

### Database

* During the earliest stages of the project, the database was created using SQLite.
* The database was then migrated to PostgreSQL.

### Entity-Relationship Diagram

* The ERD was created using [Draw.io](https://www.lucidchart.com/).

- [Database Scheme](documentation/diagrams/db_final.pdf)

### Data Modeling

1. **CustomUser**

Extends Allauth's User model.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| UserName      | username      | CharField     |  max_length=50, blank=False, null=True, unique=True    |
| Email         | email         | EmailField    | max_length=50, unique=True, blank=False, null=False    |
| First Name    | first_name    | CharField     | max_length=30, blank=False, null=False    |
| Last Name     | last_name     | CharField     | max_length=30, blank=False, null=False    |
| Phone Number  | email         | CharField     | max_length=30, blank=False, null=False    |
| Role          | phone         | IntegerField  | choices=ROLES, default=5    |


```Python
    # Roles to assign to users
    ROLES = (
        (0, 'boss'),
        (1, 'teacher'),
        (2, 'sales'),
        (3, 'receptionist'),
        (4, 'parent'),
        (5, 'potential user'),
    )
```

2. **Teacher**

It was created in order to provide more room for manipulation of the database and provide opportunities for future developments. Users with the role of teacher will be automatically assigned to this table.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Teacher       | user          | ForeignKey    |  CustomUser, on_delete=models.CASCADE  |

3. **Receptionist**

It was created in order to provide more room for manipulation of the database and provide opportunities for future developments.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Receptionist  | user          | ForeignKey    |  CustomUser, on_delete=models.CASCADE  |

4. **SalesManager**

It was created in order to provide more room for manipulation of the database and provide opportunities for future developments. Users with the role of sales manager will be automatically assigned to this table.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Sales Manager | user          | ForeignKey    |  CustomUser, on_delete=models.CASCADE  |
| Sales Total   | total_sold    | IntegerField  |  default=0, blank=True, null=True  |

5. **Parent**

It was created in order to provide more room for manipulation of the database and provide opportunities for future developments. Users with the role of the parent will be automatically assigned to this table.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Sales Manager | user          | ForeignKey    |  CustomUser, on_delete=models.CASCADE  |
| Relation to a student  | relation      | IntegerField  |  choices=GUARDIAN_RELATION, default=5  |

```Python
    # Guardian's relation to the student
    GUARDIAN_RELATION = (
        (1, 'father'),
        (2, 'mother'),
        (3, 'grandfather'),
        (4, 'grandmother'),
        (5, 'other'),
    )
```
6. **Student**

This table does not inherit from the CustomUser model. This is because the students are not users. Instead, they are the main table of the application.

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| First Name         | first_name    | CharField       | max_length=50, blank=False, null=False    |
| Last Name          | last_name     | CharField       | max_length=50, blank=False, null=False    |
| Parents            | parent        | ManyToManyField | Parent, related_name='child'  |
| Birthday           | birthday      | DateField       |          |
| Address            | address       | CharField       | max_length=100, blank=True, null=True |
| Date of enrollment | enrolled      | DateTimeField   | auto_now_add=True    |
| Classes left       | classes_left  | IntegerField    | default=0, blank=True, null=True    |
| Sales Manager      | sales_manager | ManyToManyField | SalesManager, related_name='student'    |
| Notes              | notes         | TextField       | blank=True    |

7. **Sales**

This table is needed to conduct sales operations. It controls the sales of the products. It also adds classes to a particular student and adds total classes sold to a sales manager. A separate field "student_id" was added in order to prevent a circular import but allow sales to be in control of classes added to a particular student or reduced (For example, when parents ask for a refund).

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Sales Manager | sold_by       | ForeignKey    | SalesManager, on_delete=models.CASCADE, related_name='sold'   |
| Client(Parent)| sold_to       | ForeignKey    | Parent, on_delete=models.CASCADE, related_name='bought'   |
| Classes Number| amount        | IntegerField  |            |
| Date of Sale  | date          | DateTimeField | auto_now_add=True    |
| Student       | amount        | IntegerField  |  default=0          |

8. **Lesson**

This table is necessary to control the lessons and provide data for the schedule.

| Name          | Database Key  | Field Type     | Validation |
| ------------- | ------------- | -------------- | ---------- |
| Class's Date  | date          | DateField      |            |
| Class's Time  | time          | IntegerField   | choices=TIME_PERIODS, default=0 |
| Subject       | subject       | IntegerField   | choices=SUBJECTS, default=1     |
| Teachers      | teachers      | ManyToManyField| Teacher, related_name='lessons' |
| Students      | students      | ManyToManyField| Student, related_name='lessons' |


```Python
    # Time periods variations
    TIME_PERIODS = (
        (0, '9:00-9:45'),
        (1, '10:00-10:45'),
        (2, '11:00-11:45'),
        (3, '14:00-14:45'),
        (4, '15:00-15:45'),
        (5, '16:00-16:45'),
        (6, '17:00-17:45'),
        (7, '18:00-18:45'),
    )

    # Subject variations
    SUBJECTS = (
        (1, 'art'),
        (2, 'math'),
        (3, 'casa'),
        (4, 'chinese'),
        (5, 'toddlers'),
        (6, 'music'),
        (7, 'english'),
        (8, 'sport'),
        (9, 'cooking'),
        (10, 'infants'),
    )
```




---
## Testing

Please refer to the [TESTING.md](TESTING.md) file for all test-related documentation.



---

## Deployment


- The app was deployed to [Render](https://render.com/).
- The database was deployed to [ElephantSQL](https://www.elephantsql.com/).

- The app can be reached by the [link](https://cool-school.onrender.com).

Please refer to the [DEPLOYMENT.md](DEPLOYMENT.md) file for all deployment-related documentation.

---

## Credits

- [GitHub](https://github.com/) for giving the idea of the project's design.
- [Django](https://www.djangoproject.com/) for the framework.
- [Render](https://render.com/): for the free hosting of the website.
- [ElephantSQL](https://www.elephantsql.com/): for the free hosting of the database.
- [BGJar](https://www.bgjar.com/): for the free access to the background images build tool.
- [Font awesome](https://fontawesome.com/): for the free access to icons.
- [Heroku](https://www.heroku.com/): for the free hosting of the website.
- [jQuery](https://jquery.com/): for providing varieties of tools to make standard HTML code look appealing.
- [Coolors](https://coolors.co/): for providing a free platform to generate your own palette.
- [Icons8](https://icons8.com/): for providing free access to amazing icons and illustrations.
- [Postgresql](https://www.postgresql.org/): for providing a free database.
- [Codemy.com](https://www.youtube.com/watch?v=N-PB-HMFmdo): for providing a free video on how to implement pagination in the project.
- [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en): for providing a free platform to test website responsiveness
- [GoFullPage](chrome://extensions/?id=fdpohaocaechififmbbbbbknoalclacl): for allowing to create free full web page screenshots;
- [Favicon Generator. For real.](https://realfavicongenerator.net/): for providing a free platform to generate favicons.

*All names are fictional (the majority of the names were taken from "The Simpsons" and "Rick and Morty" cartoons), and any resemblance to actual events or locales or persons, living or dead, is entirely coincidental.*


---

## Acknowledgments


- [Tim Nelson](https://github.com/TravelTimN) was a great supporter of my bold idea of a project. Tim helped me to understand the concept of a database for the school app and greatly motivated me to do my best throughout the whole development stage.
- [Aleksei Konovalov](https://github.com/lexach91), my husband and coding partner, who assisted me greatly in understanding AJAX implementation and helped me to stay sane.
- My current workplace for providing me with the main idea for the project and incentivizing me to work on it.


## Acknowledgments

- [Code Institute](https://codeinstitute.net/) tutors and Mentor for their continues support.
- [Hot Air Tools](https://www.hotairtools.com/) content for welding page.


