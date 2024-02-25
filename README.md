Prerequisites
pip install torch torchvision
pip install pillow
pip install yolov5

Object Detection with YOLOv5: The script utilizes the YOLOv5 model for object detection. It loads a pre-trained YOLOv5 model using the torch.hub.load() function from the ultralytics/yolov5 repository. This model is then used to perform object detection on an input image.

Detection Results Processing: After performing object detection, the script processes the detection results. It extracts information about each detected object, including its class label, confidence score, and bounding box coordinates. These details are stored in a list of dictionaries, with each dictionary representing a detected object.

Wikipedia URL Retrieval: For each detected object, the script attempts to find a corresponding Wikipedia page URL. It constructs a Wikipedia URL based on the object's class label (e.g., "car" or "person").

Redirect to Wikipedia: If a Wikipedia URL is found for a detected object, the script redirects the user's web browser to the corresponding Wikipedia page. This is achieved using the webbrowser.open() function.
