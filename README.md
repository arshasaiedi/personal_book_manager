# Personal Book Manager

![Static Badge](https://img.shields.io/badge/python-3.13-blue)

A simple book manager built with python

## Features
- Add multiple books
- Save books
- Display books
- Load Books
- Admin mode
- Set a priority (low, medium or high) for each book

## Book Priority

Every book has a name and a priority. The priority can be one of the following:

- low
- medium
- high

## Requirements
- Python
- python-dotenv

## Project Structure

```
personal_book_manager/
│   .env.example
│   .gitignore
│   books.py
│   main.py
│   README.md
│   requirements.txt
│
├───images/
│       Animation.gif
│       screenshot.png
```

## Instalation
Install the required packages
```bash
python -m pip install requirments.txt
```
## Environment setup
create a `.env` file in the project folder

Use `.env.example` as a template

Add your admin password

```env
BOOK_MANAGER_ADMIN_PASSWORD=your_password_here
```
Replace `your_password_here` with your own admin password

## Run The Program
Run the main file:
```bash
python main.py
```
## Screenshot
![perosnal_book_manager_screenshot](images/screenshot.png)

## Demo
![perosnal_book_manager_demo](images/Animation.gif)