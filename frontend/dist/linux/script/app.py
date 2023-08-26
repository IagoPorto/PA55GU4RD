import webview

if __name__ == "__main__":
    # Create a WebView object
    webview = webview.WebView()

    # Load a web page into the WebView object
    webview.load("https://www.google.com")

    # Show the WebView object
    webview.show()

    # Wait for the user to close the WebView object
    webview.wait_closed()