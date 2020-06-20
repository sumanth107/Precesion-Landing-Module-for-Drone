#!/bin/sh
#Ardupilot Launcher

echo "	welcome "
echo " Running roscore"
	xterm -title "roscore" -hold -e "roscore" &
        pid6=$!

echo "DO YOU WANT TO LAUNCH SITL TERMINAL [y/n]"
read input 
if [ $input = 'y' ] ; then
	xterm -title "SITL" -hold -e "sim_vehicle.py -v ArduCopter -f gazebo-iris  -m --mav10 --map --console -I0" &
        pid5=$!
fi

echo "DO YOU WANT TO LAUNCH GAZEBO TERMINAL [y/n]"
read input 
if [ "$input" = "y" ] ; then
	xterm -title "GAZEBO" -hold -e "cd ~/catkin_ws/ && source devel/setup.zsh && roslaunch iq_sim runway.launch" &
        pid4=$!
fi

echo "DO YOU WANT TO LAUNCH MAVROS TERMINAL [y/n]"
read input 
if [ $input = 'y' ] ; then
	xterm -title "MAVROS" -hold -e 'cd ~/catkin_ws/ && source devel/setup.zsh && roslaunch iq_sim apm.launch' &
        pid3=$!
fi

echo "DO YOU WANT TO LAUNCH QGROUND [y/n]"
read input
if [ $input = 'y' ]; then
	xterm -title "QGC" -hold -e "./QGroundControl.AppImage" &
        pid2=$!
fi

echo "DO YOU WANT TO Close All Terminals [y/n] "
read input 
if [ $input = 'y' ] ; then
		kill -9 $pid2
        kill -9 $pid3
        kill -2 $pid5
        kill -9 $pid6
fi
echo end 

