#Initialize the project of python with FastAPI

Define environment for development, recommendation (.environment-psql-python)
Example: ```python -m  venv .environment-psql-python```
Initialize in environment:
Example: ```.\.environment-psql-python\Scripts\activate```
Install dependencies:
```pip install -r requirements.txt```
Run API 
```fastapi dev app/main.py```
#Show in project endpoints test 
Use ```http://127.0.0.1:8000/docs``` in development