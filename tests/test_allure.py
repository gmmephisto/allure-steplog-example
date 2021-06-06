import logging

import allure
import allure_test


LOG = logging.getLogger(__name__)


def test_example(testfixture):
    with allure.step("First step"):
        LOG.info("There is first step")

    LOG.info("Between steps")
    allure_test.hello()

    second = "second"
    with allure.step("Second step"):
        LOG.info("There is %s step", second)
        LOG.info("Another message in second step")

    with allure.step("Outer step"):
        LOG.info("First line outer step")
        LOG.info("Seconds line outer step")
        with allure.step("Inner step"):
            LOG.info("First line for inner step")
            LOG.info("Second line for inner step")
        LOG.info("Lets close outer step with another line")
