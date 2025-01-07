# Scopium.

Scopium is a Python-based tool designed to automate the process of running Selenium-supported browsers handling their complicated setup. It focuses on key aspects like;

- Compatibility: Works with different browsers and versions.
- Performance: Fast and doesn't waste resources.
- Reliability: Works without errors most of the time.

With an emphasis on ensuring stability. The goal is to make browser automation smoother and more consistent, helping users automate their tasks without worrying about frequent errors or crashes. Currently, there's not much customization and options, that will be added with a good OOP structure.

### Support (not final).

- Windows 10/11.
- Selenium 4.x.
- Chrome, Edge, and Opera browsers.
- Python 3.8+.

*Currently, using Opera might raise some errors;*<br>
*Working on fixing this as soon as possible.*

### Installation.

```
pip install scopium
```

### Usage.

```python
from scopium import Scopium

# Initialize and launch Chrome (headless mode)
driver = Scopium("Chrome").run()

# Navigate to a website
driver.get("https://example.com")

# Close the browser when done
driver.quit()
```

Example with different browsers:

```python
chrome_driver = Scopium("Chrome").run()
edge_driver   = Scopium("Edge").run()
opera_driver  = Scopium("Opera").run()
```

Using unsupported browser will raise `UnsupportedBrowser` error.<br>
Can be imported through:

```py
from scopium.exceptions import UnsupportedBrowser
```

In default, browser will run in headless mode. To disable this:

```py
driver = Scopium("Chrome", headless=False).run()
```

**Default configuration:**

- Runs in headless mode.
- Window size: 1920x1080 (when headless).
- Logging disabled.
- Browser optimizations enabled.
- Automation flags hidden.

See [launcher.py](./scopium/launcher.py) `Scopium._add_options` function for full details.

### Tests.

The project is tested on Windows 11, Python 3.10.11. <br>
More tests soon Inshallah.


### Versioning.

- **v0.0.1-alpha**: First release.