"""
created by Nagaj at 06/07/2021
"""
import uvicorn
from fastapi import FastAPI
from app.api.v1.api import api_router, api_root
from app import config


def create_app(conf):
    """ Factory function for creating an application """
    app = FastAPI(
        title=conf.PROJECT_NAME,
        version="0.0.1",
        openapi_url=conf.OPENAPI_URL,
        docs_url="/docs",
    )
    register_routers(app, conf)
    return app


def register_routers(app, conf):
    """ A place for mounting routers to the application """
    app.include_router(api_root)
    app.include_router(api_router, prefix=conf.API_V1_STR)  # API_V1_STR = "/api/v1"


application = create_app(config)
if __name__ == "__main__":

    uvicorn.run("main:application", port=config.PORT, reload=True)
