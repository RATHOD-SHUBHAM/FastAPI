from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO

# create a fastAPI instance
app = FastAPI()

# Load Model
model = YOLO("weights/yolov8x.pt")  # load a pretrained model (recommended for training)

def run_yolov8_detection(image):
    results = model.predict(source=image, save=True)
    return results

@app.post("/detect")
def detect(file: UploadFile = File(...)):
    if not file:
        return {"message": "No upload file sent"}
    else:
        try:
            contents = file.file.read()

            file_path = f"/Users/shubhamrathod/PycharmProjects/fastAPI/yolov8/input_image/{file.filename}"

            with open(file_path, 'wb+') as f:
                f.write(contents)

        except Exception:
            return {"message": "There was an error uploading the file"}

        finally:
            file.file.close()

        input_image = "/Users/shubhamrathod/PycharmProjects/fastAPI/yolov8/input_image/" + file.filename

        result = run_yolov8_detection(input_image)

        return {"result ": str(result)}

