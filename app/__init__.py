from requests import session as RequestsSession
from app.models import saved_ads_id
from app.subito import fetch_ads, filter_new_ads


def main():
    resp = []

    with RequestsSession() as session:
        url_arr=[
            'https://www.subito.it/annunci-lazio/vendita/auto/latina/?ps=2000&pe=8000&ms=5&me=22&fu=2&gr=1&dr=2',
            'https://www.subito.it/annunci-lazio/vendita/caravan-e-camper/roma/?ps=1000&pe=3000&crt=2',
            'https://www.subito.it/annunci-lazio/vendita/caravan-e-camper/latina/?ps=1000&pe=3000&crt=2',
            'https://www.subito.it/annunci-campania/vendita/caravan-e-camper/napoli/?ps=1000&pe=3000&crt=2'
        ]

        for url in url_arr:
            ads = fetch_ads(session, url)
            new_ads =  filter_new_ads(session,ads,saved_ads_id)
            for ad in new_ads:
                resp.append(ad)

        return resp