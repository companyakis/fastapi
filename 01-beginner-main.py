# main.py

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"person": "mustafa buyukdereli"}

# run the live server
# uvicorn main:app --reload

# you should see 
# Uvicorn running on http://127.0.0.1:8000
# {"person": "mustafa buyukdereli}
# now go to http://127.0.0.1:8000/docs
