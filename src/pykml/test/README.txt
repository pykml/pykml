To run all tests using nose:
  nosetests -s

To run tests for a module, add the name of the module as a parameter:
  nosetests -s PATH/TO/MODULE.py

To run a particular testcase:
  nosetests -s PATH/TO/MODULE.py:TESTCASE

To run a particular test:
  nosetests -s PATH/TO/MODULE.py:TESTCASE.TESTNAME
