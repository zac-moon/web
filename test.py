import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


def display_html(html_content):
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    main_win.setWindowTitle("Linker")
    main_win.setGeometry(100, 100, 800, 600)

    central_widget = QWidget(main_win)
    main_win.setCentralWidget(central_widget)
    directory_entry = QLineEdit(central_widget)
    directory_entry.setPlaceholderText("Enter the directory path")
    directory_entry.returnPressed.connect(lambda: load_html(directory_entry.text()))
    load_button = QPushButton("Load", central_widget)
    load_button.clicked.connect(lambda: load_html(directory_entry.text()))
    text_browser = QTextBrowser(central_widget)
    layout = QVBoxLayout()
    layout.addWidget(directory_entry)
    layout.addWidget(load_button)
    layout.addWidget(text_browser)

    central_widget.setLayout(layout)

    def load_html(directory_path):
        refsars = directory_path + "/index.html"
        try:
            with open(refsars, "r") as file:
                source = file.read()
                text_browser.setHtml(source)

                # Use QWebEngineView to extract the web page title
                web_view = QWebEngineView()
                web_view.setHtml(source)
                web_view.loadFinished.connect(lambda _: set_window_title(web_view))
        except FileNotFoundError:
            print("Error: 404 URL Not Found")
        except Exception as e:
            print(f"Error occurred: {e}")

    def set_window_title(web_view):
        title = web_view.page().title()
        main_win.setWindowTitle(title)

    main_win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    display_html("")
