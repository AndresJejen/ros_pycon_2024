import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32MultiArray
from .model_pt.predict import predict


class ModelPredictorSubscriber(Node):

    def __init__(self):
        super().__init__('model_predictor_subscriber')
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'sensor_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data}')
        prediction = predict(msg.data)
        self.get_logger().info(f'Prediction: {prediction}')


def main(args=None):
    rclpy.init(args=args)

    model_predictor_subscriber = ModelPredictorSubscriber()

    rclpy.spin(model_predictor_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    model_predictor_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()