import os
import shutil

def download_file(filename):
    try:
        download_dir = os.path.expanduser("~/Downloads")

        shutil.copy(filename, os.path.join(download_dir, filename))
        print('Download complete, check your default Downloads folder.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

def main():
    filename = 'githubRelease.zip'

    download_file(filename)

if __name__ == '__main__':
    main()
