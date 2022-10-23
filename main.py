from download import Download
from platform.artstation import download_artstation
from platform.flickr import download_flickr
import os

platform = 'flickr'
num_images = 100
key_words = 'cat animal'
download = Download()
download_path = 'download'

def main(key_words='cyberpunk', platform ='flickr', num_images=10000, download_path='out') :
    exist_list = os.listdir(download_path)
    if platform == 'artstation':
        img_list = download_artstation(num_images, key_words, exist_list)
    elif platform == 'flickr':
        img_list = download_flickr(num_images, key_words, exist_list)

    print('get ' + str(len(img_list)))
    download.thread_download(img_list, download_path)

if __name__ == "__main__":
    main(key_words, platform, num_images, download_path)