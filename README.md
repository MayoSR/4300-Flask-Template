# 4300-Flask-Template

## Summary

This is a template for **Professor Cristian Danescu-Niculescu-Mizil's CS/INFO 4300 class at Cornell University.**

You will use this template to directly add your Flask code, whose deployment you can control from http://4300showcase.infosci.cornell.edu:9090/#/login. 

## Authentication and Login

To access the dashboard above, you will need an account and password to sign in, which if you're part of the course has already been created for you. These accounts will later be suspended once you are allocated your teams, and new accounts will be provided.

Your current password is your **Net ID**. The application uses JWT to track your status and activity, so clearing localStorage could cause issues, in which case you will have to login again.

# Tutorial

## Working with the template

You can clone a copy of this repository directly and use it, or you can use the create template option that has been provided to you. Either way, you can put the repository anywhere with the constraint that it has to be **PUBLIC**. 

You will not be able to run this directly, unless you have **Docker**. 

### Running locally (Flask/Gunicorn only)

You can run the code more easily offline by just creating a Python3.7 virtual enviornment, and running it 

### Running locally with Docker (Not recommended)

> Generally, I would recommend you do not install or use Docker unless you have prior experience or expertise with it. Docker for desktop while an excellent service, is _very_ CPU and RAM intensive, and will either be too slow to run or cause a lot of lag, or both. If you still want to go ahead, try to have AT LEAST 8GB Ram and an Intel i5/Ryzen 5 for Windows, including having WSL2 installed or an M1/M2 Macbook. 

Ideally, once you form teams, at least one person on the team can run Docker on their laptop just for quick testing and development, however with the provided service this should not be required.
