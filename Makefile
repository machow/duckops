docs-build:
	cd docs \
	  && quartodoc build --verbose \
	  && quarto render
