from fastapi import APIRouter, HTTPException
from model.predict import NextWordPredictor

router = APIRouter()
predictor = NextWordPredictor("model/next_word_model.h5", "model/tokenizer.pkl")
 
@router.post("/predict/")
def predict_next_word(text: str):
    try:
        next_word = predictor.predict(text)
        return {"input": text, "next_word": next_word}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
