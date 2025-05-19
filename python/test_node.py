import unittest
from node import PassNode

class TestPassNode(unittest.TestCase):
    def test_pass_node(self):
        # Create a PassNode instance
        node = PassNode(name="test_pass_node")
        node.setup()
        
        # Define input data
        inputs = {"key1": "value1", "key2": 42, "key3": [1, 2, 3]}
        
        # Run the node
        outputs = node.run(inputs)
        
        # Assert that outputs match inputs
        self.assertEqual(outputs, inputs)

        node.teardown()

if __name__ == "__main__":
    unittest.main()