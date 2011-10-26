#!/usr/bin/env python
"""
Convert markdown to HTML with some cool features.

Options:
 * -c <cssfile> - use the following CSS file
 * -h <header>  - use the following header.html
 * -f <footer>  - use the following footer
"""

import markdown
import sys, getopt
import re


try:
    opts,bargs=getopt.getopt( sys.argv[1:], "c:h:f:");
    opts=dict(opts)
    if len( bargs )<1:
        raise getopt.GetoptError("ERROR: input file")
    fname=bargs[0]
    header=opts["-h"] if opts.has_key("-h") else None
    footer=opts["-f"] if opts.has_key("-f") else None
    css   =opts["-c"] if opts.has_key("-c") else None
except getopt.GetoptError, err:
    print str(err) # will print something like "option -a not recognized"
    print __doc__
    sys.exit()


f=open(fname, "r")
content=f.read()
f.close()

md=markdown.Markdown(extensions=["pygments"])

# print the HTML
if header:
    f=open(header,"r")
    print f.read()
    f.close()

if css:
    print '<link rel="stylesheet" type="text/css" href="%s">'%css

print md.convert( content )

if footer:
    f=open(footer,"r")
    print f.read()
    f.close()
