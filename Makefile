SHELL := /bin/bash

test:
	make test_unit
	make test_int

test_unit:
	mkdir -p build
	set -o pipefail; flake8 | sed "s#^\./##" > build/flake8.txt || (cat build/flake8.txt && exit 1)
	nosetests tests/unit --with-xunit --xunit-file=build/unit.xml

test_int:
	mkdir -p build
	sleep 5
	nosetests -s --with-xunit --xunit-file=build/nosetests_int.xml tests/integration
