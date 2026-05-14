from fastapi import APIRouter

from app.api.v1.auth.routes import router as auth_router
from app.api.v1.github.routes import router as github_router
from app.api.v1.health.routes import router as health_router
from app.api.v1.repositories.routes import (
    router as repository_router
)
from app.api.v1.users.routes import router as users_router
from app.api.v1.webhooks.github_routes import (
    router as webhook_router
)
from app.api.v1.reviews.routes import (
    router as reviews_router
)
from app.api.v1.scans.routes import (
    router as scans_router
)
from app.api.v1.observability.routes import (
    router as observability_router
)


api_router = APIRouter()

api_router.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

api_router.include_router(
    users_router,
    prefix="/users",
    tags=["Users"]
)

api_router.include_router(
    github_router,
    prefix="/github",
    tags=["GitHub"]
)

api_router.include_router(
    repository_router,
    prefix="/repositories",
    tags=["Repositories"]
)

api_router.include_router(
    webhook_router,
    prefix="/webhooks",
    tags=["Webhooks"]
)

api_router.include_router(
    scans_router,
    prefix="/scans",
    tags=["Scans"]
)

api_router.include_router(
    reviews_router,
    prefix="/reviews",
    tags=["Reviews"]
)
api_router.include_router(
    observability_router,
    prefix="/observability",
    tags=["Observability"]
)
