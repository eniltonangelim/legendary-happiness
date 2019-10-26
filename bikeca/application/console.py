from bikeca.config.configuration import Configuration
from bikeca.domain.port.configuration.configurable import Configurable


class ConsoleApplication:

    def __init__(self, config: Configurable):
        self._config = config

    def main(self):
        self._config.statistic().popular_gender()


if __name__ == '__main__':
    config: Configurable = Configuration()
    app: ConsoleApplication = ConsoleApplication(config)
    app.main()
