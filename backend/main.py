from fastapi import FastAPI
import uvicorn

klu = FastAPI(title="AI Tutor",
              description="AI Tutor PBL Project",
              version="1.0.0")


@klu.get("/")
def home():
    return {"message":"welcome to AI Tutor Project"}

@klu.get("/demo")
def demo():
    return{"message":"KL University"}

@klu.get("/askquestion")
def ask():
    return{"message":"what is LLM","Answer":"Large Language Model"}

@klu.get("/student")
def student():
    return {"id":1,"name":"Ram","gender":"Male","courses":"DSA"}

@klu.get("/students")
def getstudents():
    return [
            {"id":1,"name":"Ram","gender":"Male","courses":"DSA"},
            {"id":2,"name":"Sita","gender":"Female","courses":"OS"},
            {"id":3,"name":"Gita","gender":"Female","courses":"DBMS"}
            ]
if __name__ == "__main__":
    uvicorn.run("main:klu", host="127.0.0.1", port=2027,reload=True)