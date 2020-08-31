home = "https://github.com/cloudmesh-community/book/blob/master/chapters/"

exclude = [".pdf",
               ".PDF",
               ".svg",
               ".png",
               ".jpg",
               ".gif",
               ".jpeg",
               ".sh",
               ".JPG",
               ".scad",
               "graffle",
               ".bib",
               ".java",
               ".docx",
               ".stl",
               ".dot",
               ".pptx",
               ".mm",
               ".conf",
               ".yaml"
               " images",
               " images",
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
               "─ bin",
               " bin",
               "─ l"]

def valid(name):
    for t in exclude:
        if t in name:
            return False
    return True
    
import os

os.system ('find  ../book/chapters -name "*" > tmp.txt')

with open ("tmp.txt", "r") as f:
    lines = f.read().strip().split("\n")


for line in lines:
    if valid(line):
        p = line

        count = len(p.split("/"))
        indent =  "&nbsp" * count

        base = p.rsplit("/", 1)[1]

        link = p.replace("../book/chapters", home)
        
        print (f"{indent} [{base}]({link})") 
