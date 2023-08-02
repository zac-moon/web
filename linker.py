import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QLineEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import subprocess


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
    central_widget.setLayout(layout)\
    
    def redirect(toload):
        load_html(toload)

    def load_html(directory_path):
        split_path = []
        split_path += directory_path.split('.')
        if directory_path=="/start/":
            print('start')
        elif len(split_path) == 1:
            refsars = 'errors/'+split_path[0]+'.html'
        elif split_path[1]=="errors":
            refsars = 'errors/'+split_path[0]+'.html'
        elif len(split_path) == 2:
            print('Sraight Domain')
            refsars = directory_path + "/index.html"
        elif len(split_path) == 3:
            print("Subdomain")
            refsars = split_path[1]+'.'+split_path[2]+'/'+split_path[0]+'/index.html'
        elif len(split_path) ==4:
            print('Sub Subdomain')
            refsars = split_path[2]+"."+split_path[3]+'/'+split_path[1]+"/"+split_path[0]+"/index.html"

            '''
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
            '''



        try:
            with open(refsars, "r") as file:
                source = file.read()
                text_browser.setHtml(source)

                web_view = QWebEngineView()
                web_view.setHtml(source)
                web_view.loadFinished.connect(lambda _: set_window_title(web_view, directory_path))

                if directory_path =="eng.start.web.com":
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
            redirect('404.errors')
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