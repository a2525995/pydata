# -*- coding: utf-8 -*-

from importlib import import_module

from faker import Factory
from faker.utils.loading import find_available_providers

META_PROVIDERS_MODULES = [
    "faker.providers",
    "services.properties"
]

PROVIDERS = find_available_providers(
    [import_module(path) for path in META_PROVIDERS_MODULES])

fake = Factory.create(providers=PROVIDERS)
event = fake.get_start_end()
import logging
# logger = logging.getLogger(__name__)
from common.make_log import logs

logger = logs()
logger.debug(event)
print(event)