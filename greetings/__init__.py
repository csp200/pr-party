import importlib
import os

# Automatically import all greeting modules by username
package_dir = os.path.dirname(__file__)
for filename in os.listdir(package_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        modname = filename[:-3]
        importlib.import_module(f".{modname}", package=__name__)
