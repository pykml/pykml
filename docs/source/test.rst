.. _test: 


Test 1
=================

Some documentation text.

.. doctest:: test1

   >>> print(1)
   1

Some more documentation text.


Highlighting
------------

.. highlight:: python
   :linenothreshold: 5

.. doctest:: test2

    >>> 1 + 1
    2
    >>> 1 + 1
    2
    >>> 1 + 1
    2


Include external file
----------------------

.. literalinclude:: examples/test_external_example.py
