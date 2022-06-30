"""

"""
from api.base_api import BaseApi
from api.life import Token

# token = Token.get_token()


class Company(BaseApi):
    """
      企业的API类
    """

    load_data = BaseApi.load_yaml("data/company/company_api.yml")

    def __init__(self):
        super().__init__()

    def get_list(self):
        """
        获取企业列表
        :return:返回响应体
        """
        header = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }

        data = {
            "method": "get",
            "url": self.ip+"/companys/api/v1/companies",
            "headers": header
        }
        res = self.send_api(data)
        return res

    def creat_company(self):
        """
        新建企业
        :return:
        """
        company_data = Company.load_data["creat"]
        header = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }
        data = {
            "method": "post",
            "url": self.ip+"/companys/api/v1/companies",
            "headers": header,
            "json": company_data
        }
        res = self.send_api(data)
        return res

    def update_company(self):
        """
        修改企业
        :return:
        """
        company_data = Company.load_data["put"]
        header = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }
        data = {
            "method": "put",
            "url": self.ip + "/companys/api/v1/companies",
            "headers": header,
            "json": company_data
        }
        res = self.send_api(data)
        return res

    def search_company(self):
        """
        查找员工所在企业
        :return:
        """
        header = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }

        data = {
            "method": "get",
            "url": self.ip + "/companys/api/v1/companies/employee/{userid}",
            "headers": header
        }
        res = self.send_api(data)
        return res

    def get_company(self):
        """
        获取单个企业信息
        :return:
        """
        header = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }

        data = {
            "method": "get",
            "url": self.ip + "/companys/api/v1/companies/getCompanyById/{id}",
            "headers": header
        }
        res = self.send_api(data)
        return res

    def delete_company(self):
        """
        删除企业
        :return:
        """
        header = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }

        data = {
            "method": "delete",
            "url": self.ip + "/companys/api/v1/companies{id}",
            "headers": header
        }
        res = self.send_api(data)
        return res

    def company_details(self):
        """
        企业明细
        :return:
        """
        header = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }

        data = {
            "method": "get",
            "url": self.ip + "/companys/api/v1/companies/{id}",
            "headers": header
        }
        res = self.send_api(data)
        return res


if __name__ == "__main__":
    a = Company()
    print(a.update_company())