import unittest


def urlify_algo(text, length):
    str_list = list(text)
    new_index = len(str_list)
    for i in reversed(range(length)):
        if str_list[i] == " ":
            str_list[new_index-3: new_index] = "%20"
            new_index -= 3
        else:
            str_list[new_index-1] = str_list[i]
            new_index -= 1
    return ''.join(str_list)

def urlify_pythonic(text, length):
    """solution using standard library"""
    return text[:length].replace(" ", "%20")


class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }
    testable_functions = [urlify_algo, urlify_pythonic()]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for args, expected in self.test_cases.items():
                actual = urlify(*args)
                assert actual == expected, f"Failed {urlify.__name__} for: {[*args]}"


if __name__ == "__main__":
    unittest.main()