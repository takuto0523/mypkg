import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class ListenerNode(Node):

        def __init__(self):
            super().__init__("listener")
            self.subscription = self.create_subscription(Int16, "countup", self.cb, 10)

        def cb(self, msg):
            self.get_logger().info("Listen: %d" % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = ListenerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

