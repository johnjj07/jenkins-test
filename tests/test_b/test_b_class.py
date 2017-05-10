import unittest

from jenkins_test.my_module import ClassB


class TestClassB(unittest.TestCase):

    def test_method_a(self):
        self.assertEqual("method_a", ClassB().method_a())

    def test_method_b(self):
        self.assertEqual("method_b", ClassB().method_b())

    def test_failure(self):
        self.assertTrue(True)
        # self.fail()
