import inspect
import os.path

import app.locators as locators
import app.data as data
import app.models as models
import app.pages as pages
import app.config as config
from app.helpers.utils import read_toml


class FileDefinitions:
    locators_dir = os.path.dirname(inspect.getfile(locators))
    data_dir = os.path.dirname(inspect.getfile(data))
    models_dir = os.path.dirname(inspect.getfile(models))
    config_dir = os.path.dirname(inspect.getfile(config))
    pages_dir = os.path.dirname(inspect.getfile(pages))
    CONFIG_FILE = os.path.join(config_dir, 'config.toml')

    data = read_toml(CONFIG_FILE)
    os.environ['HEADLESS'] = str(data['framework']['headless'])
    os.environ['BROWSER'] = str(data['framework']['browser'])
    os.environ['URL'] = str(data['application']['url'])
