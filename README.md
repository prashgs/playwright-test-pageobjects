
# Playwright python - Page Object model framework
Playwright is an open source web automation framework. It has bindings for many programming languages including Python. For more information about Playwright please use this [link](https://playwright.dev/python/). Page Object model is a design pattern that can be used to build UI Automation framework to be efficient and easily maintainable. This project implements Page Object Model using Playwright and Pytest in Python. It also used Async-API that Playwright exposure which includes auto-waits when interacting with locators.

### Installation
Playwright recommends using Playwright Pytest plugin for scripting which can be installed using pip and binaries for browsers can be installed on different operating systems using 
```
pip install pytest-playwright
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
   + **models**: 
   + **pages**
- **results** - Test results is placed here
- **test** - Contains "conftest.py" and other tests specific to application under test. "conftest.py" has fixtures that can be shared across different tests. 
