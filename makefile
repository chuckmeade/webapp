ROOT := .

clean-pyc:
	rm -f *.pyc
	rm -f $(ROOT)/pyserver/*.pyc

clean-build:
	rm -fR build/
	rm -fR dist/
	rm -fR deb_dist/
	rm -fR *.egg-info
	rm -f *.tar.gz

service-release: clean-pyc clean-build
	python $(ROOT)/setup.py --command-packages=stdeb.command bdist_deb

clean: clean-pyc clean-build

all:
	python $(ROOT)/setup.py --command-packages=stdeb.command bdist_deb
