

## Paginas a abrir
## URL = "https://cargillonline.sharepoint.com/sites/CASCSA_APU_brm/A_Stocks/Forms/last_pdf_file_only.aspx"
## EXPECTED_TITLE_PART = "last_pdf_file_only"


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


URL = "https://cargillonline.sharepoint.com/sites/CASCSA_APU_brm/A_Stocks/Forms/last_pdf_file_only.aspx"
EXPECTED_TITLE_PART = "last_pdf_file_only"
TIMEOUT_SECONDS = 10


def open_page_and_assert_title(url: str, expected_title_part: str) -> None:
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        # Explicitly wait until the title CONTAINS expected text
        WebDriverWait(driver, TIMEOUT_SECONDS).until(
            EC.title_contains(expected_title_part)
        )

        print("✅ Title contains expected text")

    except TimeoutException:
        print(
            f"❌ Timeout waiting for title to contain '{expected_title_part}'. "
            f"Actual title was '{driver.title}'"
        )

    finally:
        # Browser intentionally left open for inspection
        pass


if __name__ == "__main__":
    open_page_and_assert_title(URL, EXPECTED_TITLE_PART)
