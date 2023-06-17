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
python object-detection/yolo/detect.py --weights emergency_tiny_2.pt --conf 0.25 --view-img --img-size 640 --source data/testing/1_ambulance_2.mp4 --device 0
```

## For Multiple Videos
```cmd
python object-detection/yolo/detect.py --weights emergency_tiny_2.pt --conf 0.25 --view-img --img-size 640 --source streams.txt --device 0
```


## Using webcam
```cmd
python object-detection/yolo/detect.py --weights yolov7.pt --conf 0.25 --img-size 640 --source 1 --device 0
```

## For IP Camera
python object-detection/yolo/detect.py --weights yolo_tiny_freezing.pt --conf 0.25 --view-img --img-size 640 --source="rtsp://admin:Adha2023!@192.168.1.108/cam/realmonitor?channel=1&subtype=1" --device 0