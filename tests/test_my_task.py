import pytest
from functions.execution_steps import StepsOfTask
from functions.execution_steps import StepsOfTaskFirefox


def test_task_steps_chrome():
    x = StepsOfTask
    x.task_steps()


def test_task_steps_firefox():
    y = StepsOfTaskFirefox
    y.task_steps_firefox()


if __name__ == '__main__':
    pytest.main()
