import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v5/yolov5-CAGSDL.yaml', task='detect')  # select your model.yaml path
    model.load('yolov5nu.pt') # loading pretrain weights
    model.train(data='dataset3/data.yaml',  # select your data.yaml path
                cache=False,
                imgsz=640,
                epochs=500,
                batch=16,
                patience=50,  # 早停的等待轮数
                # close_mosaic=10,
                workers=0,
                device='0',
                optimizer='SGD',  # using SGD
                resume='',  # last.pt path
                amp=False,  # close amp
                fraction=0.2,
                project='runs/train',
                name='yolov5-CAGSDL',
                )
