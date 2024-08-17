import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    destpath = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(destpath, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath) # Constructing the archive path for every file with the filename itself
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths="files\\a.txt", dest_dir="compressedFiles")