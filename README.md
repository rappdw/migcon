[![PyPi](https://img.shields.io/pypi/v/con2sphx.svg)](https://pypi.org/project/con2sphx/) 
[![PyPi](https://img.shields.io/pypi/wheel/con2sphx.svg)](https://pypi.org/project/fs-con2sphx/) 
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/) 
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) 
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) 
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/) 

# Convert Confluence to Jupyter Book

This utility assists in converting Confluence content to a Jupyter Book project. Specifically, once you have a
Confluence HTML export that has been [converted to Markdown](https://github.com/meridius/confluence-to-markdown),
run this utility against the converted source to move documents into a directory structure that mirrors
the confluence page hierarchy as well as generating the Jupyter Book-isms necessary to correctly publish
back to confluence.

To run:

```shell
./con2jupyterbook -i <source-dr> -o <target-dir>
```

## Notes

When exporting from confluence, an `index.md` file is generated that holds the exported page hierarchy in a
nested list. This utility relies on that format, so the `index.md` file should not be edited prior to running 
this utility.

## What it does...

The HTML export from Confluence dumps the whole tree into a single directory. The con2jb will create a 
directory tree to mirror the page hierarchy from confluence and do some requisite fixup automatically. Additionally,
it will generate the jupyter book table of contents to ensure that the correct page hierarchy is restored upon 
publication.

There are several other miscellaneous fixes that are performed including: referencing attachment and image links
from the root rather than the current directory and removal of some sections that are added to a given page that are not
present in the Confluence page source, e.g. Comments, Attachment Lists, Change History.

## Step-by-Step Instructions

0) Prerequisites: Node.js installed, Python installed
1) Use Confluence to export all or a part of your wiki via HTML. 
   ([Export Content...](https://confluence.atlassian.com/doc/export-content-to-word-pdf-html-and-xml-139475.html))
2) Create a working directory and unzip the Confluence export into that directory (sub-dir html)
3) Clone [Confluence to Markdown](https://github.com/meridius/confluence-to-markdown)
4) From within the cloned directory run `npm run start <working-dir>/html <working-dir>/markdown`
5) `pip install con2jb`
6) Run con2jb to convert the exported markdown into a MyST, sphinx friendly markdown/dir structure
    `con2jb -i <working-dir>/markdown -o <working-dir>/sphinx`
7) Copy the resultant jupyter book friendly markdown into the project of your choice
8) Use jupyter book to build your desired output. **Note:** this will result in a few warnings that 
    need to be addressed. 