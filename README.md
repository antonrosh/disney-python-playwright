# Disney Testing Framework using Python and Playwright

Welcome to the Disney Testing Framework - a comprehensive automation test solution employing Python and Playwright to perform rigorous testing on the Disney+ website. This robust framework is adept at performing UI tests and will soon support API testing.

## Creator's Bio

Hi! I'm Anton Rosh, an accomplished Software Development Engineer in Test (SDET) and a Quality Assurance Automation Lead with a career spanning over 7 years. My specialization includes:

- Designing and implementing efficient test automation solutions to improve product quality and expedite release cycles.
- Building test automation frameworks from scratch.
- Proficient in UI, API, and database testing.

I'm proficient in TypeScript, Java, C#, and Python-based testing frameworks, including Playwright and Selenium WebDriver. Additionally, I have hands-on experience with CI/CD tools such as GitHub Actions, Azure Pipelines, Jenkins, GoCD, and Bitbucket Pipelines. Learn more about me from my [Portfolio](https://antonrosh.dev).

## Repository Structure

This repository is organized as follows:

```bash
root/
├── api/ # Reserved for future API tests
├── ui/
│ ├── pages/ # Contains UI page objects
│ │ ├── home_page.py # Page object for the home page
│ │ └── login_page.py # Page object for the login page
│ ├── tests/ # Contains UI test cases
│ │ ├── test_home_page.py # Test cases for the home page
│ │ └── test_login_page.py # Test cases for the login page
├── .env # Environment variables (excluded from Git)
├── .gitignore # Files and directories excluded from Git
├── README.md # Project documentation
├── requirements.txt # Project dependencies
└── ... # Additional project files
```

## Setting Up and Installation

For setting up the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/antonrosh/disney-python-playwright
   ```

2. Create a .env file at the root of the project directory. This file is used to store sensitive information and is not tracked by git. You'll need to add any necessary environment variables here. The following variables are required:

   ```bash
   BASE_URL=https://www.disneyplus.com/
   USERNAME= # Your Disney+ username
   PASSWORD= # Your Disney+ password
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### API Tests

The `api` directory is currently empty and is reserved for future API tests.

### UI Tests

To run the UI tests, use the following command:

```bash
pytest -n auto
```

The UI tests include test cases for the home page and login page. The test files are located in the ui/tests directory. You can modify and add more test cases as needed.

## GitHub Actions Integration

A GitHub Actions workflow file will be added in the future to run tests automatically upon each code change. To integrate the project with GitHub Actions and run the tests automatically on each code change, you can create a workflow file (e.g., .github/workflows/tests.yml).

## Run in Docker

Instructions to run the project in a Docker container will be provided soon.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Future Additions

This project is a work in progress, and in the future, I plan to add:

- Setting up a CI pipeline using GitHub Actions. ✅
- Using Docker containers for environment consistency. ✅
- Implementing API tests for comprehensive coverage.
- Enhancing the UI tests to cover more scenarios.
- Incorporating performance testing using tools such as JMeter or Locust.

## Contact

If you have any questions or wish to discuss potential collaborations, feel free to reach out:

- Email: me@antonrosh.dev
- Website: www.antonrosh.dev
- LinkedIn: www.linkedin.com/in/antonrosh
- GitHub: www.github.com/antonrosh
- Schedule a meeting: www.calendly.com/your-sdet-is-anton-rosh
