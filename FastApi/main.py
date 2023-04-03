import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def pop(): 
    return('Hey Hello World')
@app.get('/welcome')
def name():
    return{'FastApi Tutorial'}
@app.get('/thanks')
def thanks(author : str):
    return{'Author': f'{author}'}
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

##uvicorn main:app --reload





