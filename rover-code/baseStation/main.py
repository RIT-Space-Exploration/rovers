from http.client import OK
import uvicorn
from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), "static")


@app.get("/data")
def test_data():
    return {"message": "hello"}

# @app.options("/data")
# def test_data_options():
#     # print(options)
#     return '<div>Got Data</div>'


if __name__ == "__main__":
    uvicorn.serve(app)
