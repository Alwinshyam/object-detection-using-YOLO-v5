import torch
from PIL import Image
import requests
from io import BytesIO
import webbrowser

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_objects(image_path):
    
    img = Image.open(image_path)

    
    results = model(img)

   
    detected_objects = []
    for obj in results.xyxy[0]:
        class_name = model.names[int(obj[5])]
        confidence = obj[4]
        bbox = obj[:4]
        detected_objects.append({'class': class_name, 'confidence': confidence, 'bbox': bbox})

    return detected_objects


def find_wikipedia_url(object_name):

    return f"https://en.wikipedia.org/wiki/{object_name}"


def redirect_to_wikipedia(url):
    webbrowser.open(url)


def main(image_path):
    
    detected_objects = detect_objects(image_path)

    
    for obj in detected_objects:
        object_name = obj['class']
        object_confidence = obj['confidence']
        object_bbox = obj['bbox']

        
        wikipedia_url = find_wikipedia_url(object_name)

       
        if wikipedia_url:
            print(f"Object: {object_name}, Confidence: {object_confidence}, Wikipedia URL: {wikipedia_url}")
            redirect_to_wikipedia(wikipedia_url)
        else:
            print(f"Object: {object_name}, Confidence: {object_confidence}, Wikipedia URL not found")

if __name__ == "__main__":
    image_path = ""#image path  
    main(image_path)
