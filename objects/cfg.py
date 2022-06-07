from dotenv import load_dotenv
from os import getcwd, getenv

load_dotenv(getcwd() + '/.env')

class _env:
    def __init__(self):
        for env_name in ('app_name', 'domain', 'target', 'debug'):
            setattr(self, env_name, getenv(env_name))

env = _env()
