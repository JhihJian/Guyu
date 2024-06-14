
# 通过环境变量传递（作用于全局，优先级最低）

import os
from util.PWManager import PWManager
import qianfan
from Crypto.Cipher import AES
crypto_manager = PWManager('../../resource/pw.txt')
# 从文件中解密并读取字典
pw_dict = crypto_manager.decrypt_file_to_dict('../../resource/qianfan_key_id_data')


#通过环境变量初始化认证信息
# 方式一：【推荐】使用安全认证AK/SK鉴权
# 替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
os.environ["QIANFAN_ACCESS_KEY"] = pw_dict["ACCESS_KEY"]
os.environ["QIANFAN_SECRET_KEY"] = pw_dict["SECRET_KEY"]



chat_comp = qianfan.ChatCompletion()
input_str="麦当劳的香芋派一个，双层吉士堡一个，无糖可乐一杯"
prompt='''
我希望你能作为一个专业的营养师，为我分析我本次摄入饮食的营养情况，需要考虑到口语化的分量描述词，以及了解常见食物的营养成分。
所有的营养信息必须来自于官方营养信息表
你的回答不需要包含其他内容，严格输出为一段结构化的json格式，以下是一个示例参考。
[{"食物名称":"香芋派","分量":"一个","重量(g)":90,"能量(kcal)":260,"蛋白质(g)":1,"碳水化合物(g)":39,"脂肪(g)":11,"胆固醇(mg)":10,"钠(mg)":11,"钙(mg)":11}]。以下是我这次的饮食内容:{}
'''
# 调用默认模型，ERNIE-Lite-8K-0922（即ERNIE-Bot-turbo）
resp = chat_comp.do(messages=[{
    "role": "user",
    "content": prompt.format(input_str)
}])

print(resp["body"])