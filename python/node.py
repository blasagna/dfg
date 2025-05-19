from abc import ABC, abstractmethod
from attrs import define

@define
class Node(ABC):
    """Base compute node interface"""
    name: str

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