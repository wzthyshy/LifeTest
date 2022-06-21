"""

"""
from api.my_company.companies import Company


class TestCompany():
    """

    """
    company = Company()

    # 获取参数化的数据
    para_data = company.load_yaml("data/company/para_company.yml")

    # 获取不同用例需要的参数化数据以及ids标题数据
    add_data = para_data["add"]["data"]
    add_ids = para_data["add"]["ids"]

    get_data = para_data["get"]["data"]
    get_ids = para_data["get"]["ids"]

    delete_data = para_data["delete"]["data"]
    delete_ids = para_data["delete"]["ids"]

    edit_data = para_data["edit"]["data"]
    edit_ids = para_data["edit"]["ids"]

    def test_list(self):
        pass

    def test_creat_company(self):
        pass

    def test_update_company(self):
        pass

    def test_search_company(self):
        pass
