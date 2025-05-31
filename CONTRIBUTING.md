# Contributing to JEE Tracker

## Getting Started
- Fork the repository
- Clone your fork: `git clone https://github.com/yourusername/jee-tracker.git`
- Create virtual environment: `python -m venv venv`
- Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
- Install dependencies: `pip install -r requirements.txt`

## Development Setup
- Install dev dependencies: `pip install -r requirements-dev.txt`
- Run tests: `python -m pytest`
- Format code: `black .` and `isort .`
- Lint: `flake8 .`

## Making Changes
- Create feature branch: `git checkout -b feature/your-feature`
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation
- Commit with clear messages

## Pull Request Process
- Ensure all tests pass
- Update README if needed
- Reference issue numbers
- Provide clear PR description

## Code Style
- Use Black for formatting
- Follow PEP 8
- Add docstrings for functions/classes
- Use type hints where possible

## Reporting Issues
- Use issue templates
- Provide Python version, OS details
- Include error messages and steps to reproduce
