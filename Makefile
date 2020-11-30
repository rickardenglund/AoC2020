.PHONY: day

DAY_OF_MONTH ?= `date +%d`

venv:
	python3 -m venv venv


day:
	@install -d days/${DAY_OF_MONTH}
	@rm -rf days/${DAY_OF_MONTH}/*
	@cp -r days/template/* days/${DAY_OF_MONTH}/
	@sed -i '' "s/day XX/day ${DAY_OF_MONTH}/g" days/${DAY_OF_MONTH}/day.py
	@echo "generated day: ${DAY_OF_MONTH}"

