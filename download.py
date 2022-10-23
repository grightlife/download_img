import os
import time
import threading

import requests
# from config import headers

class Download:

    def download_for_view(self, pic_src, pic_id, ext, path):
        try:
            os.mkdir(path)
        except:
            pass
        name = pic_id + ext
        try:
            img = requests.get(pic_src)
        except:
            time.sleep(3)
            img = requests.get(pic_src)
        with open(os.path.join(path, name), 'ab') as f:
            f.write(img.content)
    
    # thread download
    def thread_download(self, img_list, path):
        threads = []
        for image_item in img_list:
            pic_id = str(image_item.get('id'))
            pic_src = image_item.get('image_url')
            ext = image_item.get('ext')
            t = threading.Thread(target=self.download_for_view, args=[pic_src, pic_id, ext, path])
            threads.append(t)

        for t in threads:
            t.start()
            while True:
                # Determine the number of running threads, if it is less than 5, exit the while loop,
                # Enter the for loop to start a new process. Otherwise, it will always enter an infinite loop in the while loop
                if (threading.active_count() < 10):
                    break
        for t in threads:
            t.join()
