publish:
	hugo
	git commit -m "Publish hugo" .
	git push


test:
#	pandoc a.md -t markdown-citations -s --bibliography a.bib --csl ieee.csl -o output.md
#	pandoc a.md --filter pandoc-citeproc -s --bibliography a.bib --csl ieee.csl -o output.md
	cat a.md | pandoc -t commonmark  -s --bibliography a.bib --csl ieee.csl
#-o output.md
