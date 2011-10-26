import markdown
import sys
import re


fname=sys.argv[1]
f=open(fname, "r")
content=f.read()
f.close()

md=markdown.Markdown(extensions=["pygments"])

# print the HTML
print md.convert( content )#,  ['codehilite', 'fenced_code'])
