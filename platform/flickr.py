import flickrapi
import os

API_KEY = "3e01e2339aaffd45851e54a3211cc8d1"
API_SECRET = "89f714639e495dd6"

flickr=flickrapi.FlickrAPI(API_KEY, API_SECRET, cache=True)

def download_flickr(picNum, query, exist_list):
    img_list = []
    tag = query
    try:
        photos=flickr.walk(tags=tag, extras='url_c')
    except Exception as e:
        print('Error')
    count = 1
    for photo in photos:
        print(photo)
        if count > picNum:
            break
        img_url = photo.get('url_c')
        if img_url:
            (path, filename) = os.path.split(img_url)
            (file, ext) = os.path.splitext(img_url)
            if filename in exist_list:
                continue
            img_list.append({
                'ext': ext,
                'id': filename.split('.')[0],
                'image_url': img_url
            })
            count += 1
    return img_list