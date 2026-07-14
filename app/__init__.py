from sanic import Sanic
from sanic.response import json

from app.config import settings
from app.db import engine


def create_app() -> Sanic:
    app = Sanic("PythonVacancy")
    app.config.FALLBACK_ERROR_FORMAT = "json"
    app.ctx.settings = settings

    @app.get("/health")
    async def health(request):
        return json({"status": "ok"})

    @app.after_server_stop
    async def on_stop(app, loop):
        await engine.dispose()

    return app
