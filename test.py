import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

def get_folders_in_directory(path):
    all_items = os.listdir(path)
    folders = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    return folders

def process_input(input_text):
    split_query = input_text.split()

    if input_text.startswith("http://") or input_text.startswith("https://"):
        display_html(input_text)
    else:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        folders = get_folders_in_directory(current_directory)
        unwanted_folders = ["errors", ".git"]
        folders = [folder_name for folder_name in folders if folder_name not in unwanted_folders]

        num_folders = len(folders)
        result_folders = []

        for folder_name in folders:
            try:
                with open(os.path.join(folder_name, 'bot'), 'r') as r:
                    botCur = r.read()

                botSplit = botCur.split()

                if any(word in botSplit for word in split_query):
                    result_folders.append(folder_name)
            except FileNotFoundError:
                pass

        display_results(result_folders)

def display_html(html_content):
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    main_win.setWindowTitle("Linker")
    main_win.setGeometry(100, 100, 800, 600)

    central_widget = QWidget(main_win)
    main_win.setCentralWidget(central_widget)
    directory_entry = QLineEdit(central_widget)
    directory_entry.setPlaceholderText("Enter Site URL : ")
    directory_entry.returnPressed.connect(lambda: process_input(directory_entry.text()))
    load_button = QPushButton("Load Site", central_widget)
    load_button.clicked.connect(lambda: process_input(directory_entry.text()))
    text_browser = QTextBrowser(central_widget)
    layout = QVBoxLayout()
    layout.addWidget(directory_entry)
    layout.addWidget(load_button)
    layout.addWidget(text_browser)
    central_widget.setLayout(layout)

    def redirect(toload):
        process_input(toload)

    def load_html(directory_path):
        split_path = []
        split_path += directory_path.split('.')
        if len(split_path) == 1:
            refsars = 'errors/' + split_path[0] + '.html'
        elif split_path[1] == "errors":
            refsars = 'errors/' + split_path[0] + '.html'
        elif len(split_path) == 2:
            print('Sraight Domain')
            refsars = directory_path + "/index.html"
        elif len(split_path) == 3:
            print("Subdomain")
            refsars = split_path[1] + '.' + split_path[2] + '/' + split_path[0] + '/index.html'

        try:
            with open(refsars, "r") as file:
                source = file.read()
                text_browser.setHtml(source)

                web_view = QWebEngineView()
                web_view.setHtml(source)
                web_view.loadFinished.connect(lambda _: set_window_title(web_view, directory_path))
        except FileNotFoundError:
            print("Error: 404 URL Not Found")
            redirect('404.errors')
        except Exception as e:
            print(f"Error occurred: {e}")

    def set_window_title(web_view, directory_path):
        title = web_view.page().title()
        if not title:
            title = os.path.basename(os.path.normpath(directory_path))
        main_win.setWindowTitle(title)

    def display_results(folders):
        text_browser.clear()
        if folders:
            text_browser.append("Matching Folders:")
            text_browser.append("\n".join(folders))
        else:
            text_browser.append("No matching folders found.")
    
    main_win.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    process_input("")
