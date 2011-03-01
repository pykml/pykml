#!/usr/bin/python
import sys
import getopt
from pykml.kml_gx.parser import parse
from pykml.kml_ogc.factory import write_python_script_for_kml_document

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error, msg:
             raise Usage(msg)
        # main code
        filename = argv[1]
        with open(filename) as f:
            kmldoc = parse(f, validate=True)
            print write_python_script_for_kml_document(kmldoc)

    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())


