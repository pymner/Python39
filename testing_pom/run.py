import pytest
import os
if __name__ == '__main__':
    pytest.main(['-s', './pytest_case/test_pytestCase.py', '--alluredir', './allure-results'])
    os.system('allure generate ./allure-results -o ./allure-reports --clean')

