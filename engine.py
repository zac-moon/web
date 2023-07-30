import os

query = input('Enter WEB Query : ')
split_query = query.split()

def get_folders_in_directory(path):
    all_items = os.listdir(path)
    folders = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    return folders

def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folders = get_folders_in_directory(current_directory)
    unwanted_folders = ["errors", ".git"]
    folders = [folder_name for folder_name in folders if folder_name not in unwanted_folders]

    num_folders = len(folders)

    for folder_name in folders:
        try:
            with open(folder_name + '/bot', 'r') as r:
                botCur = r.read()
            
            if any(word in botCur for word in split_query):
                print(folder_name)
        except FileNotFoundError:
            a =''

if __name__ == "__main__":
    main()
