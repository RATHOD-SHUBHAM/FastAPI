# pip install python-multipart
# Todo: Upload single file

from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post("/uploadfile")
def create_upload_file(file: UploadFile = File(...)):
    if not file:
        return {"message": "No upload file sent"}
    else:
        try:
            contents = file.file.read()
            file_path = f"/Users/shubhamrathod/PycharmProjects/fastAPI/fileUpload/uploadedImage/{file.filename}"
            with open(file_path, 'wb+') as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            file.file.close()

        # return {"message": f"Successfully uploaded {file.filename}"}

        return {"info": f"file '{file.filename}' saved at '{file_path}'"}


# todo:
# Read the File in chunks when the file is too big
from fastapi import File, UploadFile


@app.post("/uploadChunk")
def upload(file: UploadFile = File(...)):
    try:
        file_path = f"/Users/shubhamrathod/PycharmProjects/fastAPI/fileUpload/uploadedImage/{file.filename}"
        with open(file_path, 'wb') as f:
            while contents := file.file.read(1024 * 1024):
                f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}


# Todo: List of file
from fastapi import File, UploadFile
from typing import List

@app.post("/upload_multiFile")
def upload(files: List[UploadFile] = File(...)):
    for file in files:
        try:
            contents = file.file.read()

            file_path = f"/Users/shubhamrathod/PycharmProjects/fastAPI/fileUpload/uploadedImage/{file.filename}"

            with open(file_path, 'wb') as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()

    return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}