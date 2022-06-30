"""

"""



import allure
import pytest

from api.my_company.departments import Departments
from common.get_log import log


class TestDepartment:
    """
    部门管理的测试方法和断言
    """

    department = Departments()
    # 获取参数化的数据
    para_data = department.load_yaml("data/company/para_department.yml")

    # 获取不同用例需要的参数化数据以及ids标题数据

    def test_search_department(self):
        pass

    def test_creat_department(self):
        pass

    def test_update_department(self):
        pass

    def test_delete_department(self):
        pass

    def test_search_department_by_id(self):
        pass