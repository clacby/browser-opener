# Browser Opener (Selenium Demo)

This project is a small Python example that demonstrates how to open and validate a web page using a real browser, following a clean GitHub development workflow (branches, pull requests, and reviews).

It is intentionally simple and focused on learning good development practices.

---

## What the project does

- Opens a real browser (Google Chrome) using Selenium WebDriver
- Navigates to a hardcoded URL
- Waits explicitly for the page to load
- Verifies that the page title contains the expected text

This makes the script a minimal but realistic example of browser automation and UI validation.

---

## How the project evolved

The project was built incrementally to mirror how real software evolves:

### 1. Initial version — `webbrowser`
- Used Python’s built‑in `webbrowser` module
- Simply opened a URL in the default browser
- No interaction or validation

This version was useful for learning basic Git and GitHub workflows, but limited in capability.

### 2. Refactor to Selenium
- Replaced `webbrowser` with Selenium WebDriver
- Opened a real, controllable browser instance
- Laid the foundation for real automation (interaction, assertions, testing)

### 3. Add explicit waits and validation
- Added explicit waits using `WebDriverWait`
- Waited for the page title to appear
- Switched from exact title matching to `title_contains` for robustness

This final step made the script reliable and closer to production‑style automation.

---

## Why Selenium and explicit waits

- Selenium allows full control of the browser (not just opening a page)
- Explicit waits avoid flaky behaviour caused by slow or dynamic page loads
- Title validation provides a simple but meaningful automated check

---

## How to run

```bash
pip install selenium
python open_browser.py
