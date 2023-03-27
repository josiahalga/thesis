# Commands used for running YOLOv7

## Change Directory

```cmd
cd directory/of/yolo
```

## For Tracking Images
```cmd
python object-detection/yolo/detect.py --weights yolov7.pt --conf 0.25 --view-img --img-size 640 --source inference/images/horses.jpg --device 0
```

## For Tracking Videos
```cmd
python object-detection/yolo/detect.py --weights yolov7.pt --conf 0.25 --view-img --img-size 640 --source inference/images/horses.jpg --device 0
```

## Using webcam
```cmd
python object-detection/yolo/detect.py --weights yolov7.pt --conf 0.25 --img-size 640 --source 1 --device 0
```