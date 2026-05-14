from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.core.exception_handlers import (
    generic_exception_handler
)
from app.core.logging import setup_logging
from app.middleware.logging_middleware import (
    LoggingMiddleware
)
from app.middleware.request_id_middleware import (
    RequestIDMiddleware
)
from app.middleware.tenant_middleware import (
    TenantMiddleware
)

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

app.add_middleware(RequestIDMiddleware)
app.add_middleware(LoggingMiddleware)
app.add_middleware(TenantMiddleware)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX
)
