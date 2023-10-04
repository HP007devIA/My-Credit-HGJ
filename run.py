from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


class Square(BaseModel):
    age : int

app = FastAPI(
    title= "Myfirst API",
    description="""
This is your description app, written in markdown code
# This is a title
* This is a bullet point
' This is a code block'
"""
)

n=None

# @app.get('/square')
# def square(n: int= None) -> int:
#     if n == None: return "Please enter a number"
#     else:return int(n)*int(n)

@app.post('/square')
def square(s:Square) -> str:
    if s.n == None: return "Please enter a number"
    else:return str(int(s.n)*int(s.n))

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)