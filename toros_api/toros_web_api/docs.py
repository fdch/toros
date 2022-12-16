from fastapi import APIRouter
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html

router = APIRouter()


@router.get("/", tags=["documentation"])
async def swagger_documentation():
    """Creates the OpenAPI Docs

    Returns:
        OpenAPI Docs
    """
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Toros Web- OpenAPI Docs",
    )


@router.get("/redoc", tags=["documentation"])
async def redoc_documentation():
    """Creates the ReDoc Docs

    Returns:
        ReDoc Docs
    """
    return get_redoc_html(
        openapi_url="/openapi.json",
        title="Toros Web - ReDoc Docs",
    )
