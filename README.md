项目简介：基于 pytest 的接口自动化框架。
技术栈：Python + Pytest + Requests + Allure + YAML。
目录结构说明
my_api_framework/
├── common/              # 公共封装层
│   └── request.py       # 封装 requests 请求
├── data/                # 测试数据层
│   └── login.yaml       # 存放测试账号密码
├── test_cases/          # 测试用例层
│   └── test_login.py    # 具体的测试脚本
├── pytest.ini           # pytest 配置文件
├── requirements.txt     # 依赖包列表
└── reports/             # 报告存放目录（手动创建）
如何运行
pytest
allure serve reports