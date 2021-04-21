import pytest
@pytest.fixture(params=["参数1","参数2"])
def myfixture():
    print("执行myfixture,带参数%s"%request.param)