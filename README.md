![Alt text](<Screenshot 2023-09-12 134219.png>)
# RecipeMuse
This is a portfolio project to build a Recipe Web Application using Python and Flask

## Introduction
Welcome to the README of RecipeMuse. This project is designed to provide a high level description of the project's purpose whether you are a developer, designer or just someone interested in recipes. This project offers the ability to search, save and organize recipes. 

You can find the deployed project at http://web-01.becky1703.tech

Here is a blog post on LinkedIn talking about how the project came about and challlenges faced (http://)

Now let's talk about how to get started.

## Table of Contents
> Installation
   - Prerequisites
   - Installation Steps
> Usage
   - Example 1: Basic usage
   - Example 2: Basic usage
> Contributing
   - Getting started
   - Contributing Guidelines
   - Pull Request Template
   - Code of Conduct
> Related projects

> License

## Installation 

### Prerequisites
Before you begin, make sure you meet the following requirements.
```python
Python(v3.8 or higher)
```
Use the package manager [pip]
(https://pip.pypa.io/en/stable/) to install the following .

```bash
pip install flask
pip install flask_login
pip install flask_sqlalchemy
pip install requests
```
## Installation Guide
1. Clone the repository
```bash
git clone https://github.com/Becky1703/RecipeMuse.git
cd RecipeMuse
```
2. Set up a virtual environment(Optional but Recommended)
```bash
pip install virtualenv
```
Then, create a virtual environment

```bash
virtualenv myprojectenv
```

On Windows:
```bash
myprojectenv\Scripts\activate
```

On macOS/Linux:
```bash
source myprojectenv/bin/activate
```
3. Install Python Dependencies
Install the required python packages from the 'requirements.txt' file:
```bash
pip install -r requirements.txt
```
4. Run the application
You can run the flask application with:
```bash
python run.py
```

## Usage

1. Start the apllication
To run the Flask application, make sure you have followed the installation guide above. If you have not, please refer to the 'Installation Guide'.

After setting up your environment, naviagate to your project's root directory and execute the following command.

```bash
python run.py
```
This will start the application in a Flask development server and the application will be accessible locally at http://localhost:5009 in your browser or you can change the port to the default port 5000 in run.py file.

2. Access the Web Application.
Open your browser and enter the following URL to access the application:
```arduino
http://localhost:5009
```
You should see the welcome page of the flask application.

3. Explore the Application

Welcome page: The first route in the application / displays a welcome page with buttons that gives a user the option to either explore the application or create an account.

User Registration: If a user chooses to create an account, then they access the /register route. The user is asked to provide a username, password(and password confirmation)
and email.

User Login: Once a user is logged in, the user is redirected to a /login route where the user enters the previously created email and password.

Interact with features:
Searching - A user can search for a recipes that will be fecthed from the Spoonacular API and displayed in their browser.

Saving - When a user searches for a recipe and it is displayed, the user can view the details of the recipe which includes the ingredients and instructions for making the meal. At the bottom of the page, the user has an option to save the recipe and if the user has not registered/logged in before, they are prompted to do so.

## Troubleshooting
One likely issue that might occur while using the application is port conflict. Make sure to check if the port is in use by another application or service. You can do this by running
```bash
sudo lsof -i :<port number>
```
You should also check firewall rules
```bash
ufw status
```
If the port is blocked, make sure you allow the firewall rule for that port
```bash
ufw allow <port number>
```

## Contributing
Pull requests are welcome. For major changes, make sure you follow the following guidelines.

Description: [A brief description of the change]

Justification: [Explain why this change is necessary or beneficial]

Related issues: [List any related issues or pull requests ]

## Related Projects
Explore other projects and resoources related to RecipeMuse:

Related Project 1: A Recipe App for Mobile made with Flutter https://github.com/gerfagerfa/recipe

Related Project 2: A Recipe App

## Authors

> Rebecca Adelaja 
  email: <oluwabukunmia@gmail.com>
  linkedin: <>

## About Me
I am a lawyer and food business owner turned dedicated software engineer with a fervour for creating meaningful and user-friendly applications. RecipeMuse is just a precursor to what the future holds, and I'm eagerly anticipating the exciting adventures that technology has in store.  Here are links to my:

Deployed project: http://web-01.becky1703.tech

Landing page:https://myrecipemuse.mailchimpsites.com/

## License
[MIT](https://choosealicense.com/licenses/mit/)


