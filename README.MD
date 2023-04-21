## Practicing FastAPI

Currently under construction ... 🚧

## Installation instructions

- Download Python (https://www.python.org/)
- Clone the repo
- Create a virtual environment , and then activate it:
```bash
python -m venv venv
\venv\scripts\activate
```

- Install the dependencies:
```bash
pip install -r requirements.txt
```
- run 'uvicorn' localhost web server:
```bash
uvicorn main:app --reload
```
- Open your web browser and navigate to http://127.0.0.1:8000/docs