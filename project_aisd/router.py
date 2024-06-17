from new_tests import NewTests
from lk import Lk
from completed_tests import CompletedTests
from test import Test

class Router:
    def go_to_new_tests(self, info):
        return NewTests(info)
    def go_to_lk(self, info):
        return Lk(info)
    def go_to_completed_tests(self, info):
        return CompletedTests(info)
    def go_to_test(self, info, t_info):
        return Test(info, t_info)
