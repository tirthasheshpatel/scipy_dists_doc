"""
=======================================================
Hello World: A Python library for greeting people hello
=======================================================

A library to greet your friends and family a hello!

Usecases:

* Wanna wish your friends hello? You got it!
* Wanna wish a family member hello? You got it!
* Wanna wish a stranger hello? YOU GOT IT!!

Hello World API
===============

The API provides the following functions.

.. autosummary::
    :toctree: api/

    hello_world  -- Greets Hello to anyone.

The API provides the following classes for extending the
functionality.

.. autosummary::
    :toctree: api/

    HelloBase      -- A base class for greeting hello.
    HelloStandard  -- A simple class for printing the greetings on the terminal.

"""

from my_package._hello_world import hello_world
from my_package._hello_base import HelloBase
from my_package._hello_std import HelloStandard
