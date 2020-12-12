.PHONY: gen_day run source test

DAY ?= `date +%d`

venv:
	python3 -m venv venv

#source: venv
#	source venv/bin/activate

gen_day:
	@install -d days/${DAY}
	@rm -rf days/${DAY}/*
	@cp -r days/template/* days/${DAY}/
	@sed -i '' "s/day XX/day ${DAY}/g" days/${DAY}/day.py
	@echo "generated day: ${DAY}"

run:
	python days/${DAY}/day.py

test: days/*/test_*.py
	@set -e && \
	for testfile in $^ ; do \
	  	echo $$testfile ; \
		python $$testfile ; \
	done

