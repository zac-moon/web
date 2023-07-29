import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


def display_html(html_content):
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    main_win.setWindowTitle("HTML Viewer")
    main_win.setGeometry(100, 100, 800, 600)

    web_view = QWebEngineView(main_win)
    main_win.setCentralWidget(web_view)

    web_view.setHtml(html_content, QUrl.fromLocalFile("."))

    main_win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    sars = input("Enter the directory path: ")
    refsars = sars + "/index.html"

    try:
        with open(refsars, "r") as file:
            source = file.read()
        print("File content read successfully:")
        print(source)

        display_html(source)

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"Error occurred: {e}")
