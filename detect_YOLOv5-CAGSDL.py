import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/train/yolov5-CAGSDL/weights/best.pt') # select your model.pt path
    model.predict(source='dataset1/images/test',  # select your image path
                  imgsz=640,
                  project='runs/detect',
                  name='exp/yolov5-CAGSDL',
                  save=True,
                  conf=0.2,
                  visualize=False # visualize model features maps
                )