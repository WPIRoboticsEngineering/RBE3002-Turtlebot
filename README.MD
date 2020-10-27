# RBE 3002 Turtlebot3 ROS Package
The purpose of this package is to modify parts of the Turtlebot3 for educational purposes for WPI's RBE 3002 class. Information on how to run the changes are documented below.

## Launching a World
The launch file will default to an empty world, but you can change the world used using the `offset` argument in the launch file. Below is how you can run the launch file in its default configuration.

```bash
roslaunch rbe3002-turtlebot turtlebot3002_world.launch
```