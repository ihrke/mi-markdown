# My way of running Markdown #

(see [raw version](https://raw.github.com/ihrke/mi-markdown/master/README.md))

## Files ##
* [markd.py](markd.py) - executable to turn markdown into HTML
* [mdx_pygments.py](mdx_pygments.py) - python-markdown extension for syntax-highlighting a'la github
                 
## Features ##

* github-style fenced code with syntax highlighting
        ```python
        def func(a):
           print a
        ```
* works with all code types supported by pygments, e.g.
        ```c
        void main(int argc, char **argv){
              return -1;
        }
        ```
* I will unscrupulously add whatever feature I like.

## Notes ##

Uses:

* [Python Markdown](http://www.freewisdom.org/projects/python-markdown/)
* [Pygments](http://pygments.org/)

