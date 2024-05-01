import os
import logging
import argparse
from collections import namedtuple


logging.basicConfig(filename="info.log", filemode="w", encoding="utf-8", level=20)
logger = logging.getLogger(__name__)


def bypass_directory(directory: str):
    """bypass_directory - обход переданной директории и сохранение информации о файлах и папках

    Args:
        directory (str): путь до директории
    """
    if not os.listdir(directory) or not directory:
        logger.error("Директория не существует или она пустая")

    else:
        inf = namedtuple("DATA", ["name", "extension", "is_directory", "parent_dir"])

        for dir_path, _, file_name in os.walk(directory):
            dir_inf = inf(
                os.path.basename(dir_path), None, True, os.path.dirname(dir_path)
            )
            logger.info(dir_inf)

            for file in file_name:
                file_inf = inf(
                    file.rsplit(".")[0],
                    file.rsplit(".")[1],
                    False,
                    os.path.dirname(dir_path),
                )
                logger.info(file_inf)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Folder Info",
        description="Info about folder",
        epilog="Write log file with folders and files",
    )
    parser.add_argument(
        "directory",
        metavar="path",
        type=str,
        nargs="?",
        help="Enter the path to the directory",
    )
    path = parser.parse_args()
    bypass_directory(path.directory)

