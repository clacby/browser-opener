import webbrowser

URL = input("Enter a URL to open: ")

def open_page(url):
    webbrowser.open(url)

if __name__ == "__main__":
    open_page(URL)