

import pytest

from allure_custom.allurex import AllureCustom

def test_serve():
    AllureCustom.allure_custom()
    assert True

if __name__ == '__main__':
    """AllureCustom.serve("~/Desktop/")"""