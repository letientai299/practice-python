def sum_n_fast(n):
    """sum_n_fast
    Sum n first integers: 1, 2, 3, ..., n using the formula
    """
    return n * (n + 1) / 2


def sum_n_loop(n):
    """sum_n_loop
    Sum n first integers with a loop
    """
    return sum(i for i in range(1, n + 1))

# Now we try to create several test cases to test the above sum functions.
# Of course, this way of testing is just for learning python features. If I
# would like to auto generate test data for my functions, I rather using
# QuickCheck (and their port for python).

n_tests = 10
###############################################################################
#                                 Using Exec                                  #
###############################################################################
import pytest
for i in range(n_tests):
    exec("""
@pytest.mark.exec
def test{0}():
    assert sum_n_fast({1}) == sum_n_loop({1})
        """.format(i, 10 * (i + 1)))

# Run the exec tests using pytest with marker:
# pytest -m exec <file>
#
# The problem with this methods: - We have to manually indent the code
# block, and it looks just ugly. - Code is not clear and clean.

###############################################################################
#                                   Closure                                   #
###############################################################################
def make_test_func(input):
    #  @pytest.mark.closure
    def test():
        assert sum_n_fast(input) == sum_n_loop(input)
    return test

tests = [make_test_func(10 * i) for i in range(1, n_tests + 1)]

# Good:
# - Explicit
# Bad:
# - Doesn't be supported by pytest. Perhaps I don't know about it much enough
# to make it recognize my dynamic test funcs.

