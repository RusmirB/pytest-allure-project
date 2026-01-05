# Pytest Allure Project

A comprehensive testing project demonstrating pytest with Allure reporting and GitHub Actions CI/CD integration.

## 📋 Project Overview

This project showcases:
- ✅ Basic pytest test cases
- ✅ Allure report decorators and steps
- ✅ HTML test reports (pytest-html)
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
pip install pytest allure-pytest pytest-html
```

### Running Tests Locally

**Run all tests:**
```bash
pytest test_hello.py -v -s
```

**Run tests with Allure results:**
```bash
pytest test_hello.py --alluredir=allure-results -v -s
```

**Generate HTML report (pytest-html):**
```bash
pytest test_hello.py -v -s --html=report.html --self-contained-html
```

Then open `report.html` in your browser.

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

The project includes 4 test cases:

1. **test_hello_world()** - Basic assertion test with Allure steps
2. **test_simple_math()** - Math operation test with calculation and attachment
3. **test_string_operations()** - String validation test
4. **test_intentional_fail()** - Intentionally failing test (demonstrates failure handling)

### Allure Features Used

- **@allure.feature()** - Groups tests by functionality
- **@allure.story()** - Describes test scenarios
- **@allure.severity()** - Sets test priority (BLOCKER, CRITICAL, NORMAL, MINOR, TRIVIAL)
- **@allure.title()** - Custom test title
- **with allure.step()** - Test execution steps
- **allure.attach()** - Attaches data to reports

## 🔄 GitHub Actions Workflow

The project includes an automated CI/CD pipeline that:

1. ✅ Triggers on push and pull requests to `main` branch
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

### Local HTML Report
After running tests locally with `--html=report.html`, open `report.html` in your browser.

**Features:**
- Test summary (passed/failed/skipped)
- Detailed test results
- Error messages and stack traces
- Execution time metrics

### Allure Report (GitHub Actions)
Automatically generated and accessible via:
- **Artifacts**: Download from Actions tab
- **GitHub Pages**: https://YOUR_USERNAME.github.io/pytest-allure-project/

**Features:**
- Test overview and statistics
- Tests grouped by features and stories
- Severity level filtering
- Step-by-step test execution timeline
- Attached data and screenshots
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
pytest test_hello.py -v -s

# Run specific test
pytest test_hello.py::test_hello_world -v

# Run tests matching pattern
pytest -k "hello" -v
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
