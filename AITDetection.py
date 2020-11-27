from imageai.Detection import VideoObjectDetection
import os
import cv2


def per_frame_function_DataGet(counting, output_objects_array, output_objects_count,detected_frame):

    for eachObject in output_objects_array:
        print(eachObject["name"])
		
    print("====================================================")
    
    detected_frame = cv2.cvtColor(detected_frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('getCamera',detected_frame)
	
	#ascii 27:key "ESC"
    if 27 ==cv2.waitKey(1):
	    exit()


#==========================================================================    

execution_path = os.getcwd()
camera = cv2.VideoCapture(1)

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel(detection_speed='fastest')
detector.detectObjectsFromVideo(camera_input=camera,
								save_detected_video=False,
						        frames_per_second=20, 
						        minimum_percentage_probability=60,
						        log_progress=False,
						        per_frame_function=per_frame_function_DataGet,
								return_detected_frame=True)
							
