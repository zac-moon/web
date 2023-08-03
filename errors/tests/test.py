import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt
import subprocess
from bs4 import BeautifulSoup


class HTMLViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Linker")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.title_label = QLabel(central_widget)
        self.title_label.setMaximumHeight(30)  # Set the maximum height to 30 (adjust as needed)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)

        self.directory_entry = QLineEdit(central_widget)
        self.directory_entry.setPlaceholderText("Enter Site URL : ")
        self.directory_entry.returnPressed.connect(lambda: self.load_html(self.directory_entry.text()))
        layout.addWidget(self.directory_entry)

        load_button = QPushButton("Load Site", central_widget)
        load_button.clicked.connect(lambda: self.load_html(self.directory_entry.text()))
        layout.addWidget(load_button)

        self.web_view = QWebEngineView(central_widget)
        layout.addWidget(self.web_view)
        self.web_view.loadFinished.connect(self.on_web_view_load_finished)

        self.show()

    def on_web_view_load_finished(self, ok):
        if ok:
            pass

    def load_html(self, directory_path):
        split_path = []
        split_path += directory_path.split('.')
        if directory_path == "/start/":
            print('start')
        elif len(split_path) == 1:
            refsars = 'errors/' + split_path[0] + '.html'
        elif split_path[1] == "errors":
            refsars = 'errors/' + split_path[0] + '.html'
        elif len(split_path) == 2:
            print('Straight Domain')
            refsars = directory_path + "/index.html"
        elif len(split_path) == 3:
            print("Subdomain")
            refsars = split_path[1] + '.' + split_path[2] + '/' + split_path[0] + '/index.html'
        elif len(split_path) == 4:
            print('Sub Subdomain')
            refsars = split_path[2] + "." + split_path[3] + '/' + split_path[1] + "/" + split_path[0] + "/index.html"

        try:
            with open(refsars, "r") as file:
                source = file.read()
                self.web_view.setHtml(source)

                # Get the title from the loaded HTML using BeautifulSoup
                soup = BeautifulSoup(source, 'html.parser')
                title = soup.title.string.strip()

                # Update the title label
                self.title_label.setText(title)

                if directory_path == "eng.start.web.com":
                    print('SPECIAL - Start Engine Function')
                    script_name = "eng.py"
                    script_path = os.path.join("web.com", "start", "eng", script_name)

                    try:
                        subprocess.run(["python3", script_path], check=True)
                    except FileNotFoundError:
                        print(f"Error: Python interpreter not found. Make sure Python is installed.")
                    except subprocess.CalledProcessError as e:
                        print(f"Error: {e}")
                    except Exception as e:
                        print(f"Unexpected Error: {e}")

        except FileNotFoundError:
            print("Error: 404 URL Not Found")
            self.redirect('404.errors')
        except Exception as e:
            print(f"Error occurred: {e}")

    def redirect(self, to_load):
        self.load_html(to_load)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = HTMLViewer()
    sys.exit(app.exec_())
