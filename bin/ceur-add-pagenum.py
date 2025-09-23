#!/usr/bin/env python3
"""
This script adds page numbers to an index.html file written according to the
CEUR-WS specification: https://ceur-ws.org/HOWTOSUBMIT.html. The script depends
on the lxml and PyPDF2 packages.
"""

import os
import shutil
import sys
import textwrap

from lxml import html
from PyPDF2 import PdfFileReader

if len(sys.argv) > 2 or sys.argv[1] == "-h":
    MSG = """\
        Usage: ceur-add-pagenum [-h|<dir>]"

        where <dir> is the directory containing the index.html file and all paper PDFs.
        If <dir> is omitted, the current directory is assumed. The original file is
        saved with the bak extension.\
        """
    print(textwrap.dedent(MSG), file=sys.stderr)
    sys.exit(1)

dir = sys.argv[1] if len(sys.argv) >= 2 else "."
filename = os.path.join(dir, "index.html")

shutil.copyfile(filename, filename+".bak")

tree = html.parse(filename)
li_nodes = tree.xpath("//li[span[@class='CEURPAGES']]")
curr_page = 1

for li_node in li_nodes:
    a_nodes = li_node.xpath("a[@href]")
    if len(a_nodes) == 0:
        continue
    href = a_nodes[0].get("href")
    reader = PdfFileReader(os.path.join(dir, href))
    page_nodes = li_node.xpath("*[@class='CEURPAGES']")
    if len(page_nodes) == 0:
        continue
    page_count = len(reader.pages)
    page_nodes[0].text = f"{curr_page}–{curr_page+page_count-1}"
    curr_page += page_count

tree.write(filename, encoding="utf-8", method="html")
