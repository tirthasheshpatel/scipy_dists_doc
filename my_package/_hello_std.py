from my_package._hello_base import HelloBase


class HelloStandard(HelloBase):
    """A simple class for printing the greetings on the terminal."""

    def printer(self, name: str) -> None:
        print(f"Hello, {name}")
