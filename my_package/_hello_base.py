class HelloBase:
    """
    A base class for greeting people/things hello!

    Parameters
    ----------

    file: str, optional
        The file where the greeting will be logged. Logs to `"stdout"` be default.
    """

    def __init__(self, file: str = "stdout"):
        self.file = file

    def change_file(self, new_file: str):
        """
        Change the current file handle.

        Parameters
        ----------

        new_file: str
            The new file handle.
        """
        self.file = new_file

    def printer(self, name: str) -> None:
        """
        Greet hello to someone or something!

        Parameters
        ----------

        name: str
            The name of the person/thing to greet hello.

        Raises:
            NotImplementedError: If a printer isn't defined.
        """
        pass
