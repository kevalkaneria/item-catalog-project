# Item Catalog Project

An Udacity Full Stack Web Developer Nanodegree project developed by Keval Kaneria.

## About

This application provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit, and delete their own items.

This program uses third-party auth with Google. Some of the technologies used to build this application include Flask, Bootsrap, Jinja2, and SQLite.

## Features

- Proper authentication and authorization check.
- Full CRUD support using SQLAlchemy and Flask.
- JSON endpoints.
- Implements oAuth using Google Sign-in API.

## Skills used for this project

- Python
- HTML
- CSS
- Bootstrap
- Flask
- Jinja2
- SQLAchemy
- OAuth
- Google Login

## Steps to run this project

1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html).

2. Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).

3. Clone or download the Vagrant VM configuration file from [here](https://github.com/udacity/fullstack-nanodegree-vm).

4. Open the above directory and navigate to the `vagrant/` sub-directory.

5. Open terminal, and type

   ```bash
   vagrant up
   ```

   This will cause Vagrant to download the Ubuntu operating system and install it. This may take quite a while depending on how fast your Internet connection is.

6. After the above command succeeds, connect to the newly created VM by typing the following command:

   ```bash
   vagrant ssh
   ```

8. from the main directory run sudo pip install -r requirements

9. Type `cd /vagrant/` to navigate to the shared repository and
   Download or clone this repository, and navigate to it.

12. run application with `python application.py` from within its directory.

13. Open `http://localhost:8000/` in your favorite Web browser, and enjoy.
