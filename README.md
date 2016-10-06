#Project AL5D @ University of Salento
・ install ROS package al5d  
```bash
student@vaio:~$ cd ~/catkin_ws/src
student@vaio:~$ git clone https://github.com/TakakiNishio/al5d.git al5d
student@vaio:~$ rosmake al5d
student@vaio:~$ cd .. && catkin_make
```
```bash
student@vaio:~$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
student@vaio:~$ source ~/.bashrc
```

・ connect the arm and PC using Bluetooth (see README.md @ directory: al5d/src/python)    

・ move the arm by Python commands (see README.md @ directory: al5d/src/python)    

・ move the arm by Python scripts (see README.md @ directory: al5d/src/python)    

・ simulate the arm in rviz and move the arm with simulation (see README.md @ directory: al5d/src/python)    

