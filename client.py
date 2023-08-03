import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import socket

def display_html(html_content):
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    main_win.setWindowTitle("Linker")
    main_win.setGeometry(100, 100, 800, 600)

    central_widget = QWidget(main_win)
    main_win.setCentralWidget(central_widget)
    directory_entry = QLineEdit(central_widget)
    directory_entry.setPlaceholderText("Enter Site URL : ")
    directory_entry.returnPressed.connect(lambda: load_html(directory_entry.text()))
    load_button = QPushButton("Load Site", central_widget)
    load_button.clicked.connect(lambda: load_html(directory_entry.text()))
    text_browser = QTextBrowser(central_widget)
    layout = QVBoxLayout()
    layout.addWidget(directory_entry)
    layout.addWidget(load_button)
    layout.addWidget(text_browser)
    central_widget.setLayout(layout)

    def load_html(directory_path):
        try:
            server_address = 'localhost'  
            server_port = 60951
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_address, server_port))

            client_socket.sendall(directory_path.encode())

            html_content = client_socket.recv(4096).decode()

            client_socket.close()
            if html_content[:1]=='py':
                print('Run Python File')
                python_content = html_content - html_content[:1]

            text_browser.setHtml(html_content)

            web_view = QWebEngineView()
            web_view.setHtml(html_content)
            web_view.loadFinished.connect(lambda _: set_window_title(web_view, directory_path))
        except Exception as e:
            print(f"Error occurred: {e}")

    def set_window_title(web_view, directory_path):
        title = web_view.page().title()
        if not title:
            title = os.path.basename(os.path.normpath(directory_path))
        main_win.setWindowTitle(title)
    
    main_win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    display_html("")