YEAR := $(shell date +'%Y')
DAY := $(shell date +'%d' | sed 's/^0//')
FOLDER_PATH := src/advent_of_code_2023/day$(DAY)
TEST_FOLDER := tests/day$(DAY)
URL_FOR_TODAY :=  "https://adventofcode.com/$(YEAR)/day/$(DAY)"
BRANCH_NAME := day$(DAY)-challenge1
DEFAULT_STEM := README

.PHONY: create-folder fetch-page generate-pyfiles convert-to-markdown commit-prompt

all: convert-to-markdown generate-pyfiles commit-prompt

create-folder:
	mkdir -p $(FOLDER_PATH)
	mkdir -p $(TEST_FOLDER)
	touch $(FOLDER_PATH)/__init__.py $(TEST_FOLDER)/__init__.py
	@echo "Created folder: $(FOLDER_PATH)"

fetch-page: create-folder
	curl -o "$(FOLDER_PATH)/day$(DAY).html" "$(URL_FOR_TODAY)"
	@echo "Fetched page for day $(DAY) to $(FOLDER_PATH)"

convert-to-markdown: fetch-page
	pandoc -f html -t gfm -s "$(FOLDER_PATH)/day$(DAY).html" | \
		sed -n '/^##/,/\?\*$$/p' | \
		sed 's/^##/#/' \
		> $(FOLDER_PATH)/$(DEFAULT_STEM).md
	rm "$(FOLDER_PATH)/day$(DAY).html" 
	@echo "Saved fetched prompt page to $(FOLDER_PATH)/$(DEFAULT_STEM).md"

generate-pyfiles: convert-to-markdown
	hatch run python templates/generator.py
	    @echo "Created skeletons of main and tests from templates"

commit-prompt:
	git switch -c $(BRANCH_NAME)
	git add $(FOLDER_PATH) $(TEST_FOLDER)
	git commit -m "Add prompt for day $(DAY)"
	git push -u origin $(BRANCH_NAME)
