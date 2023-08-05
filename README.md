# \<PA55GU4RD\>

\*\*\*\* WORK IN PROGRESS \*\*\*\*

\<PA55GU4RD\> is a way to store your passwords securely. Users and passwords are stored hashed and passwords are stored with symmetric encryption using the AES-256 algorithm.

* [Getting started](#1-getting-started)
  * [Dependencies](#11-dependecies)
  * [Execution](#12-execution)
* [What will be in the future?](#2-what-will-be-in-the-future)

## 1. Getting Started

**First of all, \<PA55GU4RD\>, is a program still under development. There are bugs and missing functionality.**

### 1.1 Dependecies

* cryptography
* bcrypto
* python-dotenv
* PyQt5

### 1.2 Execution

* Execute the main.py file (available in the backend folder)

   ```shell
   python main.py
   ``````

* Create a new user and a new password.
* Now you can create a random password and save it securely for future reference.
  * You need to use a 32-character password to encrypt your other passwords, which will not be stored anywhere, and only you can know it.
* You can change and delete the passwords.

## 2. What will be in the future?

* DB
* Invisible passwords. You will be able to copy the password without it being displayed on the screen.
* User manager. Now only one user is allowed, but in the future it will be possible to have more.
* Frontend
  * Android application
  * Linux/Windows application
* Secure conection between backend and frontend.
  * Asymmetric encryption using RSA algorithm
  * JWT
  * HTTPS
  * ¿WireGuard?
