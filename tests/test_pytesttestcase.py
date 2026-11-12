import pytest


#fixture
@pytest.fixture
def setup():
    #pre condition
    print("")
    print("this is setup method")
    yield
    #post condition
    print("this is tear down method")


# def test_first_case(setup):
#     print("this is first test case")
#
#
#
# def test_second_case(setup):
#     print("this is first test case")

@pytest.mark.parm
@pytest.mark.parametrize("num",[1,2,3,4])
def test_param_test(num):
    print(f"this is param test case with value: {num}")




