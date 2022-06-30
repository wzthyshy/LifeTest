from api.base_api import BaseApi


class Token(BaseApi):
    """
    获取登录时返回的token

    CORP_ID:企业微信的企业id
    """
    # 通过配置文件获取企业微信的id

    def get_token(self):
        """


        """
        # r = requests.post(
        #     "http://3r5z779982.wicp.vip:7000/api/authenticate",
        #     data=json.dumps({
        #         "username": "18858104920",
        #         "password": "123456",
        #         "rememberMe": "true"
        #
        #     }),
        #     headers={
        #         "Content-Type": "application/json",
        #         "Accept": "application/json"
        #
        #     }
        #
        # )

        header = {"Content-Type": "application/json"}
        json_data = {
            "username": "18858104920",
            "password": "123456",
            "rememberMe": "true"
        }
        data = {
            "method": "POST",
            "url": "http://3r5z779982.wicp.vip:7000/api/authenticate",
            "headers": header,
            "json": json_data




        }
        # 获取access_token
        res = self.send_api(data)
        self.token = res.json()["data"]["token_id"]
        return self.token


if __name__ == "__main__":
    a = Token()
    print(a.get_token())