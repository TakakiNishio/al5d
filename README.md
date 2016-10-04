#Project AL5D  
1. install ROS package al5d  
```bash
cd ~/catkin_ws/src
git clone https://github.com/TakakiNishio/al5d.git al5d
rosmake al5d
cd .. && catkin_make
```
```bash
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

1. connect the arm and PC using Bluetooth (see README.md @ directory: al5d/src/python)    

2. move the arm by Python commands (see README.md @ directory: al5d/src/python)    

4. simulation model in rviz    
```bash
roscd al5d
cd src/urdf
roslaunch urdf_tutorial display.launch model:=al5d.urdf gui:=True
```

