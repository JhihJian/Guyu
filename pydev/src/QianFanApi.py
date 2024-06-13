
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

# 调用默认模型，ERNIE-Lite-8K-0922（即ERNIE-Bot-turbo）
resp = chat_comp.do(messages=[{
    "role": "user",
    "content": "你好"
}])

print(resp["body"])