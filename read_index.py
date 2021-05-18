#!/usr/bin/python

import sys
import parsing
import array
import math
from operator import itemgetter
from dataclasses import dataclass
import re
import os
import zipfile

# grab length and command line arguments
arglen =  len(sys.argv)

if(sys.argv[1] == '--doc') & (arglen == 3): # if it's a document
    doc = sys.argv[2]
    parsing.handle_doc(doc)
elif(sys.argv[1] == '--term') & (arglen == 3): # if it's a term
    term = sys.argv[2]
    parsing.handle_term(term)
elif(arglen == 5): # if it is both
    term = sys.argv[2]
    doc = sys.argv[4]
    parsing.handle_index(term, doc)




