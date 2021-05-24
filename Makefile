.PHONY: help all clean create-venv requirements dependencies converge verify

help:				## Show this help
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

all: create-venv test		## Default action

.venv:		## Create virtual environment
	( \
		python3 -m venv .venv && \
		. .venv/bin/activate && \
		python3 -m pip install --upgrade pip && \
		python3 -m pip install --upgrade setuptools; \
	)

requirements: .venv		## Install dependencies from requirements.txt
	( \
		. .venv/bin/activate && \
		python3 -m pip install -r requirements.txt; \
	)

create-venv: requirements	## Create virtual environment
	@echo "virtualenv ready."

dependencies:			## Install packages required for development
	sudo apt install -y python3-pip libssl-dev libffi-dev git python3-venv

converge:			## Run molecule converge
	( \
		. .venv/bin/activate && \
		molecule converge; \
	)

verify:				## Run molecule verify
	( \
		. .venv/bin/activate && \
		molecule verify; \
	)

test:				## Run molecule test
	( \
		. .venv/bin/activate && \
		molecule test; \
	)

clean:				## Remove all temporary files
	( \
		. .venv/bin/activate && \
		molecule destroy; \
	)
	rm -rf .venv
	rm -rf .cache
