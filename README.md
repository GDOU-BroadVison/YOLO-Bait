# YOLO-Bait

本项目为论文“基于YOLO-Bait多尺度特征增强的养殖场景残饵检测方法”对应代码
如果项目对您的研究有帮助，请引用我们的文章：

[1]李振华，王骥，刘雯景，等. 基于YOLO-Bait多尺度特征增强的养殖场景残饵检测方法[J]. 农业工程学报，2026，42(10)：204-214. DOI:  10.11975/j.issn.1002-6819.202512049

LI Zhenhua, WANG Ji, LIU Wenjing, et al. Residual bait detection in aquaculture scenes based on YOLO-Bait with multi-scale feature enhancement[J]. Transactions of the Chinese Society of Agricultural Engineering (Transactions of the CSAE), 2026, 42(10): 204-214. DOI:  10.11975/j.issn.1002-6819.202512049


### Recommended Configuration
- python    3.11.5   
- torch   2.0.0+cu118 
- torchvision  0.15.1+cu118 

### Additional Packages Required
Install packages by yourself if they are not already installed
Recommended dependencies:
pip install timm thop efficientnet_pytorch einops grad-cam dill

## Details

（1）下载完本项目后请先解压ultralytics.zip

（2）本文提出的所有模块在文件ultralytics\nn\modules\conv.py与文件ultralytics\nn\modules\block.py中，请对照论文查看各功能模块。

## Training
（1）运行本文模型YOLO-Bait：[train_YOLO-Bait.py](https://github.com/GDOU-BroadVison/YOLO-Bait/train_YOLO-Bait.py) 

（2）运行现有残饵检测对比模型：

  YOLOv5-CAGSDL:   [train_YOLOv5-CAGSDL](https://github.com/GDOU-BroadVison/YOLO-Bait/train_YOLOv5-CAGSDL)  ；YOLO-feed: [train_YOLOv8-feed.py](https://github.com/GDOU-BroadVison/YOLO-Bait/train_YOLOv8-feed.py)  ；；YOLO-BaitScan : [train_YOLO-BaitScan.py](https://github.com/GDOU-BroadVison/YOLO-Bait/train_YOLO-BaitScan.py)

## Inference on Images
（1）运行本文模型YOLO-Bait：[detect_YOLO-Bait.py](https://github.com/GDOU-BroadVison/YOLO-Bait/detect_YOLO-Bait.py) 

（2）运行现有残饵检测对比模型：

  YOLOv5-CAGSDL:   [detect_YOLOv5-CAGSDL](https://github.com/GDOU-BroadVison/YOLO-Bait/detect_YOLOv5-CAGSDL)  ；YOLO-feed: [detect_YOLOv8_feed.py](https://github.com/GDOU-BroadVison/YOLO-Bait/detect_YOLOv8_feed.py)  ；；YOLO-BaitScan : [detect_YOLO-BaitScan.py](https://github.com/GDOU-BroadVison/YOLO-Bait/detect_YOLO-BaitScan.py)

## Copyright Notice
Many utility codes of our project are based on the codes from the [ultralytics](https://github.com/ultralytics/ultralytics) and [Gold-YOLO](https://github.com/huawei-noah/Efficient-Computing/tree/master/Detection/Gold-YOLO) repositories.
