import requests
import os
import urllib.parse

def download_file(url, new_filename='Cracky2DPlatformer.zip'):
    try:
        download_dir = os.path.expanduser("~/Downloads")
        parsed_url = urllib.parse.urlparse(url)
        filename = os.path.basename(parsed_url.path)
        filename = os.path.splitext(filename)[0] + '.zip'

        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)

            os.rename(filename, download_dir + '/' + new_filename)

            print('The file has been downloaded successfully, check your default download directory.')
        else:
            print('The file could not be downloaded.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

def main():

    url = 'https://u.gamepowerx.com/api/d/7z8Cgn5'

    download_file(url)

if __name__ == '__main__':
    main()
