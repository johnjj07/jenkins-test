def stringify_int(num):
    return "{}".format(num)


class MyClass(object):

    def __init__(self, my_int, my_string):
        self.my_string = my_string
        self.my_int = my_int

    def is_my_int(self, num):
        return num == self.my_int

    def is_my_string(self, val):
        return val == self.my_string

    def double_my_int(self):
        return self.my_int * 2

    def is_my_string_palindrome(self):
        return self.my_string == self.my_string[::-1]


class ClassB(object):

    def method_a(self):
        return "method_a"

    def method_b(self):
        return "method_b"

    def method_c(self):
        return "method_c"
