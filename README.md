## Introduction

This repository contains the secure version of the application developed for the Cyber Security Base Project 1. The original application, which intentionally included five vulnerabilities from the OWASP Top 10 (2017) list as part of the course requirements, can be found in the [insecure version of the repository](https://github.com/LerkkaP/twitter-insecure).

In this secure version, all identified flaws have been addressed and mitigated, ensuring that the application adheres to secure coding practices.



## Requirements

- **Python**
- **Django**
> **_NOTE:_** Ensure JavaScript is enabled in your browser for proper functionality. If you encounter any issues, clearing your browser's cache usually resolves them.

## Installation guide


1. Clone this repository to your local machine

2. Navigate to the project root

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Populate database with seed data:

   ```bash
   python manage.py seed
   ```
   This creates the following accounts for testing purposes:

   ```bash
   username: ricky
   password: SunnyvaleKing2025
   ---------------------
   username: bubbles
   password: KittyLord99
   ```
   
5. Run the application and you're ready to go:

   ```bash
   python manage.py runserver
   ```

