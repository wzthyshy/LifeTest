"""

"""
from api.base_api import BaseApi


class Departments(BaseApi):
    """
    部门管理的API类
    """
    load_data = BaseApi.load_yaml("data/company/department_api.yml")

    def search_department(self):
        pass

    def creat_department(self):
        pass

    def update_department(self):
        pass

    def delete_department(self):
        pass

    def search_department_by_id(self):
        pass


if __name__ == "__main__":
    a = Departments()
    print(a.creat_department())
