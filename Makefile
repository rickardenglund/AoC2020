.PHONY: gen_day run source test

DAY ?= `date +%d`

gen_day:
	@install -d days/${DAY}
	@rm -rf days/${DAY}/*
	@cp -r days/template/* days/${DAY}/
	@sed -i "s/day XX/day ${DAY}/g" days/${DAY}/day.py
	@python util/get_puzzle.py ${DAY} days/${DAY}/puzzle.py
	@git add days/${days}

	@echo "generated day: ${DAY}"

run:
	python days/${DAY}/day.py

test: days/*/test_*.py
	@set -e && \
	for testfile in $^ ; do \
	  	echo $$testfile ; \
		python $$testfile ; \
	done

venv:
	python3 -m venv venv

#source: venv
#	source venv/bin/activate

pip_freeze:
	pip freeze > requirements.txt

pip_install:
	pip install -r requirements.txt