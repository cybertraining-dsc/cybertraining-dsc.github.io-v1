draft:
	hugo server -D

setup:
	npm install autoprefixer
	npm install postcss


pull:
	git pull
	cd content/en/report/cloudmesh-openapi; git checkout main; git pull
	cd content/en/report/fa20-523-301; git checkout master; git pull
	cd content/en/report/fa20-523-304; git checkout master; git pull
	cd content/en/report/fa20-523-305; git checkout master; git pull
	cd content/en/report/fa20-523-307; git checkout main; git pull
	cd content/en/report/fa20-523-308; git checkout main; git pull
	cd content/en/report/fa20-523-309; git checkout main; git pull
	cd content/en/report/fa20-523-312; git checkout main; git pull
	cd content/en/report/fa20-523-313; git checkout main; git pull
	cd content/en/report/fa20-523-314; git checkout main; git pull
	cd content/en/report/fa20-523-315; git checkout master; git pull
	cd content/en/report/fa20-523-316; git checkout master; git pull
	cd content/en/report/fa20-523-317; git checkout main; git pull
	cd content/en/report/fa20-523-319; git checkout master; git pull
	cd content/en/report/fa20-523-323; git checkout master; git pull
	cd content/en/report/fa20-523-326; git checkout main; git pull
	cd content/en/report/fa20-523-327; git checkout master; git pull
	cd content/en/report/fa20-523-328; git checkout master; git pull
	cd content/en/report/fa20-523-329; git checkout master; git pull
	cd content/en/report/fa20-523-330; git checkout master; git pull
	cd content/en/report/fa20-523-331; git checkout main; git pull
	cd content/en/report/fa20-523-332; git checkout master; git pull
	cd content/en/report/fa20-523-333; git checkout master; git pull
	cd content/en/report/fa20-523-334; git checkout master; git pull
	cd content/en/report/fa20-523-336; git checkout master; git pull
	cd content/en/report/fa20-523-337; git checkout master; git pull
	cd content/en/report/fa20-523-339; git checkout master; git pull
	cd content/en/report/fa20-523-340; git checkout main; git pull
	cd content/en/report/fa20-523-341; git checkout master; git pull
	cd content/en/report/fa20-523-342; git checkout master; git pull
	cd content/en/report/fa20-523-343; git checkout master; git pull
	cd content/en/report/fa20-523-345; git checkout master; git pull
	cd content/en/report/fa20-523-346; git checkout main; git pull
	cd content/en/report/fa20-523-347; git checkout main; git pull
	cd content/en/report/fa20-523-348; git checkout main; git pull
	cd content/en/report/fa20-523-349; git checkout main; git pull
	cd content/en/report/fa20-523-350; git checkout main; git pull

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
