SOURCES=$(wildcard *.py)
MAIN=main.py
PYTHON=python
ZIP=code.zip

all:$(MAIN) $(ZIP)
	$(PYTHON) $<

$(ZIP):$(SOURCES)
	zip -r $@ $?

clean:
	rm -f code.zip
	rm -f *.out
