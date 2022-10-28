__author__ = 'rohitbabugaddeti'

import requests
import os
import sys

help_output = \
    f'''Usage: python {sys.argv[0]} URL FILENAME [DEST] [--chunk-size=<int>]

required arguments:
    URL                     URL of the file to be downloaded
    FILENAME                give a name to the file to be downloaded

optional arguments:
    DEST                    destination path where file will be downloaded, usually an existing directory
                            defaults to current working directory if unspecified
    --chunk-size=<int>      specify the chunk size for download in MegaBytes, defaults to 10MB
                            useful for large downloads

'''
args_required = 2
error_output = \
    f'''required atleast {args_required} args, passed {len(sys.argv) - 1}

please check 

python {sys.argv[0]} --help 

option for more info

'''
url = ''
file_name_to_save = 'downloaded_file'
download_dir = '.'
chunk_size = 1024 * 1024 * 10
progress_bar_len = 30


def handle_input():
    args = sys.argv.copy()
    if len(args) < args_required + 1:
        if len(args) == 2 and args[1] == '--help':
            print(help_output)
            sys.exit()
        sys.stderr.write(error_output)
        sys.exit()

    global url
    global file_name_to_save
    url = args.pop(1)
    file_name_to_save = args.pop(1)

    if len(args) == 1:
        return

    global download_dir
    download_dir = args.pop(1)

    if len(args) == 1:
        return

    if args[1].startswith('--chunk-size'):
        global chunk_size
        chunk_size = 1024 * 1024 * int(args.pop(1).split('=')[1])
        return


def download_file():
    try:
        resp = requests.get(url)
        total_length = resp.headers.get('content-length')
    except Exception:
        print('unable to fetch response from ', url)
        print("either the URL is bad or it isn't supported")
        sys.exit()

    if resp.status_code != 200:
        print('Unable to download. The server returned: ', resp.status_code)
        sys.exit()

    actual_download_dir = str(download_dir if download_dir else os.getcwd())

    with open(os.path.join(actual_download_dir, file_name_to_save), 'wb') as file_obj:
        print("\nDownload started...\n")
        if total_length is not None:
            total_length = int(total_length)
            i = 0
            for chunk in resp.iter_content(chunk_size=chunk_size):
                if chunk:
                    i += len(chunk)
                    file_obj.write(chunk)
                    done = int(progress_bar_len * i / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (progress_bar_len - done)))
                    sys.stdout.flush()
        else:
            for chunk in resp.iter_content(chunk_size=chunk_size):
                if chunk:
                    file_obj.write(chunk)
                    sys.stdout.flush()

    print("\n\n"+file_name_to_save.split('/')[-1] + " downloaded to " + actual_download_dir)


if __name__ == '__main__':
    handle_input()
    download_file()
