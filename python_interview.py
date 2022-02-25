"""
A docstring for the problem
"""
from pprint import pprint


def my_func(*args, **kwargs):
    pass


# tuple of input, expected
TEST_CASES = [
]


def run_test(input_, expected):
    output = my_func(*input_)
    pprint(input_)
    if output == expected:
        print("Success!")
    else:
        print("Failed!")
        pprint(output)
        pprint(expected)
    print()

def run_tests():
    for test_case in TEST_CASES:
        run_test(*test_case)

if __name__ == "__main__":
    run_tests()
