import urllib.request
import argparse
import os.path

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

def download_girl_assets(path:str):
    print("downloading girl assets. Storing them to:", path)
    girl_download_path = os.path.join(path, "girls")
    girl_url_path = os.path.join(base_url, version,resource_path, "Girl")
    girl_filename_format = "G{index}N_SP"
    # We create a folder for all the girls
    if not os.path.exists(girl_download_path):
        os.makedirs(girl_download_path)
    # We start loop. Stopping when hitting an error
    continue_flag = True
    # Starts at 1
    girl_index = 1
    while continue_flag:
        # We create folder for said girl
        if not os.path.exists(os.path.join(girl_download_path, str(girl_index))):
            os.makedirs(os.path.join(girl_download_path, str(girl_index)))
        current_girl_folder = os.path.join(girl_download_path, str(girl_index))
        girl_filename = girl_filename_format.format(index=girl_index)
        girl_filename_webp = girl_filename + ".webp"
        girl_filename_atlas = girl_filename + "_atlas.txt"
        girl_filename_json = girl_filename + ".json"
        # https://monmusu.pro.g123-cpp.com/3.5.15/resource/assets/mwnres/Lihui/Girl/G215N_SP.webp
        try:
            print("downloading:" ,os.path.join(girl_url_path, girl_filename_webp))
            urllib.request.urlretrieve(os.path.join(girl_url_path, girl_filename_webp),  os.path.join(current_girl_folder,girl_filename_webp))
            print("downloading: ", os.path.join(girl_url_path, girl_filename_atlas))
            urllib.request.urlretrieve(os.path.join(girl_url_path, girl_filename_atlas),  os.path.join(current_girl_folder,girl_filename_atlas))
            print("downloading :", os.path.join(girl_url_path, girl_filename_json))
            urllib.request.urlretrieve(os.path.join(girl_url_path, girl_filename_json),  os.path.join(current_girl_folder,girl_filename_json)) 
            girl_index += 1
        except urllib.error.HTTPError as e:
            print(e)
            if girl_index < 75:
                print("We asume here that its a forbidden girl that has not been released...yet. And we know there is around 60 girls. So we continue")
                girl_index += 1
            else:
                continue_flag = False
def download_allies_assets(path:str):
    print("downloading ally assets. Storing them to:", path)
    ally_download_path = os.path.join(path, "allies")
    ally_url_path = os.path.join(base_url, version,resource_path, "Partner")
    ally_filename_format = "P{index}_SP"
    # We create a folder for all the girls
    if not os.path.exists(ally_download_path):
        os.makedirs(ally_download_path)
    # We start loop. Stopping when hitting an error
    continue_flag = True
    # Starts at 1
    girl_index = 1
    while continue_flag:
        # We create folder for said girl
        if not os.path.exists(os.path.join(ally_download_path, str(girl_index))):
            os.makedirs(os.path.join(ally_download_path, str(girl_index)))
        current_ally_folder = os.path.join(ally_download_path, str(girl_index))
        ally_filename = ally_filename_format.format(index=girl_index)
        ally_filename_webp = ally_filename + ".webp"
        ally_filename_atlas = ally_filename + "_atlas.txt"
        ally_filename_json = ally_filename + ".json"
        try:
            print("downloading:" ,os.path.join(ally_url_path, ally_filename_webp))
            urllib.request.urlretrieve(os.path.join(ally_url_path, ally_filename_webp),  os.path.join(current_ally_folder,ally_filename_webp))
            print("downloading: ", os.path.join(ally_url_path, ally_filename_atlas))
            urllib.request.urlretrieve(os.path.join(ally_url_path, ally_filename_atlas),  os.path.join(current_ally_folder,ally_filename_atlas))
            print("downloading :", os.path.join(ally_url_path, ally_filename_json))
            urllib.request.urlretrieve(os.path.join(ally_url_path, ally_filename_json),  os.path.join(current_ally_folder,ally_filename_json)) 
            girl_index += 1
        except urllib.error.HTTPError as e:
            print(e)
            if girl_index < 75:
                print("We asume here that its a forbidden ally that has not been released or some weird funcky indexing (it jumps sometimes)")
                girl_index += 1
            else:
                continue_flag = False

if __name__ == '__main__':
    os.path.join(os.getcwd(), "download")
    default_download_path = os.path.join(os.getcwd(), "download")
    print("hello fellow degens. The path for the download is", default_download_path)
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=str, help='A destination for the download of assets of the game', default=default_download_path)
    args = parser.parse_args()
    download_girl_assets(args.folder)
    download_allies_assets(args.folder)
