from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

# Initialize FastAPI app
app = FastAPI(
    title="ElementSim",
    description="Medieval Chemistry & Crafting Simulation API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
# We'll uncomment this later when we have API endpoints
# from app.api.v1.api import api_router
# app.include_router(api_router, prefix=settings.API_V1_STR)

# We'll implement this initialization function later
# @app.on_event("startup")
# async def initialize_data():
#     db = next(get_db())
#     try:
#         init_db.initialize(db)
#     finally:
#         db.close()

@app.get("/")
async def root():
    """
    Root endpoint - provides basic information about the API
    """
    return {
        "name": "ElementSim",
        "description": "Medieval Chemistry & Crafting Simulation API",
        "version": "0.1.0",
        "docs": "/docs",
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring
    """
    return {"status": "healthy"}