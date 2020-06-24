# Precesion-Landing-Module-for-Drone  
[cv_bridge_test.py](cv_bridge_test.py) : To make sure CvBridge is installed properply and working fine  
[hsv_finder.py](hsv_finder.py) : To visualize image for various hsv limits  
[video.py](video.py) : Outputs live video feed from the drone camera in BGR format  
[object_detection.py](object_detection.py) : Detects objects based on color and creates a bounding box around them  
[cvpubpl.py](cvpubpl.py) : Creates bounding box around the largest contour (landing platform preferably) and publishes the midpoint coordinate to cvdrone.py  
[cvdrone.py](cvdrone.py) : Helps to control the drone to align camera center with midpoint subscribed from cvpubpl.py. Here p (proportional factor) controller to used to control the velocity.   
[camera.launch](camera.launch) : Makes webcam a rosnode such that any code written will work on gazebo as well    
[Ardupilot_Launcher_2.sh](Ardupilot_Launcher_2.sh) :Created a launcher that allows me to open gazebo simulator and run other required softwares easily    
[Trial_PL_using_p_controller](Trial_PL_using_p_controller) : Video of the trial in gazebo simulator. Clearly there is lot of noise and the landing is not smooth and this problem is addressed by using a PID controller instead of just p      
[cvdrone_pid.py](cvdrone_pid.py) : Controls the drone using a PID (Proportional Integral Derivative) Controller. More efficient and smoother landing than P controller.  
[PID.py](PID.py) : Python module for PID controller  
[pid_test.py](pid_test.py) : To test if the PID controller algorithm is working as expected  



