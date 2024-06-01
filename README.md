# Healthcare Pro W

Healthcare Pro W is a comprehensive healthcare management platform designed to streamline the processes for clinics and healthcare providers. It allows patients to manage their appointments, access their appointment history, and enables doctors to manage their schedules and patient interactions securely.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Files and Folders](#files-and-folders)
- [Manual Testing](#manual-testing)
- [Usage](#usage)
  
## Description
Healthcare Pro W is designed and developed to provide a robust platform for healthcare management. It leverages Django, HTML5, CSS3 (Bootstrap), and MySQL to offer a seamless experience for users. The platform includes robust authentication features and secure data management, ensuring that sensitive information is protected.

## Features
- **User Authentication and Authorization:** Secure login functionality using unique email and password combinations.
- **Patient Management:** Patients can view their appointment history and book appointments with registered doctors.
- **Doctor Management:** Doctors can view and manage their schedules and appointments.
- **Session-based Features:** Ensures that each doctor and patient can only view their own booking details or appointment schedules.
- **Responsive Design:** Built with HTML5 and CSS3 (Bootstrap) for a responsive and user-friendly interface.
- **Version Control:** Utilizes Git for version control, ensuring organized collaboration and tracking of changes.

## Technologies Used
- **Backend:** Python, Django, MySQL
- **Frontend:** HTML5, CSS3 (Bootstrap)
- **Template Engine:** Jinja2
- **Database Management:** Django ORM (Object Relational Mapper)

## Files and Folders
- **HealthcarePro/:**
  - `settings.py`: Contains project settings such as database configuration, installed apps, static files configuration, etc.
  - `urls.py`: Main URL configuration for the project, including routing to app-level URLs.
  
- **ClinicApp/ (Django App):**
  - `models.py`: Defines Django models for the application, including patients, doctors, appointments, etc.
  - `views.py`: Contains business logic for handling requests, rendering templates, processing forms, etc.
  - `urls.py`: App-level URL configuration for routing requests to appropriate view functions.
    
- **static/:** Folder containing CSS files, images, JavaScript, or other static assets used in the application.
  - `style.css`: Custom CSS styles for the application.
  - `images/`: Folder containing image assets used in the application.
    
- **templates/:** Folder containing HTML templates for rendering views and pages.
  - `base.html`: Base template containing common elements like header, footer, etc.
  - Other HTML files for specific pages or components.

## Manual Testing
- **Register a New Account:**
  - Open the application in your web browser.
  - Click on the "Register" link to create a new account.
  - Enter your details and submit the form.
  
- **Log In to Your Account:**
  - After registering, log in using your credentials.
  - Verify that you can successfully access your account dashboard.
  
- **Book an Appointment:**
  - In your account dashboard, navigate to the "Book Appointment" section.
  - Select a doctor and choose an available time slot.
  - Enter the necessary details and submit the form.
  
- **View Appointment History:**
  - Navigate to the "Appointment History" section to view past and upcoming appointments.

- **Doctor Schedule Management:**
  - Doctors can log in and navigate to the "Manage Schedule" section to view and manage their appointments.

## Usage
- **Run the Django development server:**
   ```bash
   python manage.py runserver
