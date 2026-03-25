import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class ResponderNode(Node):
    def __init__(self):
        super().__init__('responder_node')

        self.subscription = self.create_subscription(
            Int32,
            'palindrome_result',
            self.callback,
            10)

        self.publisher_ = self.create_publisher(String, 'final_reply', 10)

    def callback(self, msg):
        response = String()
        response.data = "Yes" if msg.data == 1 else "No"
        self.publisher_.publish(response)
        self.get_logger().info(f'Output: {response.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ResponderNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
