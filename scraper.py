import json
import os
import re
import requests
from bs4 import BeautifulSoup
from requests.utils import quote

from utils import make_dir, download_image, clean_scientific_name, clean_common_names

categories = [
    { 'name': 'Alpine Flora', 'url': 'alpineflora' },
    { 'name': 'Amphibians', 'url': 'amphibians' },
    { 'name': 'Birds', 'url': 'birds' },
    { 'name': 'Butterflies and Moths', 'url': 'butterflies-moths' },
    { 'name': 'Ferns', 'url': 'ferns' },
    { 'name': 'Fungi', 'url': 'fungi' },
    { 'name': 'Insects', 'url': 'insects' },
    { 'name': 'Lichens', 'url': 'lichens' },
    { 'name': 'Mammals', 'url': 'mammals' },
    { 'name': 'Reptiles', 'url': 'reptiles' },
    { 'name': 'Trees', 'url': 'trees' },
    { 'name': 'Wildflowers', 'url': 'wildflowers' }
]

url_base = 'http://amc-nh.org'
url_head = url_base + '/resources/guides/'
url_tail = '/index.php'
output_dir = 'data'

def main():
    make_dir(output_dir)
    data = {}

    print('Scraping data from ' + url_head + '...')

    for category in categories:
        print('Starting ' + category['name'] + ' section...')
        category_dir = output_dir + '/' + category['url']
        make_dir(category_dir)
        data[category['name']] = []

        url = url_head + category['url'] + url_tail
        page = requests.get(url)

        soup = BeautifulSoup(page.text, 'lxml')
        container = soup.find('ul', class_='clGalleryList')
        items = container.find_all('li')

        for item in items:
            entry = {}
            text = item.find('div')

            # Extract scientific name
            scientific_name = text.find('em')
            for br in scientific_name.find_all('br'):
                br.replace_with(' ')
            entry['scientific_name'] = clean_scientific_name(scientific_name.text)
            scientific_name.decompose()

            # Skip if duplicate
            is_duplicate = False
            for existing_entry in data[category['name']]:
                if existing_entry['scientific_name'] == entry['scientific_name']:
                    is_duplicate = True
                    break
            if is_duplicate:
                continue

            # Extract common names
            names = text.find('a')
            *common_names, photographer = re.split(',|©\ ', names.text)
            entry['common_names'] = clean_common_names(common_names)
            entry['photographer'] = photographer

            # Extract and download image
            image = url_base + quote(item.find('a')['href'])
            backup_image = url_base + quote(item.find('img')['src'])
            extension = image[image.rfind('.'):]
            image_path = category['url'] + '/' + re.sub(r'[^\w]', '', entry['scientific_name'])
            image_path_full = output_dir + '/' + image_path + extension
            success = download_image(image, image_path_full, backup_image)
            if success:
                entry['image'] = image_path

            data[category['name']].append(entry)

        print('Finished ' + category['name'] + ' section!')

    # Store information
    with open(output_dir + '/data.json', 'w') as file:
        json.dump(data, file)

    print('Scraping complete!')

if __name__ == '__main__':
    main()

