from imageai.Detection import VideoObjectDetection
import os
import cv2
# from matplotlib import pyplot as plt



def forMinute(minute_number, output_arrays, count_arrays, average_output_count):
    print("MINUTE : ", minute_number)
    print("Array for the outputs of each frame ", output_arrays)
    print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the last minute: ", average_output_count)
    print("------------END OF A MINUTE --------------")
#full
def forFull(output_arrays, count_arrays, average_output_count):
    print("Array for the outputs of each frame ", output_arrays)
    print("Array for output count for unique objects in each  frame : ", count_arrays)
    print("Output average count for unique objects in the entire video: ", average_output_count)
    print("------------END OF THE VIDEO --------------")


camera = cv2.VideoCapture(0)
detectormodel = VideoObjectDetection()
detectormodel.setModelTypeAsYOLOv3()
detectormodel.setModelPath(os.path.join(os.getcwd() , "yolo.h5"))
detectormodel.loadModel()
# plt.show()
video_path = detectormodel.detectObjectsFromVideo(camera_input=camera, output_file_path=os.path.join(os.getcwd(), "camera_detected_video"), frames_per_second=20, log_progress=True, 
                        minimum_percentage_probability=40, detection_timeout=20, per_minute_function=forMinute)




# output(plots)
resized=False
color_index={'person':'red'}
#once for frame function
def forFrame(frame_number, output_array, output_count, returned_frame):
    plt.clf()
    this_colors = []
    labels = []
    sizes = []
    counter = 0
    for eachItem in output_count:
        counter += 1
        labels.append(eachItem + " = " + str(output_count[eachItem]))
        sizes.append(output_count[eachItem])
        this_colors.append(color_index[eachItem])
    global resized
    if not resized:
        manager = plt.get_current_fig_manager()
        manager.resize(width=1000, height=500)
        resized = True
# plots ugh
    # plt.subplot(1, 2, 1)
    # plt.title("Frame : " + str(frame_number))
    # plt.axis("off")
    # plt.imshow(returned_frame, interpolation="none")
    # plt.subplot(1, 2, 2)
    # plt.title("Analysis: " + str(frame_number))
    # plt.pie(sizes, labels=labels, colors=this_colors, shadow=True, startangle=140, autopct="%1.1f%%")
    # plt.pause(0.01)
    # print(labels.count('person'))
#each min


