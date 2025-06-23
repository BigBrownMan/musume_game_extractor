import urllib.request
import argparse
import os.path
import requests

# webp URL example:
## Ally
### https://monmusu.pro.g123-cpp.com/3.5.15/resource/assets/mwnres/Lihui/Partner/P50_SP.webp
## Girl
### https://monmusu.pro.g123-cpp.com/3.5.15/resource/assets/mwnres/Lihui/Girl/G40N_SP.webp
# atlas URL example:
# https://monmusu.pro.g123-cpp.com/3.5.15/resource/assets/mwnres/Lihui/Partner/P50_SP_atlas.txt
# https://monmusu.pro.g123-cpp.com/3.5.15/resource/assets/mwnres/Lihui/Girl/G40N_SP_atlas.txt
# Json example:
# https://monmusu.pro.g123-cpp.com/3.5.15/resource/assets/mwnres/Lihui/Partner/P50_SP.json
# https://monmusu.pro.g123-cpp.com/3.5.15/resource/assets/mwnres/Lihui/Girl/G210N_SP.json

base_url = "https://monmusu.pro.g123-cpp.com" 
# This might change with time ? No idea
version = "3.5.15"
# resource path
resource_path = "resource/assets/mwnres/Lihui"

def download_girl_assets(path:str, count: int):
    print("downloading girl assets. Storing them to:", path)
    girl_download_path = os.path.join(path, "girls")
    girl_url_path = os.path.join(base_url, version,resource_path, "Girl")
    girl_filename_format = "G{index}N_SP"
    # We create a folder for all the girls
    if not os.path.exists(girl_download_path):
        os.makedirs(girl_download_path)
    # We start loop. Stopping when hitting an error
    download_loop(girl_download_path,girl_url_path, girl_filename_format, count)

def download_allies_assets(path:str, count: int):
    print("downloading ally assets. Storing them to:", path)
    ally_download_path = os.path.join(path, "allies")
    ally_url_path = os.path.join(base_url, version,resource_path, "Partner")
    ally_filename_format = "P{index}_SP"
    # We create a folder for all the girls
    if not os.path.exists(ally_download_path):
        os.makedirs(ally_download_path)
    # We start loop. Stopping when hitting an error
    download_loop(ally_download_path,ally_url_path, ally_filename_format, count)

def download_loop(download_path: str, url: str, filename_format: str, nb_of_items: int):
    continue_flag = True
    # Starts at 1
    index = 1
    # We try until we hit 300
    max = 300
    while continue_flag:
        # We create folder for said girl
        if not os.path.exists(os.path.join(download_path, str(index))):
            os.makedirs(os.path.join(download_path, str(index)))
        current_asset_folder = os.path.join(download_path, str(index))
        asset_filename = filename_format.format(index=index)
        asset_filename_webp = asset_filename + ".webp"
        asset_filename_atlas = asset_filename + "_atlas.txt"
        asset_filename_json = asset_filename + ".json"
        try:
            print("downloading:" ,os.path.join(url, asset_filename_webp))
            urllib.request.urlretrieve(os.path.join(url, asset_filename_webp),  os.path.join(current_asset_folder,asset_filename_webp))
            print("downloading: ", os.path.join(url, asset_filename_atlas))
            urllib.request.urlretrieve(os.path.join(url, asset_filename_atlas),  os.path.join(current_asset_folder,asset_filename_atlas))
            print("downloading :", os.path.join(url, asset_filename_json))
            urllib.request.urlretrieve(os.path.join(url, asset_filename_json),  os.path.join(current_asset_folder,asset_filename_json)) 
            index += 1
        except urllib.error.HTTPError as e:
            print(e)
            # The API returns ALWAYS a 403 when hitting a not existing asset. This make making a good downloader kinda hard.
            # delete the folder
            os.rmdir(current_asset_folder)
            # Get the count
            dir_count = count_nb_folders(download_path)
            print(dir_count)
            if dir_count < nb_of_items or index <= max:
                print("We asume here that its a forbidden ally that has not been released or some weird funcky indexing (it jumps sometimes). Current is: ", index, "targeted: ", nb_of_items, " max is: ", max)
                index += 1
            else:
                continue_flag = False

def count_nb_folders(path: str):
    folders = 0
    for _, dirnames, _ in os.walk(path):
        folders += len(dirnames)
    return folders

if __name__ == '__main__':
    os.path.join(os.getcwd(), "download")
    default_download_path = os.path.join(os.getcwd(), "download")
    print("hello fellow degens. The path for the download is", default_download_path)
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=str, help='A destination for the download of assets of the game', default=default_download_path)
    parser.add_argument('--girl-count', type=int, help='The number of girls in the game currently', default=70)
    parser.add_argument('--ally-count', type=int, help='The number of allies in the game currently', default=132)
    args = parser.parse_args()
    download_girl_assets(args.folder, args.girl_count)
    download_allies_assets(args.folder, args.ally_count)
