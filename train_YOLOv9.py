import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v9/yolov9t.yaml', task='detect')  # select your model.yaml path
    model.load('yolov9.pt') # loading pretrain weights
    model.train(data='dataset3/data.yaml', # select your data.yaml path
                cache=False,
                imgsz=640,
                epochs=10,
                batch=16,
                patience=10,  #早停的等待轮数
                close_mosaic=0,
                workers=16,
                device='0',
                optimizer='SGD', # using SGD
                resume='', # last.pt path
                amp=False, # close amp
                fraction=0.2,
                project='runs/train',
                name='YOLOv9',
                )
