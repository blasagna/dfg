from abc import ABC, abstractmethod

class Node(ABC):
    """Base compute node interface"""

    def __init__(self, name: str):
        """Initialize a node instance with a unique name"""
        self.name = name

    @abstractmethod
    def run(self, inputs: dict[str, object]) -> dict[str, object]:
        """Run some computation. Inputs and outputs are names by dict keys."""
        ...
    
    def setup(self) -> None:
        """Setup invoked once. Raise an exception to communicate errors."""
        pass

    def teardown(self) -> None:
        """Teardown invoked once. Raise an exception to communicate errors."""
        pass


class PassNode(Node):
    def run(self, inputs: dict[str, object]) -> dict[str, object]:
        return inputs