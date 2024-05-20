

 Xenization
Overview
Xenization(meaning):- Art of existing as a stranger


Xenization is a web application which tries to unite the old fashion of journaling with the new era of smart talking. Users can use it to pen down their thoughts, monitor their progress, review their day, and even communicate with a smart chatbot for help and feedback.




 Features


Inbuilt Journal: Log your daily thoughts and ideas with ease.
Smart Chatbot: Share experiences, ask questions, and get answers.
User Authentication: Authorization and account creation for individualization.
Responsive Design: Compatible with computers and smartphones and tablets.
Technologies Used
Frontend: HTML, CSS, Bootstrap
Backend: Django
Database: SQLite (default Django configuration)
Animations: Custom CSS animations for smooth user interactions
Getting Started
Prerequisites
Ensure you have the following installed on your local development environment:
Python 3.x
Django
pip (Python package installer)


Installation
Clone the repository:
git clone https://github.com/your-username/xenization.git
cd  myapp
     2. Create a virtual environment:
          	python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     3. Apply migrations:
	python manage.py migrate
     4. Create a superuser:
	python manage.py createsuperuser
     5. Run the development server:
python manage.py runserver	
Visit http://127.0.0.1:8000 in your browser to view the application.






Usage
Authentication
Login: Users can log in to access their personalised journaling space and chatbot.
Registration: New users can register to create an account and start using the application.
Journal
Create Note: Users can create new journal entries.
Edit Note: Users can edit existing entries.
Delete Note: Users can delete entries they no longer need.
Chatbot
Engage with the chatbot for advice, support, and insights directly within the app.
Customization
Fonts and Colours
You can customise the fonts and colours used in the application by editing the CSS in the static/css directory. The primary CSS file is:
static/css/styles.css




Adding New Features
To add new features, create new views, templates, and update URLs as necessary. Follow the Django framework's best practices for adding new models, views, and templates.


Contributing
Contributions are welcome! Please follow these steps to contribute:
Fork the repository.
Create a new branch for your feature: git checkout -b feature-name.
Commit your changes: git commit -m 'Add some feature'.
Push to the branch: git push origin feature-name.
Open a pull request.
Licence
This project is licensed under the MIT License. See the LICENCE file for details.
Acknowledgements
Icons from Font Awesome
Background images from Pinterest














