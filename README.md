# 🧮 Python Calculator with CI/CD

![CI Pipeline](https://github.com/TU-USUARIO/python-calculator-cicd/actions/workflows/ci. yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)

A simple Python calculator project demonstrating **CI/CD best practices** using GitHub Actions.

## 🚀 Features

- ✅ Clean, well-documented Python code
- ✅ Unit tests with pytest
- ✅ Code coverage reporting
- ✅ Linting with flake8
- ✅ Multi-version Python testing (3.9, 3.10, 3.11)
- ✅ Automated CI pipeline with GitHub Actions

## 📁 Project Structure

```
├── src/
│   └── calculator.py      # Main calculator module
├── tests/
│   └── test_calculator.py # Unit tests
├── .github/
│   └── workflows/
│       └── ci.yml         # CI/CD pipeline
├── requirements.txt       # Dependencies
└── README.md
```

## 🛠️ Local Development

```bash
# Clone the repository
git clone https://github.com/TU-USUARIO/python-calculator-cicd.git
cd python-calculator-cicd

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v

# Run linter
flake8 src/ tests/
```

## 🔄 CI/CD Pipeline

This project uses GitHub Actions to automatically: 

1. **Lint** - Check code style with flake8
2. **Test** - Run unit tests on multiple Python versions
3. **Build** - Verify the package structure

The pipeline runs on every push to `main`/`develop` and on pull requests. 

## 📊 Code Coverage

Tests include coverage reporting.  View the latest coverage in the Actions artifacts.
