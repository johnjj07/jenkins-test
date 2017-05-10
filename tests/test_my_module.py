import unittest

from jenkins_test.my_module import MyClass, stringify_int, ClassB


class TestMyModule(unittest.TestCase):

    def test_stringify(self):
        v = stringify_int(11)
        self.assertEqual("11", v)

    def test_is_my_int(self):
        clazz = MyClass(11, "A String")
        self.assertTrue(clazz.is_my_int(11))

    def test_is_my_string(self):
        clazz = MyClass(11, "A String")
        self.assertTrue(clazz.is_my_string("A String"))

    def test_double_my_int(self):
        clazz = MyClass(11, "A String")
        self.assertEqual(22, clazz.double_my_int())

    def test_is_palindrome(self):
        clazz = MyClass(11, "A String")
        self.assertFalse(clazz.is_my_string_palindrome())
        klass = MyClass(11, "stop pots")
        self.assertTrue(klass.is_my_string_palindrome())
