from Lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    lis: list[str] = ["apples", "oranges", "bananas"]
    # assert that return value is what I want it to be
    assert get_first(lis) == "apples"


def test_remove_first_ret_values() -> None:
    """test that remove_first returns None"""
    lis: list[str] = ["apples", "oranges", "bananas"]
    assert remove_first(lis) == None


def test_remove_first_behavior() -> None:
    "Tests that remove first removes first element" ""
    lis: list[str] = ["apples", "oranges", "bananas"]
    remove_first(lis)
    assert lis == ["oranges", "bananas"]


def test_get_first_edge_case() -> None:
    """test that get_first works with empty list"""
    input: list[str] = []
    assert get_first(input) == ""
