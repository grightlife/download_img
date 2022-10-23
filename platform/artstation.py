import requests
import os
import math

detail_url = 'https://www.artstation.com/projects/'

def download_artstation(picNum, query, exist_list):
    page = int(picNum / 50) + 1
    img_list = []
    per_page = 50
    current_page = 1
    url = 'https://www.artstation.com/api/v2/search/projects.json?per_page=' + str(per_page) + '&pro_first=1&query=' + query
    while current_page <= page:
        if len(img_list) >= picNum:
            break
        request_data = requests.get(url + '&page=' + str(current_page)).json()

        print('get page:' +  str(current_page) + ', total: ' + str(math.ceil(request_data['total_count'] / per_page)))
        for item in request_data['data']:
            if len(img_list) >= picNum:
                break
            detail_data = requests.get(detail_url + item['hash_id'] + '.json').json()
            print(item['hash_id'] + ': has ' + str(len(detail_data['assets'])) + ' items')
            for image_item in detail_data['assets']:
                if len(img_list) >= picNum:
                    break
                if bool(image_item['has_image']):
                    img_url = image_item['image_url'].split('?')[0]
                    (file, ext) = os.path.splitext(img_url)
                    if (str(image_item['id']) + ext) in exist_list:
                        continue
                    img_list.append({
                        'ext': ext,
                        'id': image_item['id'],
                        'image_url': image_item['image_url'].split('?')[0],
                    })
        current_page += 1
        if per_page * current_page >= int(request_data['total_count']):
            break
    return img_list