from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


URL = "https://cargillonline.sharepoint.com/sites/CASCSA_APU_brm/A_Stocks/Forms/last_pdf_file_only.aspx"


def open_page(url: str) -> None:
    options = Options()
    options.add_experimental_option("detach", True)  # keep browser open

    driver = webdriver.Chrome(options=options)
    driver.get(url)


if __name__ == "__main__":
    open_page(URL)