import os


class FileFinder():
    def __init__(self) -> None:
        self.ext = (".txt", ".pdf", ".jpeg", ".png", ".jpg")
        self.file_paths = []

    def filepaths(self, folder: str) -> None:
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path, ext = os.path.splitext(root+"/"+file)
                if ext in self.ext:
                    self.file_paths.append(root+"/"+file)
