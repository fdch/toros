import logging
import os
from typing import Any, Dict

import toml
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


def load_config(config_path: str):
    with open(config_path) as f:
        conf = toml.load(f)

    load_dotenv("./config/.env")
    for env in ["DB_PASS"]:
        if not os.getenv(env):
            logger.warning(f"Environment variable {env} not set")

    conf["SQL"]["password"] = os.getenv("DB_PASS")
    return conf


config = load_config("./config/config.toml")
