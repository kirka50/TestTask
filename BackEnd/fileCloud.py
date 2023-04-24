from typing import Annotated
from bdReq import *
from fastapi import FastAPI, File, UploadFile, Form, Header
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/uploadfile/")
async def create_upload_file(file: Annotated[UploadFile, File], filename: Annotated[str | None, Header] = None):
    file_location = f"fileStorage/{filename}"
    insertFileNames([[filename]])
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"info": f"file '{filename}' saved at '{file_location}'"}


@app.get("/listAll/")
async def list_all_files_names():
    data = showAllFileNames()
    return {"fileNames": data}


@app.get("/downloadFile/")
def download_file(file_name):
    return FileResponse(path=f"fileStorage/{file_name}", filename=file_name, media_type='multipart/form-data')


@app.get("/updateBase")
def update_base():
    updateTable()
