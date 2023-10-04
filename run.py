from fastapi import FastAPI
import uvicorn

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

@app.get('/square')
def square(n: int= None) -> int:
    if n == None: return "Please enter a number"
    else:return int(n)*int(n)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)