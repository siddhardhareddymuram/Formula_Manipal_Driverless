import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32

class CheckerNode(Node):
    def __init__(self):
        super().__init__('checker_node')

        self.subscription = self.create_subscription(
            String,
            'input_text',
            self.callback,
            10)

        self.publisher_ = self.create_publisher(Int32, 'palindrome_result', 10)

    def is_palindrome(self, s):
        return s == s[::-1]

    def callback(self, msg):
        result = Int32()
        result.data = 1 if self.is_palindrome(msg.data) else 0
        self.publisher_.publish(result)
        self.get_logger().info(f'Checked: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = CheckerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
