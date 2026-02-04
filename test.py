'''from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from scipy.sparse import hstack
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse
import requests

app=FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



model=joblib.load('model.joblib')
vectorizer=joblib.load('vectorizer.joblib')
scaler=joblib.load('scaler.joblib')

class PredictRequest(BaseModel):
    text: str


@app.post('/predict')
def predict(data: PredictRequest):
    #text_vec=vectorizer.transform([data.text])
    #rating_df = pd.DataFrame({"rating": [data.rating]})
    #rating_vec = scaler.transform(rating_df)
    #X = hstack([text_vec, rating_vec])
    #ai_prob = model.predict_proba(X)[0][1]
    return{
        'text': data.text
    }

        '''

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PageText(BaseModel):
    text: str

@app.post("/receive")
def receive_text(data: PageText):
    print("Received text length:", len(data.text))
    #print(data.text)
    word=data.text.split()
    for i in range(len(word)):
        #print(word[i], end=' ')
        if word[i]=='Top' and word[i+1]=='reviews' and word[i+2]=='from' and word[i+3]=='India':
            rating=word[i+6]
            print(f'rating {rating}')

            s=word[i+22]
            print(f'f word{s}')



    return {
        "length": len(data.text)
    }
