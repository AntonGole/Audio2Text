import os
import shutil


def remove_temp_files():
    """
    Remove all temporary files in the 'temp' directory.
    If 'temp' directory doesn't exist, create it.
    """
    # Check if the 'temp' directory exists
    if os.path.isdir('temp'):
        # Iterate through each file in the 'temp' directory
        for filename in os.listdir('temp'):
            file_path = os.path.join('temp', filename)
            try:
                # If the file is a regular file or a symbolic link, delete it
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                # If the file is a directory, delete it using 'shutil.rmtree'
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
    else:
        os.mkdir('temp')
