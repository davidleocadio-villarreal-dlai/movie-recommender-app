from typing import Optional, Literal
from pydantic import BaseModel, Field


class MovieRecommendation(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    genre: Literal["action", "comedy", "drama", "sci-fi", "thriller", "horror", "romance"]
    year: int = Field(..., ge=1900, le=2025)
    rating: float = Field(..., ge=0.0, le=10.0)
    synopsis: str = Field(..., min_length=10, max_length=500)
    director: Optional[str] = None
    lead_actor: Optional[str] = None
    recommended_for: Optional[Literal["family", "adults", "teens"]] = None
