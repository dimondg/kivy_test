def load_image(image_name, image_dir_path="images"):

    import requests
    from constants import CLOUD_URL, TOKEN, CLOUD_IMG_DIR_PATH

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

    """Загрузка файла.
    savefile: Путь к файлу на Диске
    loadfile: Путь к загружаемому файлу
    replace: true or false Замена файла на Диске"""

    res = requests.get(f'{CLOUD_URL}/upload?path={CLOUD_IMG_DIR_PATH}/{image_name}&overwrite=true', headers=headers).json()

    with open(f'{image_dir_path}/{image_name}', 'rb') as f:
        try:
            requests.put(res['href'], files={'file': f})
        except KeyError:
            print(res)
