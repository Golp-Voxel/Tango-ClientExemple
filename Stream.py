import tango
import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
import time

camara_device = tango.DeviceProxy("sys/tg_thorlabs/1")
print(camara_device.state())
camara_device.set_timeout_millis(9000)

camara_device.get_attribute_list()

# plt.figure()

# plt.imshow(camara_device.Image_foto)
# plt.show()  
# time.sleep(1)

 
# to run GUI event loop
plt.ion()
 
# here we are creating sub plots
figure = plt.figure()
plt.imshow(camara_device.Image_foto)
 
# setting title
plt.title("Stream", fontsize=12)
 
# setting x-axis label and y-axis label

 
# Loop
for _ in range(25):
    # creating new Y values 
    # updating data values
    
    plt.imshow(camara_device.Image_foto)
    # drawing updated values
    figure.canvas.draw()
 
    # This will run the GUI event
    # loop until all UI events
    # currently waiting have been processed
    figure.canvas.flush_events()
 
    #time.sleep(0.1)