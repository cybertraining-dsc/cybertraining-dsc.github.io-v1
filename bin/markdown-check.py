#! /usr/bin/env python

# usage:
# markdown-check.py content/en/report/fa20-523-350/report/report.md
# markdown-check.py content/en/report/fa20-523-312/project/project.md

errors = 0
wrong = False

def error(msg):
    global errors
    global wrong
    print ("ERROR:", msg)
    wrong = True
    errors = errors + 1
    
import sys
filename = sys.argv[1]

with open(filename, 'r') as f:
  content = f.read()


# block above, bellow previous next figures and tables  
oneline = " ".join(content.split()).lower()

for form in ["figure", "table"]:
    for word in ["next", "previous",        
                 "above", "below",
                 "above the", "below the"]:

        if f"{word} {form}" in oneline:
            error(f"Refer to the {form} by numbered {form}. Found {word} {form}") 
        if f"{form} {word}" in oneline:
            error(f"Refer to the {form} by numbered {form}. Found {form} {word}")


# word count

lines = 0
words = 0
for line in content.splitlines():
    lines = lines + 1
    if "##" in line and "References" in line:
        break
    
    line = line.replace("*", "")
    line = line.replace("#", "")
    line = line.replace("-", "")
    line = line.replace("{{% pageinfo %}}", "")
    line = line.replace("{{% /pageinfo %}}", "")
    
    
    line = line.strip()
    # print (line)
    if "![" in line:
        line = ""
    words = words + len(line.split(" "))

  
#print (content)

# check for numbers

if "## 1." not in content:
    error("Use numbered section headers.")

if "## 2." not in content or "## 3." not in content:
    error("To few sections in the report.")


if "## Abstract" not in content:
    error("Abstract missing")

if "Contents" not in content:
    error("Contents missing")

toc = """Contents

{{< table_of_contents >}}

{{% /pageinfo %}}
"""

for section in ["Conclusion", "Abstract", "Introduction"]:
    if section not in content:
        error(f"Could not find section {section}.")
    
if toc not in content or "{{% pageinfo %}}" not in content:
    error("pageinfo with Contents template is not properly used.")

if "] :" in content:
    error ("Spaces not allowed in front of :")

if ".[^" in content or ". [^" in content:
    error ("Citation after a . not allowed.")

if "[^" not in content or "]:" not in content:
    error("Refernces are missing")
    
#check image inclusion

counter = 0
for line in content.splitlines():
    line = line.strip()
    counter = counter + 1 
    if line.startswith("!["):
        if "raw" not in line:
            error(f"{counter}: Image must be included from raw. URL wrong.")

        ending = line.rsplit(".")[-1][:-1]
        if ending not in ["png", "jpg", "jpeg"]:
            error(f"{counter}: Image ending must be one of png, jpg, jpeg.")
        if "/images/" not in line:
            error(f"{counter}: Image must be in an images folder")

if "[Edit](https://github.com/cybertraining-dsc/" not in content:
    error("no edit link found")

if "**Keywords:**" not in content:
    error("Keywords not found.")

titles = 0
code = False    
counter = 0
section = False
for line in content.splitlines():
    counter = counter + 1     
    line = line.strip()
    if line.startswith("```"):
        code = not code
    if not code:
        if section and not line == "":
            error(f"{counter}: Line after heading must be empty.")        
        section = line.startswith("#")

        if line.startswith("# "):
            titles = titles + 1
        if " http://" in line or " https://" in line:
            error(f"{counter}: http link is not enclosed in < >.")
    

if titles > 1:
    error("you used multiple titles")

        
counter = 0
# check for html
for line in content.splitlines():
    line = line.strip()
    counter = counter + 1     

    for tag in ["h1", "h2", "h3", "h4", "th", "td",
                "ul", "img", "p", "b", "li"]:
        if f"<{tag}>" in line:
            error(f"{counter}: HTML tag <{tag}> not allowed in project.")
        if f"</{tag}>" in line:
            error(f"{counter}: HTML tag </{tag}> not allowed in project.")
    if "“" in line or "”" in line:
        error(f"{counter}: Illeagal quote use \" instead")

# Check README

try:
    filename = "README.yml"

    with open(filename, 'r') as f:
        readme = f.read()

    if "TBD" in readme:
        error("Your README.yml is not set up properly.")
except:
    pass
        
print()
print ("Lines:", lines)
print ("Words:", words)
print()
    
if wrong:
    print (f"{errors} Errors found")
    print("This is not a valid report")
    sys.exit(1)
else:
    print("OK. No errors found. But there could be some as we do not test everything.")
print()

