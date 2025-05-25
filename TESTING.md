# Testing

## Manual Testing

Testing was done throughout site development, for each feature before it was merged into the main file.

Usability was tested with the below user acceptance testing, sent to new users to ensure testing from different users, on different devices and browsers to ensure issues were caught and where possible fixed during development.


|     | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Sign Up     |                        |                  |      |             |
| 1           | Click on the Register link,on mobile devices, click Hamburger Icon then click Register| Redirection to Sign Up page: Login and SignUp | Y |          |
| 2           | Click on the Login button in Sign Up page | Redirection to Login page | Y |          |
| 3           | Enter valid email(optional)| Field will only accept email address format | Y |          |
| 4           | Enter valid username | Field will only accept no more than 150 characters | Y |          |
| 5          | Enter valid password | Field will only accept secure passwords | Y |          |
| 6          | Enter valid password again | Field will only accept the same password from the previous field | Y |          |
| 7          | Click on the Sign Up button | Takes user to Home page confirming successful sign up.| Y |          |
| 8          | Sign In with the same username and password | Takes user Home page confirming successful sign in.  | Y |          |
| 9          | Click Logout button on link, on mobile devices, click Hamburger Icon then click logout button| Takes user to log out page to confirm logout | Y |          |
| 10          | Click "Logout" button  in the page| Redirects user to home page | Y |          |
| 11          | Click browser back button | You are still logged out | Y |          |
| Log In      |                        |                  |      |             |
| 1           | Click on the log in link, on mobile devices, click Hamburger Icon then click log in | Redirection to Sign in page: SignUp and Sign in| Y |          |
| 2           | Click on the SignUp link in the form | Redirection to SignUp page | Y |          |
| 3           | Enter valid username | Field will only accept registerd username | Y |          |
| 4           | Enter valid password | Field will only accept secure passwords | Y |          |
| 5           | Click on the Sign In button | Takes user to home page with pop-up confirming successful sign in. Register link now missing in main nav, replaced by Logout | Y |          |
| 6           | Click "Logout" link, on mobile devices, click Hamburger Icon then click logout| Takes user to log out page to confirm logout | Y |          |
| 7           | Click "Logout" button  in the page| Redirects user to home page | Y |          |
| 8          | Click browser back button | You are still logged out | Y |          |
| Home        |                        |                  |      |             |
| 1           | Click on the "Book Your Training" button at the center of the home page banner| Redirection to Training page | Y | Available to everyone |
| 2           | Click on RidersClub in navbar | Redirection to Home page | Y | Available to everyone |
| 3           | Click browser back button | Redirection to Home page | Y | Available to everyone |
| Contact     |            |                  |      |             |
| 1           |  Click Contact link, on mobile devices, click Hamburger Icon then click Contact | Redirection to contact page | Y | Available only to everyone  |
| 2           |  Fill form and Click submit | Redirect to success message page | Y |  Available to everyone  |
| Book Training        |     |      |     |    |
| 1           |  Click "Book Training" link, on mobile devices, click Hamburger Icon then click Book Training linkj | Redirection to Book Training Page | Y | Available only to logged in users|
| 2           |  Click "Create New Booking" button in the Book Training page| Redirection to Creat New Booking page| Y | Available only to logged in users |
| 3           |  Click on create new Booking after filling the form | Redirection to Book Training page and success messaeg for new booking created| Y | Available only to logged in users |
| 4           |  Click "cancel" button in the create new booking page | Redirection to Book Training page | Y | Available only to logged in users |
|Bookin Details       |     |      |     |    |
| 1           |  Click "Detail" in the newly created booking table in the booking page| Redirection to Boking Details page| Y | Available only to logged in users|
| 2          |  Click "Update" button in the booking details page | Redirection to update buttons page| Y | Available only to logged in users |
| 3          |  Click "Delete" button in the Booking Details page | redirected to Confirm Deletion page | Y | Available only to logged in users |
| 4          |  Click "Book Training" button in the Booking Details page| Redirection to book training page | Y | Available only to logged in users |
|Update Booking       |     |      |     |      |
| 1          |  Click "Update" button in the newly created booking table in the booking page | Redirection to update booking page| Y | Available only to logged in users|
| 2          |  Click "Update Booking" button in the update booking page with/without making updates | Redirection to book training page | Y | Available only to logged in users|
| 3          |  Click "cancel" button in the update booking page | updates booking and redirection to book training page | Y | Available only to logged in users|
|Delete Booking       |     |      |     |      |
| 1           |  Click "Delete" button in the newly created booking table in the booking page| Redirection to confirm deletion page | Y | Available only to logged in users |
| 2           |  Click "cancel" button in the confirm deletion page | Redirection back to book training page | Y | Available only to logged in users |
| 3           |  Click "Yes, delete it" button in the confirm deletion page | deletes booking and redirection to book training page| Available only to logged in users  |



