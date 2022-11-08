from requests import session as RequestsSession
from app.models import saved_ads_id
from app.subito import fetch_ads, filter_new_ads


def main():
    new_ads = []

    with RequestsSession() as session:
        #Latina Disel 2000<x<8000eur x<120000km  
        url='https://www.subito.it/annunci-lazio/vendita/auto/latina/?ps=2000&pe=8000&ms=5&me=22&fu=2&gr=1&dr=2'
        #Latina Metan 2000<x<8000eur x<120000km 
        url2='https://www.subito.it/annunci-lazio/vendita/auto/latina/?ps=2000&pe=8000&ms=5&me=22&fu=7&gr=1&dr=2'

        ads = fetch_ads(session, url)
        ads2 = fetch_ads(session, url2)


        new_ads = filter_new_ads(session,ads,saved_ads_id)
        new_ads2 = filter_new_ads(session,ads2,saved_ads_id)


        print('==============\n\n\n')
        for ad in new_ads2:
            new_ads.append(ad)
            
        return new_ads