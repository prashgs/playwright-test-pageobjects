
# Playwright python - Page Object model
Playwright is an open source web automation framework. It has bindings for many programming languages including Python. For more information about Playwright please use this [link](https://playwright.dev/python/). Page Object model is a design pattern that can be used to build UI Automation framework to be efficient and maintainable. This project implements Page Object Model using Playwright and Pytest in Python. It uses Async-API that Playwright exposes which includes auto-waits when interacting with locators.

### Installation
Playwright recommends using Playwright Pytest plugin for scripting which can be installed using pip and binaries for browsers can be installed on different operating systems using 
```
pip install pytest-playwright
pip install pytest-asyncio
pip install pytest-html
playwright install
```
Pydantic(https://pydantic-docs.helpmanual.io/) is used for data validation and conformance which can be installed using 
```
pip install pydantic
```


### Structure
- **app** - This is the parent folder which contains subfolders for model, logic and data. 
   + **config**: Configuration related to framework and application is maintained in "config.toml" file.
   + **core**: Includes "playwrightbrowser.py" which initializes Async Playwright browser object and "filedefinitions.py" which initilizes environment variables. 
   + **data**: Data used by the framework is maintained in ".json" files in this folder
   + **helpers**: "utils.py" file contains helper functions that 
   + **selectors**: All the selectors used on different pages are places in this directory as ".py" files. 
   + **models**: Data files of format ".json" is deserialized using the model provided to an object. This is used to validate data and its conformance to data model. Validation errors will result if data is missing or if data type is not same as mentioned on the model class. 
   + **pages**: Pages contains page entities of the application under test. It could be the whole page as a class or components within the page if there are many elements within a page. 
- **results** - Test results are placed here
- **test** - Contains "conftest.py" and other tests specific to application under test. "conftest.py" has fixtures that can be shared across different tests. 

## Usage
To run all tests and create html report use
```
pytest --html=./results/report.html --self-contained-html
```