| what|            |                  |      |             |
| 1           |  Change the form data for the first name, last name, or phone number | Date in the form will be updated | Y | Available only when the user opens his/her own profile  |
| 2           |  Click "cancel" button | Redirect back to user profile | Y |  Available only when the user opens his/her own profile |


---

## Testing User Story


| Site Developer Goals   | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a site developer, I want to set up both development and production environments, so that I can build and deploy a reliable Riders club website. | Website is reliable. | ![Navbar,home page](documentation/features/user_story_page/user_story_page.png) |


| Site User Goals    | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a site user, I want to register and log in to an account so that I can book club training sessions. | User can register, login and book training | ![Logged in Booked Training](documentation/features/user_story_page/user_story_page1.png) |
| As a logged-in site user, I want to create, view detail, update, and delete my booked trainings so that I can manage my training schedule effectively. | Manage booked training is working| ![Manage Booked Training](documentation/features/user_story_page/user_story_page2.png) |
| As a site user, I want to fill out and submit a contact form to express my interest in collaborating with the club, So that the club can review my request and get in touch with me for further communication. | Contact form is working | ![Contact form](documentation/features/user_story_page/user_story_page3.png) |


| Site Owner's Goals   | Requirement met | Image |
| ------------------------- | --------------- | ----- |
| As a site owner I can update home page so that I can make users to better understand the purpose of the club. | Update is working| ![Update home page information](documentation/features/user_story_page/user_story_page4.png) |
| As a site owner I can add information to contact page so that I can make it easier for users to reach site owner. | Update is working | ![Update contact page information](documentation/features/user_story_page/user_story_page5.png) |


---


## Bugs

### Known bugs

There is no known bug.

### Solved bugs

There were many bugs during the development and production process and some times, I just reset the database.

However, they were a few significant bugs:

- Bug: I mistakenly capitalised the first letter of one of my html files(Booking_detail.html). But the other links for same file was not first letter capitalised. It worked well without errors on windows browser but raised error on safari browser. The error was not fixed by changing the capitalised letter to a small letter.

Solution: I changed all related file links to capitalised first letter.

- Bug: 



---

## Validation:

### HTML Validation:

No errors or warnigs were found when passing through the official [W3C](https://validator.w3.org/) validator. This checking was done manually by copying the view page source code and pasting it into the validator.

- Home Page

![HTML Validation Report](documentation/validation/html_validation.png)

- Contact Page

![HTML Validation Report](documentation/validation/html_validation1.png)

- Book Training Page

![HTML Validation Report](documentation/validation/html_validation2.png)

- Login Page

![HTML Validation Report](documentation/validation/html_validation3.png)

- Logout Page

![HTML Validation Report](documentation/validation/html_validation4.png)

- Registration Page

![HTML Validation Report](documentation/validation/html_validation5.png)

- Create New Booking Page

![HTML Validation Report](documentation/validation/html_validation6.png)

- Booking Details Page

![HTML Validation Report](documentation/validation/html_validation7.png)

- Update Booking Page

![HTML Validation Report](documentation/validation/html_validation8.png)

- Confirm Deletion Page

![HTML Validation Report](documentation/validation/html_validation9.png)

- Contact Form Success Page

![HTML Validation Report](documentation/validation/html_validation11.png)


### CSS Validation:

![CSS Validation Report](documentation/validation/css_validation.png)

No errors or warnings were found when passing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_uri).


### Python Validation:

No errors or warnings were found when the code was passed through [PEP8CI](https://pep8ci.herokuapp.com/). This checking was done manually by copying python code and pasting it into the validator.

#### Riders club project

- settings.py

![Python Validation Report](documentation/validation/python_validation.png)

- urls.py

![Python Validation Report](documentation/validation/python_validation1.png)

- env.py

![Python Validation Report](documentation/validation/python_validation2.png)

#### Home applicatiom

- views.py

![Python Validation Report](documentation/validation/python_validation3.png)

#### Contact application

- admin.py

![Python Validation Report](documentation/validation/python_validation4.png)

- forms.py

![Python Validation Report](documentation/validation/python_validation5.png)

- models.py

![Python Validation Report](documentation/validation/python_validation6.png)

- urls.py

![Python Validation Report](documentation/validation/python_validation7.png)

- views.py

![Python Validation Report](documentation/validation/python_validation8.png)


#### Home applicatiom

- views.py

![Python Validation Report](documentation/validation/python_validation3.png)

#### Bookings application

- admin.py

![Python Validation Report](documentation/validation/python_validation14.png)

- forms.py

![Python Validation Report](documentation/validation/python_validation15.png)

- models.py

![Python Validation Report](documentation/validation/python_validation16.png)

- urls.py

![Python Validation Report](documentation/validation/python_validation17.png)

- views.py

![Python Validation Report](documentation/validation/python_validation18.png)


---


## Lighthouse Report


- Home Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report.png)

