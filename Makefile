readme = README.md
index = index.html

#all: $(readme)
all: $(index)


$(index): index.html.in style.css pygmentize.css *.go *.py
	./generate-html.py < $< > $@

$(readme): $(readme).in generate.py *.go *.py
	./generate.py < $< > $@

test:
	pytest -v

clean:
	rm -f $(readme)
	rm -f $(index)
	rm pygmentize.css

pygmentize.css:
	pygmentize -S default -f html > $@

fresh: clean all


.PHONY: all test clean fresh
