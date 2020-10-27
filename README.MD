# RBE 3002 Turtlebot3 ROS Package
The purpose of this package is to modify parts of the Turtlebot3 for educational purposes for WPI's RBE 3002 class. Information on how to run the changes are documented below.

## Using this package
Clone this repository in your catkin source directory. If your catkin workspace is in your home directory and your workspace is named `catkin_ws`, you can use the following commands:
``` bash
cd ~/catkin_ws/src
git clone https://github.com/WPIRoboticsEngineering/RBE3002-Turtlebot.git rbe3002-turtlebot
```
To launch the RBE 3002 turtlebot see the `Launching RBE3002 Turtlebot in a World` section below

## Launching RBE3002 Turtlebot in a World
The launch file will default to an empty world, but you can change the world used using the `world_name` argument in the launch file. Below is how you can run the launch file in its default configuration.

```bash
roslaunch rbe3002-turtlebot turtlebot3002_world.launch
```