- Contact Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report1.png)

- Book Training Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report2.png)

- Login Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report3.png)

- Logout Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report4.png)

- Registration Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report5.png)

- Create New Booking Page
![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report6.png)

- Booking Details Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report7.png)

- Update Booking Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report8.png)

- Confirm Deletion Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report9.png)

- Contact Form Success Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report11.png)


---

## Compatibility

Testing was conducted on the following browsers;

- Safari;

![Compatibility Report](documentation/compatibility/compatibility.png)

- Chrome;

![Compatibility Report](documentation/compatibility/compatibility1.png)

- Firefox;

![Compatibility Report](documentation/compatibility/compatibility2.png)


---

# Responsiveness

The responsiveness was checked manually by using devtools (Chrome) throughout the whole development. It was also checked with [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en) Chrome extension.


- Home Page

<a>
<img src="documentation/responsiveness/iphone-14-proh.png" alt="Responsive Design iphone 14 pro" height="400">
<img src="documentation/responsiveness/iphone-14-pro-maxh.png" alt="Responsive Design iphone 14 pro max" height="400">
<img src="documentation/responsiveness/pixel-7-proh.png" alt="Responsive Design Pixel-7" height="400">
<img src="documentation/responsiveness/ipad-air-5h.png" alt="Responsive Design iPad-Air" height="400">
<img src="documentation/responsiveness/macbook-airh.png" alt="Responsive Design Mac Air" height="400">
</a>

- Contact Page

<a>
<img src="documentation/responsiveness/iphone-14-proc.png" alt="Responsive Design iphone 14 pro" height="400">
<img src="documentation/responsiveness/iphone-14-pro-maxc.png" alt="Responsive Design iphone 14 pro max" height="400">
<img src="documentation/responsiveness/pixel-7-proc.png" alt="Responsive Design Pixel-7" height="400">
<img src="documentation/responsiveness/ipad-air-5c.png" alt="Responsive Design iPad-Air" height="400">
<img src="documentation/responsiveness/macbook-airc.png" alt="Responsive Design Mac Air" height="400">
</a>

- Book Training Page

<a>
<img src="documentation/responsiveness/iphone-14-prob.png" alt="Responsive Design iphone 14 pro" height="400">
<img src="documentation/responsiveness/iphone-14-pro-maxb.png" alt="Responsive Design iphone 14 pro max" height="400">
<img src="documentation/responsiveness/pixel-7-prob.png" alt="Responsive Design Pixel-7" height="400">
<img src="documentation/responsiveness/ipad-air-5b.png" alt="Responsive Design iPad-Air" height="400">
<img src="documentation/responsiveness/macbook-airb.png" alt="Responsive Design Mac Air" height="400">
</a>

- Login Page

<a>
<img src="documentation/responsiveness/iphone-14-proi.png" alt="Responsive Design iphone 14 pro" height="400">
<img src="documentation/responsiveness/iphone-14-pro-maxi.png" alt="Responsive Design iphone 14 pro max" height="400">
<img src="documentation/responsiveness/pixel-7-proi.png" alt="Responsive Design Pixel-7" height="400">
<img src="documentation/responsiveness/ipad-air-5i.png" alt="Responsive Design iPad-Air" height="400">
<img src="documentation/responsiveness/macbook-airi.png" alt="Responsive Design Mac Air" height="400">
</a>

- Logout Page

<a>
<img src="documentation/responsiveness/iphone-14-proo.png" alt="Responsive Design iphone 14 pro" height="400">
<img src="documentation/responsiveness/iphone-14-pro-maxo.png" alt="Responsive Design iphone 14 pro max" height="400">
<img src="documentation/responsiveness/pixel-7-proo.png" alt="Responsive Design Pixel-7" height="400">
<img src="documentation/responsiveness/ipad-air-5o.png" alt="Responsive Design iPad-Air" height="400">
<img src="documentation/responsiveness/macbook-airo.png" alt="Responsive Design Mac Air" height="400">
</a>

- Registration Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report5.png)

- Create New Booking Page
![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report6.png)

- Booking Details Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report7.png)

- Update Booking Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report8.png)

- Confirm Deletion Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report9.png)

- Contact Form Success Page

![Lighthouse Report](documentation/lighthouse_reports/lighthouse_report11.png)


---