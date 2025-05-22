# Riders-Club-Project

## Features

Website has the following pages:
- Home Page
- Contact Page
- Book Training Page
- Login Page
- Logout Page
- Registration Page
- Create New Booking Page
- Bookings Details Page
- Update Booking Page
- Confirm Deletion Page
- Contact Form Success Page
- Error Pages



### Pages:

Each page has a navbar and a footer

#### Navbar

1 Navbar has the following links with logout:

![Navbar, logout](documentation/features/navbar/navbar.png)

- Home page.
- Contact page.
- Book Training page.
- Registration page.
- Login page.
- A title name: RidersClub
- It also has a statement: community for cyclists and motorcyclists, and a message display below it: Not logged in

2 Navbar has the following links with login:

![Navbar, login](documentation/features/navbar/navbar2.png)

- Home page.
- Contact page.
- Book Training page.
- Logout page.
- A title name: RidersClub
- It also has a statement: community for cyclists and motorcyclists, and a message display below it: logged in as (Username).

3 Navbar has the Hamburger Menu on mobile devices:

![Navbar, login](documentation/features/navbar/navbar5.png)

- Navbar Hamburger Menu With login
![Navbar, login](documentation/features/navbar/navbar3.png)

- Navbar Hamburger Menu With logout
![Navbar, logout](documentation/features/navbar/navbar4.png)



#### Footer

![Footer](documentation/features/footer/footer.png)

Footer has the following sections:

- About RidersClub in first place.

- Quick Links in the second place.

- Social Medial links in the third place.

- Footer bottom which is below the above three sections, houses the copyright statement.

For mobile devices, the footer looks like Viz:

![Footer](documentation/features/footer/footer2.png)



#### Home Page


The Home page consist of a hero section, features section, gallery section and testimonials.
![Home page](documentation/features/home_page/home_page.png)
![Home page](documentation/features/home_page/home_page2.png)


##### Hero Section

This section has a welcome message and a button "Book Training" at the center which leads to the book training page. Under the hero 

section, there is a section, which describes the features of the Riders Club.

![Home page Hero section](documentation/features/home_page/home_page_hero.png)

##### Features Section

This section has 3 images in 3 parts displayed in a row, with a title, and a description at the top for all. The first image is a race cyclist, the second image is a city cyclist with a child behind the loader, and the third image is a motorcyclist.

On the mobile version, the sections are displayed in a column.

![Home page Features section](documentation/features/home_page/home_page_features.png)

##### Gallery Section

This section has 3 parts displayed in a row, each with an icon, a title, and a description.

On the mobile version, the sections are displayed in a column.

![Home page Gallery section](documentation/features/home_page/home_page_gallery.png)

##### Testimonials Section

The section is the testimony of two users with their ratings.

![Home page Testimonials section](documentation/features/home_page/home_page_testimonials.png)


#### Contact Page

 The Home page consist of a hero section, features section, gallery section and testimonials.
![Contact page](documentation/features/contact_page/contact_page.png)
![Contact page](documentation/features/contact_page/contact_page2.png)


##### Contact Information Section

This section has two sections, first section contains a welcome message and second section contains address(email, telephone, and postal address) and location google map in an iframe. 

![Contact page, Contact Information Section](documentation/features/contact_page/contact_info.png)

On the mobile version, the sections are displayed in a column.

![Contact page, Contact Information Section](documentation/features/contact_page/contact_info2.png)

##### Business Hours Section

This section contains working days and opening and clossing hours. It is displayed in a row, with a title, and a description at the top.

On the mobile version, the sections is displayed in same way; centered.

![Contact page Business Hours Section](documentation/features/contact_page/contact_hours.png)

##### Contact Form Section

This section is a contact form with required entries of name, email, and message. A submit button is below and a successful message will display if positive , otherwise a failed message will display indicating what to fix.

On the mobile version, the section is displayed in same way.

![Contact page Contact Form Section](documentation/features/contact_page/contact_form.png)


##### FAQ Section

The section is the testimony of two users with their ratings.

On the mobile version, the section is displayed in same way.

![Contact page FAQ Section](documentation/features/contact_page/contact_faq.png)

#### Book Training Page

 The book training page consist of a welcome page header message , section header message; your bookings and a button to create new bookings. Below is a table showing all user bookings illustrated by slot, status, created at, action. Under action, user is able to see booking details, update booking, and delete booking. Below the table, pagination is displayed when there is pagination.

 Book training page when there are no bookings.

![Contact page](documentation/features/booking_page/booking_book.png)

Book training page when there are bookings.

![Contact page](documentation/features/booking_page/booking_book2.png)

On the mobile version, the booking table section is scrollable.

![Contact page](documentation/features/booking_page/booking_book3.png)



### Login Page

