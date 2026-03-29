import requests

class RequestUtil:

    def send_request(self, method, url, **kwargs):
      """"
    :method:get,post,put 方法
    ：url:接口地址
    :kwargs:参数(json,data,headers)
    :return:响应对象
      """
      try:
          # 使用request请求
          response = requests.request(method=method, url=url, **kwargs)
          return response
      except Exception as e:
          print(f"请求发生错误：{e}")
          return None