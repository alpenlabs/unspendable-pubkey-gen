.DEFAULT_GOAL := run

.PHONY: ensure-sage
ensure-sage:
	@if ! command -v sage &> /dev/null; then \
		echo "sage not found. Please install it by following the instructions from: https://doc.sagemath.org/html/en/installation/" \
		exit 1; \
  fi

.PHONY: run
run: ensure-sage
	poetry run sage main.py
