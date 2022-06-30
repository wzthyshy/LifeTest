"""

"""
from api.base_api import BaseApi


class Cooperate(BaseApi):
    """
    合作类型的API类
    """
    load_data = BaseApi.load_yaml("data/company/cooperate_api.yml")

    def __init__(self):
        super().__init__()

    def creat_type(self):
        pass

    def update_type(self):
        pass

    def search_type_by_id(self):
        pass

    def search_type_by_comid(self):
        pass

    def delete_type(self):
        pass


if __name__ == "__main__":
    a = Cooperate()
    print(a.creat_type())