Login Page has a white background with a login form, which has a header including a "signup" button if user is not registered. The login form includes input fields for the user to fill in. Plus it has a button "Sign In".

![Login page](documentation/features/login_page/login_page.png)

On the mobile version, the page is displayed as viz:

![Login page](documentation/features/login_page/login_page1.png)


### Logout Page

This page has a white background with a logout form with a header and a button "Logout" leading to the home page.

![Logout page](documentation/features/logout_page/logout_page.png)

On the mobile version, the page is displayed as viz:

![Logout page](documentation/features/logout_page/logout_page1.png)

### Registration Page

This page has a white background with a registration form, which has a header including a "signin" button if user is already registered. The form includes input fields for the user to fill in user name, optional email, password and password again. Plus it has a button "Sign Up".

![Registration Page](documentation/features/registration_page/registration_page.png)

On the mobile version, the page is displayed as viz:

![Registration Page](documentation/features/registration_page/registration_page1.png)



### Create New Booking Page

This page has a link in the book training page, when clicked, it leads to the create new booking page. The page has a header and includes input fields for the user to fill in slot(required), optional notes, and status(required). It has a button at the bottom: "Create New Booking". 

![Create New Booking Page](documentation/features/new_booking_page/new_booking_page.png)

If succesful, a booking is created and leads you to the booking training page and a succesful message will display. If unsuccesful, an error message will display and equally gives you an explanation of what is wrong. For example as viz:

![Create New Booking Page](documentation/features/new_booking_page/new_booking_page1.png)

On the mobile version, the page is displayed as viz:

![Create New Booking Page](documentation/features/new_booking_page/new_booking_page2.png)



### Bookings Details Page

This page has a button link in the "book training page" as "Detail" for each booked slot. When clicked, it leads to the "Bookings Details Page". The page has a header and displays booked date, time, location, and status(pending, confirmed, or cancelled). 

It equally has 3 buttons at the bottom which are: "Update"; leads to update booking page, "Delete"; leads to delete booking page, and  "Book Training" leads to book training page. 

![Bookings Details Page](documentation/features/detail_booking_page/detail_booking_page.png)

On the mobile version, the page is displayed as viz:

![Bookings Details Page](documentation/features/detail_booking_page/detail_booking_page1.png)


### Update Booking Page

This page has a link in the book training page for each booking. When clicked, it leads to the update booking page. The page has a header and includes input fields for the user to edit whic are: slot(required), optional notes, and status(required). 

It has two buttons at the bottom: "Update Booking" button; which updates the booking and leads to "Book Training page" and "Cancel" button; which leads to "Book Training page".

![Update Booking Page](documentation/features/update_booking_page/update_booking_page.png)

On the mobile version, the page is displayed as viz:

![Update Booking Page](documentation/features/update_booking_page/update_booking_page1.png)



### Confirm Deletion Page

This page has a link in the book training page for each booking as "Delete". When clicked, it leads to the "Confirm Deletion Page". The page has a header and includes the slot's booking date, time, place, status, notes, and date/time created.

It has two buttons at the bottom: "Yes, Delete it" button; which deletes the booking and leads to "Book Training page" and "Cancel" button; which leads to "Book Training page".

![Confirm Deletion Page](documentation/features/confirm_deletion_page/confirm_deletion_page.png)

On the mobile version, the page is displayed as viz:

![Confirm Deletion Page](documentation/features/confirm_deletion_page/confirm_deletion_page1.png)


### Contact Form Success Page

This page displays when a contact form in the contact page is submitted succesfully. It displays a thank you message and assures you of a reply.

![Contact Form Success Page](documentation/features/contact_success_page/contact_success_page.png)

On the mobile version, the page is displayed as viz:

![Confirm Deletion Page](documentation/features/contact_success_page/contact_success_page1.png)


### Error Pages

There are 2 additional error pages:

  it has a box with the header "404 - Page Not Found", an image and a short message about the error ("The page you're looking for doesn't exist or may have been moved").

  If the user is logged in and tries to access a page that doesn't exist, he/she will find a button with the link to his/her Book Training page.

  ![Error Page. 404. Link to user profile](documentation/features/error_page/404_error_page.png)

  If the user is logged out and tries to access a page that doesn't exist, he/she will find a button with the link to the home page

  ![Error Page. 404. Link to home page](documentation/features/error_page/404_error_page1.png)

  Page 505 is the same as 404 page, but it has a different header ("500 - Internal Server Error") and message ("Something went wrong due to an internal server error").

  ![Error Page. 500](documentation/features/error_page/500_error_page.png)

### Favicon

  ![Favicon](documentation/features/favicon/favicon.png)

  The favicon is a small image displayed in the browser's address bar. It identifies the website amongst others.

[Back to contents](#contents)

---