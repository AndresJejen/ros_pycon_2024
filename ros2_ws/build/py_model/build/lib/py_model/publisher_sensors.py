import rclpy
import random
from rclpy.node import Node

from std_msgs.msg import Float32MultiArray


class SensorPublisher(Node):

    def __init__(self):
        super().__init__('sensor_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'sensor_topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.value = [float(0) for _ in range(3)]

    def timer_callback(self):
        msg = Float32MultiArray()
        msg.data = self.value
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing sensor info now: {msg.data}")
        self.value = [float(random.random()) for _ in self.value]


def main(args=None):
    rclpy.init(args=args)

    sensor_publisher = SensorPublisher()

    rclpy.spin(sensor_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    sensor_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()