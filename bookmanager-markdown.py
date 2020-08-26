#! /usr/bin/env python
import click
import textwrap
from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import path_expand
import os
import sys
import shutil

def bibtex(file):
        os.system(f"pandoc -F pandoc-crossref -F pandoc-citeproc -t commonmark  -s --bibliography book/bib/devops.bib --csl bib/ieee-url.csl {file} -o ./tmp.md")
        os.system(f"mv ./tmp.md {file}")

        
def metadata (title, weight, description=None):
    if description is None:        
        data = textwrap.dedent(
            f"""
            ---
            title: {title}
            weight: {weight}
            ---
            """).strip()
    else:
        data = textwrap.dedent(
            f"""
            ---
            title: {title}
            weight: {weight}
            description: >
              {description}
            ---
            """).strip()

    return data

'''
converter = [
  {
      "file": "book/chapters/devops/devop-ci.md",
      "to": "./content/en/modules/devops/devop-ci.md",        
      "old": "# DevOps - Continuous Improvement",
      "new": """
          ---
          title: DevOps - Continuous Improvement
          ---"""
  }
'''

@click.command()
@click.option('--weight', default=100, help='the weight of the entry.')
@click.option('--title', default=None, help='the title of the entry.')
@click.option('--content', default="content/en", help='the content directory base.')
@click.option('--description', default=None, help='the description.')
@click.argument('filename')
def convert(weight, title, content, description, filename):
    """convert the given bookmanager markdown to a hugo markdown with
       bibtex and metadata.
    """

    d = False
    filename = filename.replace("./", "")
    if d:
        file_to = filename.replace("book/chapters/", "").replace(".md","")
        directory = f"./content/en/modules/{file_to}"
        destination = f"{directory}/_index.md"

    else:
        file_to = filename.replace("book/chapters/", "")
        directory = os.path.dirname(f"./content/en/modules/{file_to}")
        destination = f"./content/en/modules/{file_to}"

    print (filename, "->", destination)

    #
    # copy file
    #
    Shell.mkdir(directory)
    content = open(filename, 'r').read()

    with_bib = "[@" in content
    if with_bib:
        content = content + "\n\n## Refernces\n\n"
    
    with  open(destination, 'w') as f:
        f.write(content)
    #
    # apply bibtex
    #
    if with_bib:
        bibtex(destination)
    

    
    content = open(destination, 'r').read().split("\n")
    #print (content)


    for i in range(0, len(content)):

        if "![" in content[i] and '(images' in content[i]:
            content[i] = content[i].replace("(images","(../images")         
        elif "![" in content[i] and '(./images' in content[i]:
            content[i] = content[i].replace("(./images","(../images")            
        elif '<img src="images' in content[i]:
            print ("OOOOO", content[i])
            content[i] = content[i].replace("images","../images")
            print ("WWWWW", content[i])
        elif '<img src="./images' in content[i]:
            content[i] = content[i].replace("./images","../images")            

    #    content = t
    #    print ("JJJJ")
    #if '.\/images' in content:
    #    content.replace(".\/images", "..\/images")
    
    
    if content[0].startswith("#"):
        title = content[0].replace("# ", "").strip()
        content[0] = metadata(title, weight, description)
        content = "\n".join(content)
    elif content[1].startswith("==="):
        title = content[0].strip()
        content[1] = ""
        content[0] = metadata(title, weight, description)
        content = "\n".join(content)
    elif content[0].startswith("---"):
        sys.exit("File in wrong markdown format. detected metadata")
    else:
        sys.exit("First line has no title of metadata")
    with  open(destination, 'w') as f:
        f.write(content)
    

    #print (">>>",directory)
    

if __name__ == '__main__':
    convert()
