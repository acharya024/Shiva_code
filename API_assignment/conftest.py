import pytest

def pytest_addoption(parser):
    parser.addoption("--EnvName", action="store")

## this is to read the Enviornment type from command linw which user wants to execute the TCs on
@pytest.fixture(scope='session')
def get_EnvName(request):
    name_value = request.config.option.EnvName
    if name_value is None:
        pytest.skip()
    yield name_value