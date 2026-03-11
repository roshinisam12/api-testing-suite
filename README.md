# 🔌 API Testing Suite

A comprehensive REST API testing framework built with **Python**, **Pytest**, and **Requests** — featuring schema validation, data-driven tests, and full CI/CD integration.

## ✨ Features

- ✅ REST API test coverage (GET, POST, PUT, DELETE)
- ✅ JSON schema validation with `jsonschema`
- ✅ Data-driven tests with parameterization
- ✅ Reusable HTTP client with base URL and auth handling
- ✅ Response time assertions
- ✅ GitHub Actions CI/CD pipeline
- ✅ Detailed HTML reporting

## 🗂️ Project Structure

```
api-testing-suite/
├── tests/
│   ├── test_users.py
│   └── test_posts.py
├── utils/
│   ├── api_client.py
│   └── schema_validator.py
├── .github/
│   └── workflows/
│       └── api-tests.yml
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

```bash
git clone https://github.com/roshinisam/api-testing-suite.git
cd api-testing-suite
pip install -r requirements.txt
```

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_users.py -v

# Run smoke tests only
pytest -m smoke
```

## 🧠 Design Principles

- **Separation of concerns**: HTTP client logic isolated from test assertions
- **Schema validation**: Every response validated against a defined contract
- **Performance awareness**: Response time thresholds enforced on critical endpoints
- **Readable assertions**: Clear failure messages for fast debugging
