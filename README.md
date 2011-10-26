# My way of running Markdown #

_Check out the [Github-page](https://github.com/ihrke/mi-markdown) for
the code and everything else_

(see [raw version](https://raw.github.com/ihrke/mi-markdown/master/README.md))

## Files ##
* [markd.py](https://github.com/ihrke/mi-markdown/blob/master/mdown.py): executable to turn markdown into HTML
  + from the docstring:

     > Convert markdown to HTML with some cool features.
     >
     > Options:
     >
     > * -c cssfile: use the following CSS file
     > * -h header:  use the following header.html
     > * -f footer:  use the following footer

* Example:
    
      ``python mdown.py -h header_ex.html -f footer_ex.html README.md > README.html``


* [mdx_pygments.py](https://github.com/ihrke/mi-markdown/blob/master/mdx_pygments.py): python-markdown extension for syntax-highlighting a'la github
                 
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

