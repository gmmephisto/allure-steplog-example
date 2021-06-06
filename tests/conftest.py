import io
import logging

import allure
import allure_commons
import pytest
import _pytest.logging
import _pytest.config


LOG = logging.getLogger(__name__)


@pytest.fixture
def testfixture(request):
    LOG.info("testfixture setup")
    yield
    LOG.info("testfixture teardown")


class AllureLogStep:
    def __init__(
        self, capture_handler: _pytest.logging.LogCaptureHandler = None
    ):
        self._capture_handler = capture_handler
        self._io_stack = []

    @allure_commons.hookimpl
    def start_step(self, uuid, title, params):
        if self._capture_handler:
            stream = self._capture_handler.setStream(io.StringIO())
            self._io_stack.append(stream)

    @allure_commons.hookimpl
    def stop_step(self, uuid, exc_type, exc_val, exc_tb):
        if self._capture_handler:
            previous_stream = self._io_stack.pop()
            stream = self._capture_handler.setStream(previous_stream)
            step_logs = stream.getvalue().strip()
            allure.attach(
                step_logs,
                name="log",
                attachment_type=allure.attachment_type.TEXT,
            )


@pytest.hookimpl(trylast=True)
def pytest_configure(config: _pytest.config.Config):
    logging_plugin = config.pluginmanager.get_plugin("logging-plugin")
    handler = _pytest.logging.LogCaptureHandler()
    handler.setFormatter(logging_plugin.formatter)
    handler.setLevel(logging_plugin.log_level)

    logger = logging.getLogger()
    logger.addHandler(handler)

    step_plugin = AllureLogStep(handler)
    allure_commons.plugin_manager.register(step_plugin)

    def unregister_plugin(plugin):
        def unregister():
            allure_commons.plugin_manager.unregister(plugin)

        return unregister

    config.add_cleanup(unregister_plugin(step_plugin))
