import os
from urllib.request import urlretrieve

def make_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def download_image(image, image_path, backup_image=False):
    try:
        urlretrieve(image, image_path)
        return True
    except Exception as e:
        print('Error downloading image from: ' + image)
        if backup_image:
            print('Downloading from backup source: ' + backup_image)
            return download_image(backup_image, image_path)
        else:
            print('Download failed. No backup source.')
            return False

def clean_name(name):
    name = name.replace('u26', '')
    name = ''.join(i for i in name if not i.isdigit())
    open_paren = name.find('(')
    close_paren = name.find(')') + 1
    if open_paren != -1 and close_paren != -1:
        name = name[:open_paren] + name[close_paren:]
    name = name.lstrip().rstrip()
    return name

def clean_scientific_name(name):
    comma = name.find(',')
    if comma != -1:
        name = name[:comma]
    return clean_name(name)

def clean_common_names(names):
    clean_names = []
    for name in names:
        name = clean_name(name)
        if name != '':
            clean_names.append(name)
    return clean_names