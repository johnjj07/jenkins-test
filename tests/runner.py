import unittest

loader = unittest.defaultTestLoader.discover(".")
runner = unittest.TextTestRunner()
runner.run(loader)
