
import logging
import pytest
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.info("Starting test execution...")
logger = logging.getLogger("mylogger")
logger.addHandler(logging.StreamHandler())
logger.addHandler(logging.FileHandler("test.log"))
logger.setLevel(logging.DEBUG)
loggerformatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")


@pytest.fixture
def setup():
    print("precondition")
    yield
    print("postcondition")

# @pytest.mark.skipif("False")
@pytest.mark.test
def test_1(setup):
    print("this is first test case")

@pytest.mark.xfail
@pytest.mark.test
def test_2(setup):
    # s= 5/0
    print("this is first test case")

@pytest.mark.test
def test_3():
    print("this is first test case")

@pytest.mark.test
def test_4():
    s = 5 / 0
    print("this is first test case")

@pytest.mark.test
def test_5():
    print("this is first test case")

@pytest.mark.test
def test_6():
    print("this is first test case")