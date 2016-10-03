#Project AL5D  
1. connect the arm and PC using Bluetooth  
2. move the arm by Python commands  
3. create ros package "al5d"  
 echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc  
 source ~/.bashrc  
4. simulation model in rviz  
 roscd al5d  
 cd src/urdf  
 roslaunch urdf_tutorial display.launch model:=sample.urdf gui:=True  

