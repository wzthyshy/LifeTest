"""

"""
from api.base_api import BaseApi
from api.life import Token


token = Token.get_token()


class Company(BaseApi):
    """
      企业的API类
    """
    def list(self):
        """
        获取企业列表
        :return:返回响应体
        """
        p_data = {"ip": self.ip, "token": token}
        res = self.send_api_data("data/company/company_api.yml", p_data, "list")
        return res

    def creat_company(self):
        """
        新建企业
        :return:
        """
        pass

    def update_company(self):
        """
        修改企业
        :return:
        """
        pass

    def search_company(self):
        """
        查找员工所在企业
        :return:
        """
        pass

    def get_company(self):
        """
        获取单个企业信息
        :return:
        """
        pass

    def delete_company(self):
        """
        删除企业
        :return:
        """
        pass

    def company_details(self):
        """
        企业明细
        :return:
        """
        pass

