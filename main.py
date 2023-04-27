from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token

class User(BaseModel):
    email:str 
    password:str
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=2, max_length=15)
    overview: str = Field(min_length=5, max_length=50)
    year: int = Field(le=2023)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=2, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripcion de la pelicula",
                "year": 2023,
                "rating": 7,
                "category": "Drama",
            }
        }




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
    },
]

## ROUTES
@app.get("/", tags=["home"], response_model=List[Movie], status_code=200)
def message():
    return HTMLResponse("<h1>Hello World </h1")

@app.post("/login", tags=["auth"] ,status_code=200)
def login(user: User):
    return user


@app.get("/movies", tags=["movies"], status_code=200)
def getMovies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)


@app.get("/movies/{id}", tags=["movies"], response_model=Movie)
def getMovie(id: int = Path(ge=1, le=2000)) -> Movie:
    for item in movies:
        if item["id"] == id:
            return JSONResponse(status_code=200 , content=item)
    return JSONResponse(status_code=400, content=[])


@app.get("/movies/", tags=["movies"], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    data = [item for item in movies if item["category"].lower() == category.lower()]
    return JSONResponse(content=data)


##CREATE Movie
@app.post("/movies", tags=["movies"], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(status_code=201, content={"message": "Se registró la película"})


##UPDATE Movie
@app.put("/movies/{id}", tags=["movies"], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    for element in movies:
        if element["id"] == id:
            element["title"] = movie.title
            element["overview"] = movie.overview
            element["year"] = movie.year
            element["rating"] = movie.rating
            element["category"] = movie.category
            return JSONResponse(
                status_code=200, content={"message": "Se modificó la película"}
            )


@app.delete("/movies/{id}", tags=["movies"], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return JSONResponse(
                status_code=200, content={"message": "Se eliminó la película"}
            )
