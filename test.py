from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Review(BaseModel):
    rating: Optional[str]
    title: Optional[str]
    body: Optional[str]
    date: Optional[str]

class ReviewPayload(BaseModel):
    reviews: List[Review]

@app.post("/receive")
def receive_reviews(data: ReviewPayload):
    print("✅ REQUEST RECEIVED")
    print("Total reviews:", len(data.reviews))

    for i, r in enumerate(data.reviews, 1):
        print(f"\nReview {i}")
        print("Rating:", r.rating)
        print("Title:", r.title)
        print("Body:", r.body)
        print("Date:", r.date)

    return {"ok": True, "count": len(data.reviews)}
