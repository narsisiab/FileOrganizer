import os
import shutil


FILE_TYPES = {
    "Images": (
        ".jpg",
        ".jpeg",
        ".png",
        ".gif"
    ),

    "Videos": (
        ".mp4",
        ".avi",
        ".mkv"
    ),

    "Documents": (
        ".pdf",
        ".docx",
        ".txt"
    ),

    "Audio": (
        ".mp3",
        ".wav"
    )
}


def is_valid_folder(path):
    return os.path.exists(path) and os.path.isdir(path)


def get_file_type(filename):

    filename = filename.lower()

    for folder, extensions in FILE_TYPES.items():

        if filename.endswith(extensions):
            return folder

    return None


def organize_files(path):

    for folder in FILE_TYPES.keys():

        os.makedirs(
            os.path.join(path, folder),
            exist_ok=True
        )

    moved_files = 0

    files = os.listdir(path)

    for file in files:

        full_path = os.path.join(
            path,
            file
        )

        if not os.path.isfile(full_path):
            continue

        target_folder = get_file_type(file)

        if not target_folder:
            continue

        destination = os.path.join(
            path,
            target_folder,
            file
        )

        try:

            shutil.move(
                full_path,
                destination)

        except Exception as e:

            print(f"Error moving {file}: {e}")

        else:

            moved_files += 1

            print(f"{file} -> {target_folder}")

    return moved_files

