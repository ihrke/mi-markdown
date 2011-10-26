# -*- coding: utf-8 -*-
"""
    This is based on code from the pygments team (external/mardown-processor.py).
    It didn't work for me with a recent version of pygments, that's why
    I modified it.
    Code segments are highlighted by
    ```python
    def func(a):
        print a
    ```
    for compatibility with github.

    The Pygments Markdown Preprocessor
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This fragment is a Markdown_ preprocessor that renders source code
    to HTML via Pygments.  To use it, invoke Markdown like so::

        from markdown import Markdown

        md = Markdown(extensions=['pygments'])
        html = md.convert(someText)

    .. _Markdown: http://www.freewisdom.org/projects/python-markdown/

    :copyright: Copyright 2006-2011 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

# Options
# ~~~~~~~

# Set to True if you want inline CSS styles instead of classes
INLINESTYLES = True


import re

import markdown

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, TextLexer


def makeExtension(configs=None):
    return PygmentsExtension(configs=configs)


class CodeBlockPreprocessor(markdown.preprocessors.Preprocessor):
    # github compatibility: use ```python <code>``` 
    pattern = re.compile( r'```(\w+?)\n(.+?)```', re.DOTALL)

    formatter = HtmlFormatter(noclasses=INLINESTYLES)


    def run(self, lines):
        def repl(m):
            try:
                lexer = get_lexer_by_name(m.group(1))
            except ValueError:
                lexer = TextLexer()
            code = highlight(m.group(2), lexer, self.formatter)
            code = code.replace('\n\n', '\n&nbsp;\n').replace('\n', '<br />')
            code= '\n\n<div class="code">%s</div>\n\n' % code
            return code

        return self.pattern.sub( repl, "\n".join(lines) ).split("\n")

class PygmentsExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        # Insert instance of 'mypattern' before 'references' pattern
        md.preprocessors.add('pygmentcode', CodeBlockPreprocessor(md), '_begin')
