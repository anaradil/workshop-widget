# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = FedoraHubswidgettutorial
SOURCEDIR     = .
BUILDDIR      = _build
REPONAME	  = fedora-hubs-widget-workshop
LOCALREPONAME = _pagure-docs
GITREV       := $(shell git show -s --pretty=format:%h)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile upload

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

upload: html $(LOCALREPONAME)
	cp -r _build/html/* $(LOCALREPONAME)
	cd $(LOCALREPONAME) && git add -A
	cd $(LOCALREPONAME) && git commit -m "Documentation update for rev $(GITREV)"
	cd $(LOCALREPONAME) && git push

$(LOCALREPONAME):
	git clone ssh://git@pagure.io/docs/$(REPONAME).git $(LOCALREPONAME)
