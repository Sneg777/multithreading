import os
import shutil
import logging
from threading import Thread

def copy_file(filepath, target_folder, file_extension):

    extension_folder = os.path.join(target_folder, file_extension)


    if not os.path.exists(extension_folder):
        os.makedirs(extension_folder)
        logging.info(f'Folder {extension_folder} created')


    shutil.copy2(filepath, extension_folder)
    logging.info(f"File {os.path.basename(filepath)} copied to the folder {extension_folder}")

def sort_files_by_extension(source_folder, target_folder):
    if not os.path.exists(source_folder):
        logging.info(f'Folder {source_folder} does not exist')
        return

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        logging.info(f'Folder {target_folder} created')


    threads = []


    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            filepath = os.path.join(root, filename)


            if os.path.isfile(filepath):

                file_extension = os.path.splitext(filename)[1].lower()

                if file_extension == '':
                    file_extension = 'no_extension'
                else:
                    file_extension = file_extension[1:]

                thread = Thread(target=copy_file, args=(filepath, target_folder, file_extension))
                threads.append(thread)
                thread.start()

    for thread in threads:
        thread.join()
        logging.info(f"Thread {thread.name} finished")

    logging.info("All files copied successfully.")

if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    source_folder = 'picture'
    target_folder = 'sorted_pictures'

    sort_files_by_extension(source_folder, target_folder)
