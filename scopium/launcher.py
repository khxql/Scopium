# this is used to automate the process of running selenium supported browsers;
# focusing on compatibility, performance, reliability, and stability.

from .exceptions import UnsupportedBrowser
from .browsers   import CHROME, EDGE, OPERA

# common selenium imports
from selenium import webdriver

# for chrome
from selenium.webdriver.chrome.service  import Service as ChromeService
from selenium.webdriver.chrome.options  import Options as ChromeOptions
from webdriver_manager.chrome           import ChromeDriverManager

# for edge
from selenium.webdriver.edge.service    import Service as EdgeService
from selenium.webdriver.edge.options    import Options as EdgeOptions
from webdriver_manager.microsoft        import EdgeChromiumDriverManager

# for opera
from selenium.webdriver.chrome          import service as OperaService
from selenium.webdriver.chrome.options  import Options as OperaOptions
from webdriver_manager.opera            import OperaDriverManager


class Scopium:

    selenium_supported = [CHROME, EDGE, OPERA]


    def __init__(self, name, headless=True):

        self.name = name.capitalize()
        self.headless = headless

        if self.name not in self.selenium_supported:
            raise UnsupportedBrowser(f"{name} is not supported by Scopium")


    def _add_options(self, options_class):

        # disable logging
        options_class.add_experimental_option("excludeSwitches", ["enable-logging"])
        options_class.add_argument("--log-level=3")

        # customize GUI
        if self.headless:
            options_class.add_argument('--headless=old')
            options_class.add_argument('--window-size=1920,1080')

        # making browser faster and reduce possible errors
        options_class.add_argument("--disable-extensions")
        options_class.add_argument("--no-sandbox")
        options_class.add_argument('--no-first-run')
        options_class.add_argument('--no-default-browser-check')
        options_class.add_argument('--disable-notifications')

        # hide any automation fingerprints
        options_class.add_experimental_option("useAutomationExtension", False)
        options_class.add_experimental_option("excludeSwitches",["enable-automation"])


    def run(self):

        if self.name == CHROME:

            # https://github.com/SergeyPirogov/webdriver_manager?tab=readme-ov-file#use-with-chrome
            driver_path = ChromeDriverManager().install()
            service     = ChromeService(driver_path)
            options     = ChromeOptions()
            self._add_options(options)
            self.driver = webdriver.Chrome(service=service, options=options)

        elif self.name == EDGE:

            # https://github.com/SergeyPirogov/webdriver_manager?tab=readme-ov-file#use-with-edge
            driver_path = EdgeChromiumDriverManager().install()
            service     = EdgeService(driver_path)
            options     = EdgeOptions()
            self._add_options(options)
            self.driver = webdriver.Edge(service=service, options=options)

        elif self.name == OPERA:

            # https://github.com/SergeyPirogov/webdriver_manager?tab=readme-ov-file#use-with-opera
            driver_path = OperaDriverManager().install()
            service     = OperaService.Service(driver_path)
            options     = OperaOptions()
            service.start()
            options.add_experimental_option('w3c', True)
            self._add_options(options)

            self.driver = webdriver.Remote(service.service_url, options=options)

        return self.driver


__all__ = ["Scopium"]
