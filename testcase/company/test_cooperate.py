"""

"""



import allure
import pytest
from common.get_log import log
from api.my_company.cooperate_type import Cooperate


class TestCooperate:
    """
    合作类型的测试和断言
    """
    cooperate = Cooperate()
    # 获取参数化的数据
    para_data = cooperate.load_yaml("data/company/para_cooperate.yml")

    # 获取不同用例需要的参数化数据以及ids标题数据

    def test_creat_type(self):
        pass

    def test_update_type(self):
        pass

    def test_search_type_by_id(self):
        pass

    def test_search_type_by_comid(self):
        pass

    def test_delete_type(self):
        pass