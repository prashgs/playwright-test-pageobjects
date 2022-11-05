import inspect
import os.path

import app.selectors as selectors
import app.data as data
import app.models as models
import app.pages as pages
import app.config as config
import results as results
from app.helpers.utils import read_data_file


class FileDefinitions:
    locators_dir = os.path.dirname(inspect.getfile(selectors))
    data_dir = os.path.dirname(inspect.getfile(data))
    models_dir = os.path.dirname(inspect.getfile(models))
    config_dir = os.path.dirname(inspect.getfile(config))
    results_dir = os.path.dirname(inspect.getfile(results))
    pages_dir = os.path.dirname(inspect.getfile(pages))

    CONFIG_FILE = os.path.join(config_dir, 'config.toml')
    DEBUG_FILE = os.path.join(results_dir, 'debug.log')

    data = read_data_file(CONFIG_FILE, type='toml')
    os.environ['HEADLESS'] = str(data['framework']['headless'])
    os.environ['BROWSER'] = str(data['framework']['browser'])
    os.environ['URL'] = str(data['application']['url'])
