draft:
	hugo server -D

pull:
	cd content/en/report/cloudmesh-openapi; git pull
	cd content/en/report/fa20-523-301; git pull
	cd content/en/report/fa20-523-304; git pull
	cd content/en/report/fa20-523-305; git pull
	cd content/en/report/fa20-523-307; git pull
	cd content/en/report/fa20-523-308; git pull
	cd content/en/report/fa20-523-309; git pull
	cd content/en/report/fa20-523-312; git pull git@github.com:cybertraining-dsc/fa20-523-312.git master
	cd content/en/report/fa20-523-313; git pull
	cd content/en/report/fa20-523-314; git pull
	cd content/en/report/fa20-523-316; git pull
	cd content/en/report/fa20-523-317; git pull
	cd content/en/report/fa20-523-326; git pull
	cd content/en/report/fa20-523-329; git pull
	cd content/en/report/fa20-523-331; git pull
	cd content/en/report/fa20-523-333; git pull
	cd content/en/report/fa20-523-337; git pull
	cd content/en/report/fa20-523-342; git pull
	cd content/en/report/fa20-523-343; git pull
	cd content/en/report/fa20-523-348; git pull

view:
	gopen http://localhost:1313/ 
server:
	hugo server

publish:
	hugo
	git commit -m "Publish hugo" .
	git push


test:
#	pandoc a.md -t markdown-citations -s --bibliography a.bib --csl ieee.csl -o output.md
#	pandoc a.md --filter pandoc-citeproc -s --bibliography a.bib --csl ieee.csl -o output.md
	cat a.md | pandoc -t commonmark  -s --bibliography a.bib --csl ieee.csl
#-o output.md

list:
	python bin/tree.py > content/en/modules/list/_index.md
