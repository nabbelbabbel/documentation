# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = build

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

.PHONY: help clean html html_short

default: html

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"

clean:
	rm -rf $(BUILDDIR)/*
	rm -rf source/utilities
	rm -rf source/core
	rm -rf source/readuct
	rm -rf source/sparrow
        

html:
	mkdir -p build/xml
	cd source/ && doxygen utilities.dox
	python3 apidoc.py -o source/utilities -p utilities build/xml/utilities/
	cd source/ && doxygen core.dox
	python3 apidoc.py -o source/core -p core build/xml/core/
	cd source/ && doxygen sparrow.dox
	python3 apidoc.py -o source/sparrow -p sparrow build/xml/sparrow/
	cd source/ && doxygen readuct.dox
	python3 apidoc.py -o source/readuct -p readuct build/xml/readuct/
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

html_short:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."
