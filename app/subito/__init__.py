from bs4 import BeautifulSoup

from typing import Set, Tuple, List

import re
from requests import ConnectionError as RequestsConnectionError
from requests import session as Session

from app.config import logger
from app.config import Settings
from app.models import Car, newCar
from app import saved_ads_id


def fetch_ads(session: Session, url) -> Set[Car]:
    ads = []

    logger.info('=== Starting fetch ads ===')
    
    response = session.get(url, headers={'User-Agent':Settings.DEFAULT_USER_AGENT})
    if response.status_code != 200:
        logger.critical('=== Unsuccessful attempt. '
                        'Please check url - %s '
                        'The script will be stopped ===', url)
        raise RequestsConnectionError('Unable to get urls')
    
    soup = BeautifulSoup(response.content.decode('utf-8'), "html.parser",)
    print('====== list =====')
    ads_items = soup.find_all('div', class_='item-card')
    print(len(ads_items))

    if len(ads_items) > 0:
        logger.info('=== Start processing %s ads ===', len(ads_items))
        for item in ads_items:
            car = Car()
            car.title =item.find_all('h2')[0].text or None
            car.price = item.find(class_='price').text or None
            car.url = item.find('a', href=True)['href'] or None
            car.km = item.find_all(text=re.compile('Km')) or None
            update_class = 'index-module_sbt-text-atom__ed5J9 index-module_token-caption__TaQWv index-module_size-small__XFVFl index-module_weight-semibold__MWtJJ index-module_date__Fmf-4 index-module_with-spacer__UNkQz'
            if car.url:
                car.car_id = str(car.url).split('-')[-1].split('.')[0]

            try:
                car.update = item.find('span', class_=update_class).text
            except :
                # logger.exception('=== Error during parsing a price ===')
                car.update = None
                # continue
            
            ads.append(car)
    
    result = {ad for ad in ads}
    print(type(result))
    return result


def filter_new_ads(session: Session, ads: Set[Car], saved_ads_id) -> List[newCar]:
    new_ads = []

    for ad in ads:
        if ad.car_id not in saved_ads_id:
            new_ads.append(ad)
            saved_ads_id.append(ad.car_id)
    
    return new_ads
    