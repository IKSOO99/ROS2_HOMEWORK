import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32, Float64

class IcksuPublisher(Node):

    def __init__(self):
        super().__init__('icksu_publisher')
        self.publisher_ = self.create_publisher(String, 'icksu_topic_string', 10)
        self.publisher_int_ = self.create_publisher(Int32, 'icksu_topic_int', 10)
        self.publisher_float_ = self.create_publisher(Float64, 'icksu_topic_float', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello, I am Icksu'
        self.publisher_.publish(msg)

        msg_int = Int32()
        msg_int.data = 26
        self.publisher_int_.publish(msg_int)

        msg_float = Float64()
        msg_float.data = 1.999
        self.publisher_float_.publish(msg_float)

        self.get_logger().info('Publishing: "%s", %d, %f' % (msg.data, msg_int.data, msg_float.data))

def main(args=None):
    rclpy.init(args=args)
    icksu_publisher = IcksuPublisher()
    rclpy.spin(icksu_publisher)
    icksu_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
