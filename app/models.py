from datetime import datetime


saved_ads_id=list()

class Car:
    car_id: int
    title: str
    price: int
    km: int
    url: str
    update: str

    def print_info(self) -> None:
        return f'\
            \nId: {self.car_id} \
            \nTitle: {self.title or None} \
            \nPrice: {self.price or None} \
            \nURL: {self.url} '
        # return f'\
        #     \nCar_id: {self.car_id} \
        #     \nTitle: {self.title or None} \
        #     \nPrice: {self.price or None} \
        #     \nkm: {self.km[0] or None} \
        #     \nURL: {self.url} \
        #     \nUpdate date: {self.update}'

class newCar:
    pass