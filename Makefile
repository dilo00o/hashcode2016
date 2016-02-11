SOURCES=$(wildcard *.py)
MAIN=main.py
PYTHON=python3
ZIP=code.zip

all:$(MAIN)
	$(PYTHON) $?

$(ZIP):$(SOURCES)
	zip -r $@ $?

clean:
	rm -f code.zip
	rm -f *.out
