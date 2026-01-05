# Pytest Allure Project

A comprehensive testing project demonstrating pytest with Allure reporting and GitHub Actions CI/CD integration.

## 📋 Project Overview

This project showcases:
- ✅ Basic pytest test cases with Allure reporting
- ✅ Allure decorators (feature, story, severity, title)
- ✅ Allure steps and attachments in tests
- ✅ GitHub Actions CI/CD automation
- ✅ Allure report artifacts and GitHub Pages deployment

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/pytest-allure-project.git
cd pytest-allure-project
```

2. **Install dependencies:**
```bash
pip install pytest allure-pytest
```

### Running Tests Locally

**Run all tests:**
```bash
pytest test_hello.py -v
```

**Run tests with Allure results:**
```bash
pytest test_hello.py --alluredir=allure-results -v
```

**Note:** One test (`test_intentional_fail`) is designed to fail - this demonstrates how the Allure report handles test failures.

## 📁 Project Structure

```
pytest-allure-project/
├── test_hello.py                      # Test file with Allure decorators
├── .github/
│   └── workflows/
│       └── pytest-allure.yml          # GitHub Actions workflow
├── .gitignore                         # Git ignore rules
├── README.md                          # This file
└── report.html                        # Generated HTML report
```

## 🧪 Test Cases

The project includes 4 comprehensive test cases with full Allure integration:

1. **test_hello_world()** - Hello World test with Allure steps and attachments
2. **test_simple_math()** - Math operation test with calculation results
3. **test_string_operations()** - String validation with detailed reporting
4. **test_intentional_fail()** - Intentionally failing test (demonstrates failure handling)

### Allure Features Used

- **@allure.feature()** - Groups tests by functionality (Hello World, Basic Tests, Failure Tests)
- **@allure.story()** - Describes test scenarios
- **@allure.severity()** - Sets test priority level
- **@allure.title()** - Custom test title in report
- **with allure.step()** - Test execution steps (visible in detailed report)
- **allure.attach()** - Attaches test data and results to report

## 🔄 GitHub Actions Workflow

The project includes an automated CI/CD pipeline that:

1. ✅ Triggers on push to `main` branch
2. ✅ Sets up Python 3.11 environment
3. ✅ Installs dependencies (pytest, allure-pytest)
4. ✅ Runs all tests with Allure results collection
5. ✅ Generates Allure HTML report
6. ✅ Uploads report as artifact (30 days retention)
7. ✅ Deploys report to GitHub Pages

### View GitHub Actions Results

1. Go to **Actions** tab on GitHub
2. Click on the latest workflow run
3. View test results and download artifacts
4. Access the live Allure report on GitHub Pages

## 📊 Reports

### Allure Report (GitHub Actions)
Automatically generated after each test run and accessible via:
- **Artifacts**: Download from Actions tab
- **GitHub Pages**: https://YOUR_USERNAME.github.io/pytest-allure-project/

**Features:**
- Test overview and statistics
- Tests grouped by features and stories
- Detailed test execution results
- Error messages and stack traces
- Historical trend graphs

## 📝 Configuration

### Git Configuration
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### GitHub Pages Setup
1. Go to Repository Settings → Pages
2. Select `gh-pages` branch as source
3. Save

## 🔗 Useful Commands

```bash
# Check git status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Your message"

# Push to GitHub
git push

# View remote URL
git remote -v

# Run tests with verbose output
pytest test_hello.py -v

# Run specific test
pytest test_hello.py::test_hello_world -v

# Run tests matching pattern
pytest -k "hello" -v

# Generate Allure results
pytest test_hello.py --alluredir=allure-results -v
```

## 📚 Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Documentation](https://docs.qameta.io/allure/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

## 🛠️ Troubleshooting

### Tests not running?
- Ensure pytest is installed: `pip install pytest`
- Check Python version: `python --version` (should be 3.11+)

### No Allure report generated?
- Install allure-pytest: `pip install allure-pytest`
- Run with correct flag: `--alluredir=allure-results`

### GitHub Actions failing?
- Check Actions tab for detailed error messages
- Verify Python version in workflow (3.11)
- Check that all dependencies are properly installed

## 📧 Contact & Support

For questions or issues, please open an issue in the GitHub repository.

## 📄 License

This project is open source and available for educational purposes.

---

**Last Updated:** January 5, 2026
**Python Version:** 3.11+
**Status:** ✅ Working
