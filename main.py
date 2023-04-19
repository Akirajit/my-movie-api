from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi aplicación con fastAPI"
app.version = "0.0.1"

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
        {
        "id": 2,
        "title": "Titanic",
        "overview": "La historia de un barco que se hundió XD",
        "year": "2009",
        "rating": 7.0,
        "category": "Drama",
    }

]


@app.get("/", tags=["home"])
def message():
    return HTMLResponse('<h1>Hello World </h1')


@app.get("/movies", tags=["movies"])
def getMovies():
    return movies

@app.get("/movies/{id}" , tags=["movies"])
def getMovie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get("/movies/", tags=["movies"])
def getMoviesByCategory(category:  str):
    result = []
    for movie in movies:
        if movie['category'].lower() == category.lower():
            result.append(movie)
    return result