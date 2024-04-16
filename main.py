import webview

def create_window():
    webview.create_window("YourApp", "https://your_domain", width=800, height=600)

if __name__ == "__main__":
    create_window()
    webview.start()
