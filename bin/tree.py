import os
import requests


common_home = "https://github.com/cloudmesh-community/book/blob/master/chapters/"
cybertraining_home = "https://github.com/cybertraining-community/book/blob/master/chapters/"

print("""
---
title: "List"
linkTitle: "List"
weight: 1
description: >
  Link and location to available modules in markdown
---

{{% pageinfo %}}
This page contains the list of current modules.
{{% /pageinfo %}}

""".strip())

dirs = ['bin', 'images']

exclude = [
    "/setup"
    "empty.md",
    "_index.md",
    "version.md",
    "join",
    "gg.md",
    "issues.md",
    "a.md",
    "authors.md",
    ".pdf",
    ".PDF",
    ".svg",
    ".png",
    ".jpg",
    ".gif",
    ".jpeg",
    ".sh",
    ".JPG",
    ".scad",
    ".graffle",
    ".bib",
    ".java",
    ".docx",
    ".stl",
    ".dot",
    ".pptx",
    ".mm",
    ".conf",
    ".yaml"
    ".html",
    ".py",
    ".PNG",
    ".txt",
    ".yaml",
    ".tex",
    ".rst",
    ".tiff",
    ".ipynb",
    ".csv",
    ".fzz",
    ".bin",
    "l"]

def valid(name):
    for t in exclude:
        if t in name:
            return False
    for t in dirs:
        if "/" + t in name:
            return False
    return True

i_git = '{{< fa fab github >}}'
i_folder = '{{< fa folder >}}'
i_file = '{{< fa file >}}'

i_warn= '{{< fa exclamation-triangle >}}'
    
def get_title(path):
    error = ""
    title = ""
    if os.path.isdir(path):
        title = os.path.basename(path)
        title = f"{i_folder} "  + title
        return title, error
    else:
        try:
            with open (p, "r") as f:
                content = f.read().split("\n")
            title = content[0]
            if "#" not in title:
                error = error + "h"
            # remove ref
            title = title.split(" {")[0]
            counter = title.count('#') 
            if counter > 1:
                error = error + "m"
            title = title.replace("{.part}", "")
            title = title.replace(":o2:", "")
            title = title.replace("[", "")
            title = title.replace("]", "")

            title = title.replace("#", "") 
            title = title.strip()
            title = f"{i_file} " + title
            return title, error
        except Exception as e:
            title = f"{i_warn} " + title
            return title, e
        
os.system ('find  ../book/chapters -name "*" > tmp.txt')

with open ("tmp.txt", "r") as f:
    lines = f.read().strip().split("\n")

print ()
print ("Legend")
print ()
print ("* h - **header** missing the #")
print ("* m - too **many** #'s in titles") 
print()
    
print ()    
#print ("| Title | Warn | GitHub | Cybertraining | ")
#print ("| ---- | ---- | ----  | ---- |")
print ("| Title | Warn | Cybertraining | ")
print ("| ---- | ---- | ---- |")
for line in lines:
    warn = ""

    if valid(line):
        # print (f"| >{line}< |" )
        p = line

        count = len(p.split("/"))
        #indent =  "____" * count
        indent =  "&nbsp;&nbsp;&nbsp;&nbsp;" * (count - 3)
        
        base = p.rsplit("/", 1)[1]

        # url = "http://download.thinkbroadband.com/10MB.zip"
        # r = requests.get(url)
        # pontent = r.content


        title, error = get_title(p)
            
        
        common_link = p.replace("../book/chapters", common_home)
        cybertraining_link = p.replace("../book/chapters", cybertraining_home)
        if error:
            warn = i_warn
            
        # print (f"| {indent} [{title}]({common_link}) {warn} | {error} | {indent} {i_git}  [{base}]({common_link}) |  [read]({cybertraining_link})  |")
        print (f"| {indent} [{title}]({common_link}) {warn} | {error} |  [read]({cybertraining_link})  |") 
