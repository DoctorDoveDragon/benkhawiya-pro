.PHONY: help format lint security test clean

help:
	@echo "Available commands:"
	@echo "  make format    - Format code with black"
	@echo "  make lint      - Run flake8 linter"
	@echo "  make security  - Run bandit security scan"
	@echo "  make test      - Run all quality checks"
	@echo "  make clean     - Remove Python cache files"

format:
	black app/ --line-length 127

lint:
	flake8 app/ --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

security:
	bandit -r app/ -f txt

test: format lint security
	@echo "All quality checks passed!"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.log" -delete
