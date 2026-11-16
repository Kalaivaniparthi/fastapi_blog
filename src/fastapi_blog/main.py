from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

posts: list[dict] = [
    {"id": 1, 
    "title": "fast api is awesome", 
    "content": "This is the content of the first post."},
    {"id": 2, 
    "title": "python is great fordevelopment", 
    "content": "This is the content of the second post."},
]

@app.get("/", response_class=HTMLResponse ,include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse , include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1><p>{posts[0]['content']}</p>"

@app.get("/api/posts")
def get_posts():
    return posts