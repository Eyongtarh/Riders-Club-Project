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
- Confirm Delete Booking Page
- Success Page
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

This page has a button link in the "book training page" as "Detail" for each booked slot. When clicked, it leads to the "Bookings Details Page". The page has a header and displays booked date, time, location, and status(pending, confirmed, or cancelled). It equally has 3 buttons at the bottom which are: "Update"; leads to update booking page, "Delete"; leads to delete booking page, and  "Book Training" leads to book training page. 

![Bookings Details Page](documentation/features/detail_booking_page/detail_booking_page.png)

On the mobile version, the page is displayed as viz:

![Bookings Details Page](documentation/features/detail_booking_page/detail_booking_page1.png)


### Update Booking Page

This page has a button link in the book training page as "Detail" for each booked slot, when clicked, it leads to the "Bookings Details Page". The page has a header and includes input fields for the user to fill in slot(required), optional notes, and status(required). It has a button at the bottom: "Create New Booking". 

  ![Update Booking Page](documentation/features/update_booking_page/update_booking_page.png)

It has a container where the user can edit:

- First Name;
- Last Name;
- Phone Number;

There are three fields with prefilled data for the user. The user could change this data if he/she wants.

  ![Edit profile page](documentation/features/profile_edit_page/profile_edit_fields.png)

Underneath the fields, there are two buttons, "Go Back" and "Save." If the user doesn't want to save changes, they can click on the "Go Back" button and will be redirected to the profile page. If the user wants to save changes, they can click on the "Save" button and will be redirected to the profile page.

  ![Edit profile page](documentation/features/profile_edit_page/cancel_save_buttons.png)

**Profile Delete Page**

  ![Profile delete page](documentation/features/profile_delete_page/profile_delete_page.png)

Only the bosses have access to this page as only they are able to delete any profile.

This page has a box with a warning message and a link to the profile page of the user that is about to be deleted:

  ![Profile delete page](documentation/features/profile_delete_page/member_delete_link.png)

There are two buttons under the warning message, there are two buttons, "Cancel" and "Delete". If the user doesn't want to delete the profile, he/she can click on the "Cancel" button and will be redirected to the profile page. If the user wants to delete the profile, he/she can click on the "Delete" button and will be redirected to the profile page, and the school member will be permanently deleted.

  ![Profile delete page](documentation/features/profile_delete_page/cancel_delete_buttons.png)

**Profile Change Password Page**

  ![Profile change password page](documentation/features/profile_change_password_page/profile_password_page.png)

It has a header with the title "Change Password" and a subtitle to guide the user on what to do next. Underneath, there are three field to be filled:

- Old Password;
- New Password;
- Confirm New Password.

  ![Profile change password page](documentation/features/profile_change_password_page/change_password_fields.png)

If there are any errors in the fields, the user will see the error message.

Under the fields, there are two buttons, "Go Back" and "Submit". If the user doesn't want to change the password, he/she can click on the "Go Back" button and will be redirected to the profile page. If the user wants to change the password, he/she can click on the "Change Password" button and will be redirected to the profile page, and the password will be changed if all conditions are met.

  ![Profile change password page](documentation/features/profile_change_password_page/cancel_delete_buttons.png)

**New Applications Page**

This page is only visible to the boss and sales manager.
  
![New applications page](documentation/features/new_applications_page/new_applications.png)

This page has a title and the number of the new applications left.

  ![New applications page](documentation/features/new_applications_page/new_applications_summary.png)

It also has a table with the new applications, where each application has a link. After clicking on the application in a table, the user will be redirected to the application detail page.

  ![New applications page](documentation/features/new_applications_page/new_applications_data.png)

Underneath the table, there are navigation buttons. If the user wants to see the next page of the application, he/she can click on the "Next" button. If the user wants to see the previous page of the applications, he/she can click on the "Previous" button.

  ![New applications page](documentation/features/new_applications_page/page_navigation1.png)
  ![New applications page](documentation/features/new_applications_page/page_navigation2.png)

**Application Detail Page**

