from functions.functions_for_work import FunctionsForWork
from functions.function_for_work_firefox import FunctionsForWorkFirefox


class LocatorsAndNames:
    """Класс локаторов элементов страницы"""
    XPATH_ELEMENT1 = "//*[text()='Elements']"
    XPATH_ELEMENT_MAIN_HEADER = "//*[@class='main-header']"
    XPATH_ELEMENT3 = "//span[text()='Check Box']"
    XPATH_ELEMENT_HOME = "//*[@id='tree-node']/ol/li/span/button"
    XPATH_ELEMENT_HOME_DIRECTORY = "//*[@id='tree-node']/ol/li/ol"
    XPATH_ELEMENT_DOWNLOWDS = "//*[@id='tree-node']/ol/li/ol/li[3]/span/button"
    XPATH_ELEMENT_DOWNLOWDS_DIRECTORY = "//*[@id='tree-node']/ol/li/ol/li[3]/ol"
    XPATH_ELEMENT_WORDFILE = "//*[@id='tree-node']/ol/li/ol/li[3]/ol/li[1]/span/label"
    XPATH_ELEMENT_WORDFILE_NOTIFICATION_TEXT_PART1 = "//*[@id='result']/span[1]"
    XPATH_ELEMENT_WORDFILE_NOTIFICATION_TEXT_PART2 = "//*[@id='result']/span[2]"

    ELEMENT_TEXT1 = 'Elements'
    ELEMENT_TEXT2 = 'Check Box'
    ELEMENT_TEXT3 = 'You have selected :wordFile'


class StepsOfTask:
    @staticmethod
    def task_steps():
        el = LocatorsAndNames()
        step = FunctionsForWorkFirefox()
        step.element_click(element_xpath=el.XPATH_ELEMENT1),
        step.element_text(element_xpath=el.XPATH_ELEMENT_MAIN_HEADER, element_name=el.ELEMENT_TEXT1)
        step.element_click(element_xpath=el.XPATH_ELEMENT3)
        step.element_text(element_xpath=el.XPATH_ELEMENT_MAIN_HEADER, element_name=el.ELEMENT_TEXT2)
        step.element_click(element_xpath=el.XPATH_ELEMENT_HOME)
        step.check_element_find(element_xpath=el.XPATH_ELEMENT_HOME_DIRECTORY, element='Директория Home')
        step.element_click(element_xpath=el.XPATH_ELEMENT_DOWNLOWDS)
        step.check_element_find(element_xpath=el.XPATH_ELEMENT_DOWNLOWDS_DIRECTORY, element='Директория Downlowds')
        step.element_click(element_xpath=el.XPATH_ELEMENT_WORDFILE)
        step.element_text_special(element_xpath1=el.XPATH_ELEMENT_WORDFILE_NOTIFICATION_TEXT_PART1,
                                  element_xpath2=el.XPATH_ELEMENT_WORDFILE_NOTIFICATION_TEXT_PART2,
                                  element_name=el.ELEMENT_TEXT3)
        step.close_driver()


class StepsOfTaskFirefox:
    @staticmethod
    def task_steps_firefox():
        el = LocatorsAndNames()
        step = FunctionsForWork()
        step.element_click(element_xpath=el.XPATH_ELEMENT1),
        step.element_text(element_xpath=el.XPATH_ELEMENT_MAIN_HEADER, element_name=el.ELEMENT_TEXT1)
        step.element_click(element_xpath=el.XPATH_ELEMENT3)
        step.element_text(element_xpath=el.XPATH_ELEMENT_MAIN_HEADER, element_name=el.ELEMENT_TEXT2)
        step.element_click(element_xpath=el.XPATH_ELEMENT_HOME)
        step.check_element_find(element_xpath=el.XPATH_ELEMENT_HOME_DIRECTORY, element='Директория Home')
        step.element_click(element_xpath=el.XPATH_ELEMENT_DOWNLOWDS)
        step.check_element_find(element_xpath=el.XPATH_ELEMENT_DOWNLOWDS_DIRECTORY, element='Директория Downlowds')
        step.element_click(element_xpath=el.XPATH_ELEMENT_WORDFILE)
        step.element_text_special(element_xpath1=el.XPATH_ELEMENT_WORDFILE_NOTIFICATION_TEXT_PART1,
                                  element_xpath2=el.XPATH_ELEMENT_WORDFILE_NOTIFICATION_TEXT_PART2,
                                  element_name=el.ELEMENT_TEXT3)
        step.close_driver()
