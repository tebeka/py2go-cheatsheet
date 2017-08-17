html = cheatsheet.html

all: $(html)


$(html): $(html).in style.css pygmentize.css *.go *.py modules.yaml
	./generate-html.py < $< > $@

test:
	flake8 *.py
	pytest -v

clean:
	rm -f $(html)
	rm pygmentize.css

pygmentize.css:
	pygmentize -S default -f html > $@

fresh: clean all

upload: $(index) *.css
	s3cmd put $(html) *.css logo.png s3://353-scipy/py2go/
	s3cmd setacl s3://353-scipy/py2go/ --acl-public --recursive

.PHONY: all test clean fresh