This page is accessible to the boss and sales manager.
For the boss, the page has the following look:

  ![Application detail page. Boss View](documentation/features/application_detail_page/application_detail_admin_view.png)

It has two boxes. The first box consists of the information about the applicant, including the name, the email, and the phone number.

  ![Application detail page. Applicant Data Box](documentation/features/application_detail_page/application_detail_data.png)

It also has a "Delete" button in the top right corner of the page. If the boss wants to delete the application, he/she can click on the "Delete" button and will be redirected to the delete application page.

  ![Application detail page. Delete Button](documentation/features/application_detail_page/application_detail_delete_button.png)

The second box provides the boss with the assigning role functionality, which will give access to the applicant to the application according to the role the boss assigns.

  ![Application detail page. Role Assignment Box](documentation/features/application_detail_page/application_detail_role.png)

When the boss clicks on the dropdown menu, the following choices will be shown:

  ![Application detail page. Role Choices](documentation/features/application_detail_page/application_detail_role_choice.png)

After choosing the role the boss wants to assign, he/she can click on the "Save" button.

  ![Application detail page. Save Role Button](documentation/features/application_detail_page/application_detail_save_role_button.png)

When the boss clicks on "Save" button, the role will be assigned to the applicant. However, it will not redirect the boss to any page in order to prevent the boss from accidentally assigning the wrong role to an applicant.

To go back to the applications page, the boss may click on the link underneath the boxes "Go to other applications". And the user will be redirected to the applications page.

  ![Application detail page. Go back to applications](documentation/features/application_detail_page/application_detail_back.png)

For the sales manager, the page has the following look:

  ![Application detail page. Sales Manager View](documentation/features/application_detail_page/application_detail_sale_view.png)

The page has no "Delete" button as it is not accessible to the sales manager. Moreover, the page has no box with the assigning role to the new applicant as it is accessible only to the boss.

**Application Delete Page**

  ![Application delete page](documentation/features/application_delete_page/application_delete_page.png)

This page is only accessible to the boss. Thus, only the boss is empowered to delete any applications.
It has a warning message with the applicant's name.

  ![Application delete page](documentation/features/application_delete_page/application_delete_warning.png)

It also has 2 buttons, "Go Back" and "Delete". If the boss doesn't want to delete the application, he/she can click on "Go Back" button and will be redirected to the application detail page. If the boss wants to delete the application, he/she can click on "Delete" button. He / she will be redirected to the new applications page, and the application will be permanently deleted.

  ![Application delete page](documentation/features/application_delete_page/cancel_delete_buttons.png)

**Limited Access Page**

  ![Limited access page](documentation/features/limited_access_page/limited_access_page.png)

This page applies to the users that are not allowed to access the page that they want to enter manually in the address bar. it has a box with a friendly message pointing out that the user has no access to a particular page. It also has a link to the user's profile page.


  ![Limited access page. Link to Personal Profile](documentation/features/limited_access_page/limit_access_link.png)



**Error Pages**

There are also 2 additional error pages:

  ![Error Page. 404](documentation/features/error_page/404_error_page.png)

  it has a box with the header "Page 404", an image and a short message about the error ("Something went wrong as this page is not found").

  If the user is logged in and tries to access a page that doesn't exist, he/she will find a button with the link to his/her profile page.

  ![Error Page. 404. Link to user profile](documentation/features/error_page/404_error_page2.png)

  If the user is logged out and tries to access a page that doesn't exist, he/she will find a button with the link to the home page

  ![Error Page. 404. Link to home page](documentation/features/error_page/404_error_page1.png)

  Page 505 is the same as 404 page, but it has a different header ("Page 500") and message ("Something went wrong as there is an internal sever error!").

  ![Error Page. 500](documentation/features/error_page/500_error_page.png)

**Favicon**

  ![Favicon](documentation/features/favicon/favicon.png)

  The favicon is a small image that is displayed in the browser's address bar. It is used to identify the website among others and help the user to find it when he/she is searching for it.

[Back to contents](#contents)

---