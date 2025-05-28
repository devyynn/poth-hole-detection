from ultralytics import YOLO

# Load the trained model from the current directory
model = YOLO('best.pt')

# Path to the image or directory for prediction
source = 'data/images/'  # Change this to your image or folder

# Run inference and save results
results = model.predict(source=source, save=True, imgsz=640, conf=0.25)

print("Inference complete. Results saved in 'runs/segment/predict'.")
