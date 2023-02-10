from fastapi import APIRouter

from routes import classroom_routes
from routes import students_routes
from routes import groups_routes

from main import app

app.include_router(classroom_routes.router)
app.include_router(groups_routes.router)
app.include_router(students_routes.router)