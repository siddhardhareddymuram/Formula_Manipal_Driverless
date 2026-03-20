import rclpy
from rclpy.node import Node
from taskone_msgs.msg import TaskOne

class Publisher(Node):
    def __init__(self):
        super().__init__('taskone_publisher')
        self.pub = self.create_publisher(TaskOne, '/taskone', 10)

    def send_data(self):
        msg = TaskOne()

        msg.ang_vel = float(input("Enter angular velocity: "))
        msg.radius = float(input("Enter radius: "))

        self.pub.publish(msg)
        self.get_logger().info(f"Published: {msg.ang_vel}, {msg.radius}")

def main():
    rclpy.init()
    node = Publisher()

    while True:
        node.send_data()
