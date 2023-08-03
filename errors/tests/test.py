import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
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
            pass  # No need to do anything here for now

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

    def render_html(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        self.replace_buttons_with_widgets(soup)
        self.replace_entries_with_widgets(soup)
        rendered_html = str(soup)
        self.web_view.setHtml(rendered_html)

    def replace_buttons_with_widgets(self, soup):
        buttons = soup.find_all('button')
        for button in buttons:
            button_text = button.get_text()
            button_widget = QPushButton(button_text)
            button_widget.clicked.connect(lambda _, btn=button: self.handle_button_click(btn))
            button.insert_after(button_widget)
            button.extract()

    def replace_entries_with_widgets(self, soup):
        entries = soup.find_all('entry')
        for entry in entries:
            entry_widget = QLineEdit()
            entry_widget.returnPressed.connect(lambda _, ent=entry: self.handle_entry_submit(ent, entry_widget))
            entry.insert_after(entry_widget)
            entry.extract()

    def handle_button_click(self, button_tag):
        # Handle button click event here
        print(f"Button '{button_tag.get_text()}' clicked!")

    def handle_entry_submit(self, entry_tag, entry_widget):
        # Handle entry submit event here
        entered_text = entry_widget.text()
        print(f"Entry '{entry_tag.get_text()}' submitted with text: {entered_text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = HTMLViewer()
    sys.exit(app.exec_())
