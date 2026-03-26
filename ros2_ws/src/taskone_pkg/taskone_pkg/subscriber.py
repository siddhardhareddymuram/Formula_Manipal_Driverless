import rclpy
from rclpy.node import Node
from taskone_msgs.msg import TaskOne

class Subscriber(Node):
    def __init__(self):
        super().__init__('taskone_subscriber')
        self.sub = self.create_subscription(
            TaskOne,
            '/taskone',
            self.callback,
            10
        )

    def callback(self, msg):
        speed = msg.ang_vel * msg.radius
        self.get_logger().info(f"Speed = {speed}")

def main():
    rclpy.init()
    node = Subscriber()
    rclpy.spin(node)
