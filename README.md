# 4300-Flask-Template

## Summary

This is a template for **Professor Cristian Danescu-Niculescu-Mizil's CS/INFO 4300 class at Cornell University.**

You will use this template to directly add your Flask code, whose deployment you can control from http://4300showcase.infosci.cornell.edu:9090/#/login. 

## Authentication and Login

To access the dashboard above, you will need an account and password to sign in, which if you're part of the course has already been created for you. These accounts will later be suspended once you are allocated your teams, and new accounts will be provided.

Your current password is your **Net ID**. The application uses JWT to track your status and activity, so clearing localStorage could cause issues, in which case you will have to login again.

# Working with the template

You can clone a copy of this repository directly and use it, or you can use the create template option that has been provided to you. Either way, you can put the repository anywhere with the constraint that it has to be **PUBLIC**. 

You will not be able to run this directly, unless you have **Docker**. 

### Running locally (Flask/Gunicorn only)

You can run the code more easily offline by just creating a Python3.7 virtual enviornment, and running it 

### Running locally with Docker (Not recommended)

> Generally, I would recommend you do not install or use Docker unless you have prior experience or expertise with it. Docker for desktop while an excellent service, is _very_ CPU and RAM intensive, and will either be too slow to run or cause a lot of lag, or both. If you still want to go ahead, try to have AT LEAST 8GB Ram and an Intel i5/Ryzen 5 for Windows, including having WSL2 installed or an M1/M2 Macbook. 

Ideally, once you form teams, at least one person on the team can run Docker on their laptop just for quick testing and development, however with the provided service this should not be required.

# Tutorial

### Step 1: Login and basic setup

- Login to the dashboard at http://4300showcase.infosci.cornell.edu:9090/#/login using your NET_ID and password (also your NET_ID)
- When you login, ensure your dashboard has the following data filled from the image below (check the black arrows only)
  - If it's not filled, reload the page to check if that fixes it. If it doesn't, report it via Gmail or post on ED
- Clicking the URL should re-direct you, but since no deployments will be active, it won't do anything
- Your allocated port indicates on which port your flask service will be deployed

![4300showcase infosci cornell edu_9090_ (1)](https://user-images.githubusercontent.com/55399795/223569113-e820125e-29ff-4baa-8a01-3abf22668180.png)

### Step 2: Understanding the interface

- **BUILD**: Will re-clone and build everything from your GitHub repo, and only from the master/main branch. This is a hard reset, however your data will be preserved. This includes all data from your database and tables. 
- **START**: Containers not in use will typically be turned off. To reboot these containers **WITHOUT RE-BUILDING**, use this button. This will restart your code in the exact same state as you left it, and will not clone or pull any new changes or tamper with data.
- **STOP**: Will stop containers, but not delete them. STOP just turns off your container.
- **DESTROY**: Will destroy all your containers as well as remove any data associated with them. Useful for fresh boot from scratch
- **Container Information Table**: Will show you the status of all your containers. This should tell you if they are on/off. Generally this information is just useful for debugging and for checking any port errors or mismatches, although mostly just useful for TAs
- **Logs**: Should give you an idea of what went wrong during deployment. This of course will not tell you if something is broken during build time, but only what happened when your code was deployed. 

### Step 2: Cloning repo and API creation

- Leave the dashboard for a bit and clone the template from https://github.com/MayoSR/4300-Flask-Template as you see fit, and make your repo public
- In the backend folder, modify the app.py file to return "Hello, <your name/net_id>"
- Push the changes

### Step 3: Test deployment

- Back at the dashboard, in the provided search bar, add the URL of your template from your repository
- Click the **clone** button and wait for a bit, about a minute at most (As of now, there's no indication that deployment has succeeded, but that will be added soon)
- Click **build**, and wait for a minute. If all goes successfully, hitting the refresh button on the Container Information table and the logs tab will show the created data from the service. If this doesn't work, logout and log back in.
- Your URL should now work and display "Hello, <your name/net_id>"

### Step 4: Experiment a bit (optional)
- Create a new API that will fetch data from the DB
- Create a new database using the init.sql file
- Create a new table (either using SQLalchemy from within flask or from the init.sql file)
- Connect to the DB from Flask and return the data 

# General comments from the author (Mayank/ms3293/ms3293@cornell.edu)
- Since this project was made in the span of a few weeks, it is very likely things will break from time to time. If things do break, you can email me at the above email, although please do not email if you aren't sure if it's an actual bug or not. In those cases, post to ED first.
- If you would like to see stuff added to the dashboard you can send me an email at the above email and prefix the title with FEATURE REQUEST
- If you REALLY want to go above and beyond, you can make a request for a special Docker template. These will likely be turned down unless the project is exceptional, and you will have to be able to debug it yourself to ensure it works.
- You can ask for allocation of extra port numbers which will be approved or denied on a case by case basis.
- You can also email regarding any questions relating to the service itself. If you think things can be improved or some better logic can be implemented for certain portions, or even just want to know more about the project then feel free to do so.
