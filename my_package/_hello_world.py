from typing import List
from my_package._hello_base import HelloBase
from my_package._hello_std import HelloStandard


__all__: List[str] = ["hello_world"]


def hello_world(name: str = "World", printer: HelloBase = HelloStandard()) -> None:
    """
    Wishes a person/thing hello!

    Parameters
    ----------

    name: str, optional
        The person/thing you want to wish hello! Default is `"World"`.
    printer: `my_package.HelloBase`, optional
        A printer object to tell where to print the greetings. Uses the standard
        printer by default. See `my_package.HelloStandard`.

    Returns
    -------

    None

    Raises
    ------

    ValueError:
        If the name is anything other than a string. I can't wish
        Python objects hello!!!!!!!!!!!!!!!!!!!!!

    Notes
    -----

    The name must be a string.

    References
    ----------

    .. [1] Hello World Wikipedia, https://en.wikipedia.org/wiki/Hello_World
    """
    printer.printer(f"Hello, {name}!")
