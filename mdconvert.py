import html2text
import re
from os import listdir
import shutil
h = html2text.HTML2Text()
h.body_width = 120
src = "C:/Users/a/Downloads/sebi-it"
dest = "C:/Users/a/Downloads/sebi-docs/docs"
files = [
    ("C - Quick Guide - Tutorialspoint.htm", "c.md"),
    ("C++ Quick Guide - Tutorialspoint.htm", "cpp.md"),
    ("Cryptography - Quick Guide - Tutorialspoint.htm", "crypto.md"),
    ("Data Structures & Algorithms - Quick Guide.htm", "dsa.md"),
    ("Data Warehousing - Quick Guide.htm", "dw.md"),
    ("DBMS - Quick Guide - Tutorialspoint.htm", "db.md"),
    ("DCN - Quick Guide - Tutorialspoint.htm", "dcn.md"),
    ("Internet Technologies - Quick Reference Guide.htm", "it.md"),
    ("Java - Quick Guide - Tutorialspoint.htm", "java.md"),
    ("Python Pandas - Quick Guide.htm", "python.md"),
    ("R - Quick Guide - Tutorialspoint.htm", "r.md"),
    ("SQL - Quick Guide - Tutorialspoint.htm", "sql.md"),
    ("Unix _ Linux - Quick Guide.htm", "unix.md")
]

for file in files:
    src_path = src + "/" + file[0]
    dest_path = dest + "/" + file[1]
    f = open(src_path, 'r', encoding="utf-8")
    content = ''.join(f.readlines()[70:])
    content = content.replace("</b></p>\n<p>","</b>")
    content = content.replace("<td><p>","<td>")
    content = content.replace("<td>\n<p>","<td>")
    content = content.replace("</p></td>","</td>")
    content = content.replace("</p>\n</td>","</td>")
    
    f.close()
    print(file)
    md = h.handle(content)
    f = open(dest_path, 'w', encoding="utf-8")
    dir_src =  file[0].replace(".htm", "") + "_files"
    dir_dest =  file[1].replace(".md", "") + "-img"
    dir_src_path = src + "/" + dir_src
    dir_dest_path = dest +"/" + dir_dest
    md = md.replace(dir_src.replace(' ','%20'), dir_dest)
    f.write(md)
    #shutil.copytree(dir_src_path,dir_dest_path)
    f.close()