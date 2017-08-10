readme = README.md

all: $(readme)

$(readme): $(readme).in generate.py
	./generate.py < $< > $@

test:
	pytest -v

clean:
	rm -f $(readme)

fresh: clean all


.PHONY: all test clean fresh
