# Equipment Maintenance History (Log)

# Goal
The goal of this project is to create a simple Python Web App using DJango. It enables a service technician to record an equipment status (in this example; temperature). Initially, the focus will be on developing basic functionality for logging status. Subsequent iterations will introduce features for logging delicate equipment parameters and preventative maintenance records.

# Current Status
As of now, the project is in the planning and early development stage. Basic code scaffolding and project structure are being set up.

The codes in this projects allow you to run a simple web app from your PC at 127.0.0.1:8000
You enter three parameters (Model, SN, and Temperature of the equipment).
Above data will be saved in SQLite which can be inspected by running "SELECT * FROM pm_form_app_formdata;" query.

# Installation
1- Clone the repository.
2- Install dependencies (See requirements.txt)

# Usage
1- In Visual Studio Code Program, Terminal Window, change directory to:
Your paython directory\service_department\pm_form_project
2- Run:
python manage.py runserver
3- Open a webbrowser and load:
http://127.0.0.1:8000
4- Let's assume you want to log these parameters.
Enter Model, Serial Number and Temperature.
5- Press Submit Button.
6- Go to your Visual Studio Code Program, Terminal Window.
7- Press CTRL-C to exit the server.
8- Check the sqlite to confirm your data has been recorded. In Terminal Window type:
python manage.py dbshell
9- From sqlite> prompt type:
SELECT * FROM pm_form_app_formdata;
press Enter.
10- You should be able to see the Model, SN, and the Temperature you entered in the web browser.
11- to exit from sqlite shell, type:
.quit
followed by Enter.

# Keywords
Service - Maintenance - Troubleshooting - Scheduled Maintenance Records - Problem Solving - Preventative Maintenance - PM
