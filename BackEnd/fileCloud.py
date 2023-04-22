from typing import Annotated
from bdReq import *
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()
con = createConnection()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    file_location = f"fileStorage/{file.filename}"
    insertFileNames(con, (file_location))
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}


@app.get("/listAll/")
async def list_all_files_names():
    data = showAllFileNames(con)
    return {"fileNames": data}


@app.get("/downloadFile/{file_name}")
def download_file(file_name):
  return FileResponse(path=f"fileStorage/{file_name}", filename=file_name, media_type='multipart/form-data')