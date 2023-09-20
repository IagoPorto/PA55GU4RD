# \<PA55GU4RD\>

\*\*\*\* **WORK IN PROGRESS** \*\*\*\*

\<PA55GU4RD\> is a way to store your passwords securely. Users and passwords are stored hashed and passwords are stored with symmetric encryption using the AES-256 algorithm.

* [Getting started](#1-getting-started)
  * [Dependencies](#11-dependecies)
  * [Execution](#12-execution)
* [What will be in the future?](#2-what-will-be-in-the-future)

## 1. Getting Started

> **First and foremost, \<PA55GU4RD\>, is a program still under development, so there may be bugs and missing functionality.**

### 1.1 Dependecies

* cryptography
* bcrypto
* python-dotenv
* PyQt5

### 1.2 Execution

* To run the program, execute the main.py file (available in the backend folder) using the following command:

   ```shell
   python main.py
   ``````

* Create a new user and a new password.
* Now you can create a random password and save it securely for future reference.
  * To securely save passwords for future reference, you'll need to use a 32-character password for encryption, which will not be stored anywhere, ensuring that only you know it.
* You can change and delete the passwords.

## 2. What will be in the future?

In the future, <PA55GU4RD> will include the following enhancements:

* Database (DB) integration
* Invisible passwords. The ability to copy passwords without displaying them on the screen.
* User manager. Support for multiple users.
* Frontend development:
  * Android application
  * Linux/Windows application
* Secure conection between backend and frontend, featuring:
  * Asymmetric encryption using RSA algorithm
  * JWT (Jason Web token)
  * HTTPS
  * Possible WireGuard integration
