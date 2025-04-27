from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)

def initialize(db: Session) -> None:
    """
    Initialize the database with seed data if empty.
    """
    logger.info("Database initialization skipped for now.")
    # We'll implement this later when we have the API endpoints working
    pass