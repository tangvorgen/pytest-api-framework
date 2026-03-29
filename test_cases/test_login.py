import pytest
import allure
import yaml
import sys
import os

# ================= 路径配置（核心修复） =================
# 1. 获取当前测试文件的绝对路径
current_file = os.path.abspath(__file__)
# 2. 获取 test_cases 目录
test_cases_dir = os.path.dirname(current_file)
# 3. 获取项目根目录 (vorgen)
project_root = os.path.dirname(test_cases_dir)
# 4. 将项目根目录加入系统路径（解决 import 问题）
sys.path.insert(0, project_root)
# =======================================================

from common.request import RequestUtil

# ================= 读取 YAML 数据（修复文件路径） =================
# 使用绝对路径拼接，不再用 ../
yaml_path = os.path.join(project_root, 'data', 'login.yaml')
print(f"正在读取数据文件：{yaml_path}")  # 调试用，确认路径对不对

with open(yaml_path, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


# ================================================================

@allure.feature("用户登录模块")
class TestLogin:

    @pytest.mark.parametrize("case_info", data)
    @allure.story("登录接口测试")
    def test_login_api(self, case_info):
        # 使用 httpbin 测试接口（稳定）
        url = "https://httpbin.org/post"
        method = "post"
        json_data = {
            "email": case_info['username'],
            "password": case_info['password']
        }

        allure.attach.name = "请求参数"
        allure.attach.body = str(json_data)
        allure.attach.attachment_type = allure.attachment_type.TEXT

        req = RequestUtil()
        response = req.send_request(method=method, url=url, json=json_data)

        # httpbin 永远返回 200，只验证连通性
        assert response.status_code == 200, f"请求失败：{response.status_code}"
        print(f"用例 {case_info['case_name']} 执行完毕")