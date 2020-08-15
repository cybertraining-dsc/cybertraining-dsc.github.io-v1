publish:
	hugo
	git commit -m "Publish hugo" .
	git push
