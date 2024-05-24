import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32, Float64

class IcksuSubscriber(Node):

    def __init__(self):
        super().__init__('icksu_subscriber')
        self.subscription = self.create_subscription(
            String,
            'icksu_topic_string',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.subscription_int = self.create_subscription(
            Int32,
            'icksu_topic_int',
            self.listener_int_callback,
            10)
        self.subscription_int  # prevent unused variable warning

        self.subscription_float = self.create_subscription(
            Float64,
            'icksu_topic_float',
            self.listener_float_callback,
            10)
        self.subscription_float  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

    def listener_int_callback(self, msg):
        self.get_logger().info('I heard: "%d"' % msg.data)

    def listener_float_callback(self, msg):
        self.get_logger().info('I heard: "%f"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    icksu_subscriber = IcksuSubscriber()
    rclpy.spin(icksu_subscriber)
    icksu_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
