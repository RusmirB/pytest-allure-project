# Pytest Allure Project

Testing project with pytest, Allure reporting, and GitHub Actions CI/CD.

## Quick Start

**Install:**
```bash
pip install pytest allure-pytest
```

**Run tests:**
```bash
pytest test_hello.py --alluredir=allure-results -v
```

**Generate report:**
```bash
allure generate allure-results --single-file --clean -o allure-report
start allure-report/index.html
```

## Project Structure

```
├── test_hello.py              # Tests with Allure decorators
├── .github/workflows/
│   └── pytest-allure.yml      # GitHub Actions workflow
├── .gitignore
└── README.md
```

## Test Cases

- `test_hello_world()` - Basic test with steps and attachments
- `test_simple_math()` - Math operations
- `test_string_operations()` - String validation
- `test_intentional_fail()` - Failure example

## GitHub Actions

Workflow runs on push/PR:
1. Installs dependencies
2. Runs tests with Allure
3. Generates HTML report
4. Uploads as artifact (30 days)

**View results:** Actions tab → Download artifact → Extract → Open `index.html`

## Troubleshooting

- **Tests not running:** `pip install pytest allure-pytest`
- **No report:** Ensure `--alluredir=allure-results` flag
- **GitHub Actions fail:** Check Actions tab for error details

## Resources

- [Pytest Docs](https://docs.pytest.org/)
- [Allure Docs](https://docs.qameta.io/allure/)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
