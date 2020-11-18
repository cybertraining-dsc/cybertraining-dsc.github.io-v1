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

code = False    
counter = 0
section = False
for line in content.splitlines():
    counter = counter + 1     
    line = line.strip()
    if line.startswith("```"):
        code = not code
    if not code:
        if "- [ ]" in line:
            error(f"{counter}: Please address comment.")        
            print (line)

if  "Status: final" not in content: 
    error("Please indicate final submission with Status: final after the CHeck Report Icon")
    
if wrong:
    print (f"{errors} Errors found")
    print("This is not a valid report")
    sys.exit(1)
else:
    print("OK. No errors found. But there could be some as we do not test everything.")
print()

