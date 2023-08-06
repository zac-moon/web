import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import socket
import os

class WebPageMonitor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Linker")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.directory_entry = QLineEdit(self.central_widget)
        self.directory_entry.setPlaceholderText("Enter Site URL : ")
        self.directory_entry.returnPressed.connect(self.load_html)

        self.load_button = QPushButton("Load Site", self.central_widget)
        self.load_button.clicked.connect(self.load_html)

        self.text_browser = QTextBrowser(self.central_widget)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.directory_entry)
        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.text_browser)

        self.central_widget.setLayout(self.layout)

        self.web_view = QWebEngineView(self.central_widget)
        self.layout.addWidget(self.web_view)

        self.current_url = None
        self.web_view.page().urlChanged.connect(self.page_url_changed)

        self.web_view.loadFinished.connect(self.on_web_view_load_finished)


        self.show()

    def load_html(self):
        try:
            directory_path = self.directory_entry.text()

            server_address = 'localhost'  
            server_port = 60951
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_address, server_port))

            client_socket.sendall(directory_path.encode())

            html_content = client_socket.recv(4096).decode()

            client_socket.close()
            if html_content[:2]=="#py":
                print('Python Script')
                pyscript =  html_content
                try :
                    scriptC = open('pyscriptcache.py','x')
                    scriptC.close()

                    scriptE = open('pyscriptcache.py')
                    scriptE.write('')
                    scriptE.close()

                    scriptW = open('pyscriptcache.py')
                    scriptW.write(pyscript)
                    scriptW.close()
                except FileExistsError:
                    scriptE = open('pyscriptcache.py')
                    scriptE.write('')
                    scriptE.close()

                    scriptW = open('pyscriptcache.py')
                    scriptW.write(pyscript)
                    scriptW.close()

                pyscriptpath = ('pyscriptcachepy')
                subprocess.run(["python3",pyscriptpath], check=True)

                clearCache = open('pyscriptcache.py')
                clearCache.write('')
                clearCache.close()


            else: 
                self.text_browser.setHtml(html_content)
                self.web_view.setHtml(html_content)

        except Exception as e:
            print(f"Error occurred: {e}")

    def on_title_extracted(self, title):
        self.setWindowTitle(title)  

    def on_web_view_load_finished(self):
        self.web_view.page().runJavaScript("document.title", self.on_title_extracted)

    def page_url_changed(self, url):
        if url != self.current_url:
            self.current_url = url
            print("New page loaded:", url.toString())
            self.on_web_view_load_finished()  # Removed unnecessary argument



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebPageMonitor()
    sys.exit(app.exec_())
