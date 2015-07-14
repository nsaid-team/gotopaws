FILES :=                            				\
    	.travis.yml                     			\
    	manage.py                       			\
    	apiary.apib 						\
	IDB.log             					\
    	models.html						\
    	Report.pdf						\
    	tests.out						\
    	tests.py						\

all:

check:
	@for i in $(FILES);                                     \
    do                                                          \
        [ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; \
    done

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  tests.out
	rm -rf __pycache__

config:
	git config -l

test: tests.out

models.html: models.py
	pydoc3 -w models

IDB.log:
	git log > IDB.log

tests.out: tests.py
	python -m unittest discover -s nsaid test
	./manage.py test 
