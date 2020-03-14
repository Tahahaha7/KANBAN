# KANBAN
## Description of Application
A web application of a simple Kanban board designed to organize tasks in three categories (To do, In progress, Done). Each task can be moved through the three categories or deleted at any stage.  
An example of the layout of the web application:  

![Github](https://github.com/Tahahaha7/KANBAN/blob/master/kanban_view.png)

## Setting Up Virtual Environment
### Create a Virtual Environment

```bash
$ python -m venv .venv
$ source venv/bin/activate
```

## Installing Dependencies

```bash
$ pip install -r requirements.txt 
```

## Running the application

```bash
$ python3 run.py
```

## Testing 
To run the unit tests, be sure to run the following command and the project directory:

```bash
$ python3 -m unittest discover test
```

## Project Structure

```bash
Directory/KANBAN
├── project/
│   ├── __init__.py
│   ├── routes.py
│   ├── app.sqlite
│   ├── templates/
│   │   └── index.html
├── requirements.txt
├── run.py
├── test.py
└── venv/
```
