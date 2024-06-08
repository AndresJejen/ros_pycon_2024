mkdir -p ./ros2_ws/src
cd ./ros2_ws/src

# Test if works
ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name my_node my_package
colcon build
source install/local_setup.bash
ros2 run my_package my_node

# Basic package
ros2 pkg create --build-type ament_python --license Apache-2.0 py_pubsub
# Edit the code
rosdep install -i --from-path src --rosdistro humble -y
sudo rosdep init
rosdep update
colcon build --packages-select py_pubsub
source install/setup.bash
ros2 run py_pubsub talker
ros2 run py_pubsub listener

# More Complex system
sudo apt-get install python3-pip
ros2 pkg create --build-type ament_python --license Apache-2.0 py_model
# Edit the code
colcon build --packages-select py_model
source install/setup.bash
ros2 run py_model sensores
ros2 run py_model prediction

