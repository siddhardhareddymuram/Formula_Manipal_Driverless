import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker_node')
        self.publisher_ = self.create_publisher(String, 'input_text', 10)
        self.timer = self.create_timer(2.0, self.publish_text)

    def publish_text(self):
        user_input = input("Enter string: ")
        msg = String()
        msg.data = user_input
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {user_input}')

def main(args=None):
    rclpy.init(args=args)
    node = TalkerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
