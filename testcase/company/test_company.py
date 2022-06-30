"""

"""
import allure
import pytest
from common.get_log import log
from api.my_company.companies import Company


class TestCompany:
    """
    部门的测试和断言
    """
    company = Company()

    # 获取参数化的数据
    para_data = company.load_yaml("data/company/para_company.yml")

    # 获取不同用例需要的参数化数据以及ids标题数据
    list_data = para_data["list"]["data"]
    list_ids = para_data["list"]["ids"]

    creat_data = para_data["creat"]["data"]
    creat_ids = para_data["creat"]["ids"]

    update_data = para_data["update"]["data"]
    update_ids = para_data["update"]["ids"]
    #
    # delete_data = para_data["delete"]["data"]
    # delete_ids = para_data["delete"]["ids"]
    #
    # edit_data = para_data["edit"]["data"]
    # edit_ids = para_data["edit"]["ids"]

    # def setup_class(self):
    #     self.company = Company()
    #     self.token = self.company.get_token()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(("code"), list_data, ids=list_ids)
    def test_list(self, code):
        log.info("-------------开始测试---------")
        res = self.company.get_list()
        print(res.json())
        log.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format("code", res.status_code))
        assert res.status_code == code

        log.info("-------------测试结束---------")

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(("code"), creat_data, ids=creat_ids)
    def test_creat_company(self, code):
        log.info("-------------开始测试---------")
        res = self.company.creat_company()
        print(res.json())
        log.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format("code", res.status_code))
        assert res.status_code == code

        log.info("-------------测试结束---------")

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(("code"), update_data, ids=update_ids)
    def test_update_company(self, code):
        log.info("-------------开始测试---------")
        res = self.company.update_company()
        print(res.json())
        log.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format("code", res.status_code))
        assert res.status_code == code

        log.info("-------------测试结束---------")

    def test_search_company(self):
        pass

    def test_get_company(self):
        pass

    def test_delete_company(self):
        pass

    def test_company_details(self):
        pass
    
