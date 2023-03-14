import pytest
from functions.execution_steps import StepsOfTask


def test_task_steps():
    x = StepsOfTask
    x.task_steps()


if __name__ == '__main__':
    pytest.main()
