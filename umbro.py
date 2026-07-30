


from __future__ import annotations

import os

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from .api.routes.hardware import router as hardware_router
from .api.routes.health import router as health_router
from .api.routes.inference import router as inference_router
from .api.routes.memory import router as memory_router
from .api.routes.model import router as model_router
from .api.routes.runtime import router as runtime_router
from .api.routes.scheduler import router as scheduler_router
from .core.config import settings
from .core.logger import configure_logging
from .runtime.runtime_controller import RuntimeController
from .websocket.stream import chat_stream

configure_logging()

runtime_controller = RuntimeController()

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if "*" in settings.cors_origins else list(settings.cors_origins),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(hardware_router)
app.include_router(model_router)
app.include_router(inference_router)
app.include_router(runtime_router)
app.include_router(memory_router)
app.include_router(scheduler_router)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/ui/index.html")


_frontend = os.environ.get(
    "FRONTEND_DIR",
    os.path.join(os.path.dirname(__file__), "..", "..", "frontend")
)
if not os.path.isdir(_frontend):
    _frontend = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "frontend"))
if not os.path.isdir(_frontend):
    _frontend = "/app/frontend"
app.mount("/ui", StaticFiles(directory=_frontend), name="frontend")


@app.get("/pages/{page_name}", include_in_schema=False)
@app.get("/pages/{page_name}/", include_in_schema=False)
async def legacy_pages(page_name: str):
    return RedirectResponse(url=f"/ui/pages/{page_name}.html")


@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket) -> None:
    await chat_stream(websocket, runtime_controller)













