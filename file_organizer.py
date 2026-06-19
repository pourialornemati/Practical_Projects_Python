# import modules and global variable
from pathlib import Path
import shutil

base_dir = Path(r"Enter Your Path Here")
target_dir = base_dir / "sorted"


# declare categories and extensions
FILE_CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
}


# create directories based on categories
def create_category_directories():
    for category, _ in FILE_CATEGORIES.items():
        (target_dir / category).mkdir(parents=True, exist_ok=True)


# searching and categorizing files
def search_and_categorize_files():
    for file in base_dir.rglob("*"):
        for category, extentions in FILE_CATEGORIES.items():
            if file.suffix in extentions:
                try:
                    shutil.copy(file, target_dir / category)
                except shutil.SameFileError:
                    pass


# run the application
create_category_directories()
search_and_categorize_files()