FILES :=                            				\
    	.travis.yml                     			\
    	manage.py                       			\
    	apiary.apib 						\
	IDB.log             					\
    	models.html						\
    	UML.pdf							\
    
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

models.html: nsaid/models.py
	pydoc3 -w models

IDB.log:
	git log > IDB.log

tests.out:
	coverage3 run manage.py test nsaid/ >  nsaid/tests.out 2>&1
	coverage3 report -m  nsaid/tests.py nsaid/models.py  >> nsaid/tests.out
	cat nsaid/tests.out

