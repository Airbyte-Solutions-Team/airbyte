#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#

import pytest

pytest_plugins = ("connector_acceptance_test.plugin",)


@pytest.fixture(name="connector_config")
def connector_config_fixture(request):
    return request.config
