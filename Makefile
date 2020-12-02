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
	cd days/${DAY} && python day.py

test:
	@scripts/test.sh
