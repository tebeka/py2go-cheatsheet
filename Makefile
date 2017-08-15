readme = README.md
index = index.html

#all: $(readme)
all: $(index)


$(index): index.html.in style.css pygmentize.css *.go *.py
	./generate-html.py < $< > $@

$(readme): $(readme).in generate.py *.go *.py
	./generate.py < $< > $@

test:
	flake8 *.py
	pytest -v

clean:
	rm -f $(readme)
	rm -f $(index)
	rm pygmentize.css

pygmentize.css:
	pygmentize -S default -f html > $@

fresh: clean all

upload: $(index) *.css
	s3cmd put index.html *.css s3://353-scipy/py2go/
	s3cmd setacl s3://353-scipy/py2go/ --acl-public --recursive

.PHONY: all test clean fresh
