import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

supported_locales = ["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-hans"]

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en-gb",
                     help="Choose language: ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    locale = request.config.getoption("language")

    #Checking if the chosen language is supported
    if locale not in supported_locales:
        raise pytest.UsageError("Supported --language options: ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans")
    
    browser = None
    if browser_name == "chrome":
        print("\nstart Chrome browser for test..")
        #Passing the chosen language option and starting Chrome
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': locale})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart Firefox browser for test..")
        #Passing the chosen language option and starting Firefox
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", locale)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
