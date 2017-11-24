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

uri = s3://353solutions/py2go
upload: $(index) *.css
	s3cmd put $(html) *.css logo.png $(uri)/
	s3cmd setacl $(uri) --acl-public --recursive

.PHONY: all test clean fresh
