from environs import Env

env = Env()
env.read_env()


class Settings:
    DEFAULT_USER_AGENT = env.str('DEFAULT_USER_AGENT',
                                 default='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                                         '(KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36')
    CLIENT_ID = env.str('CLIENT_ID')
    CLIENT_SECRET = env.str('CLIENT_SECRET')

    LOGGER_NAME = env.str('LOG_FILENAME', default='olx_parser_log')
    LOGGING_IN_STDOUT = env.bool('LOGGING_IN_STDOUT', default=True)
    LOGGING_IN_FILE = env.bool('LOGGING_IN_FILE', default=False)
