from fastapi import FastAPI
app = FastAPI()

@app.get("/") #endpoint functio shoul be right away the funcyion defination
def home():
    return {"Data" : "Test"}

@app.get("/about")
def about():
    return {"Data" : "About"}
    