import json
from DESHelper import DESHelper
class PWManager:
    def __init__(self, password_file='pw.txt', encryption_key=None):
        self._password_file = password_file
        self._password = self._load_password(password_file)
        self._desHelper=DESHelper(self._password)

    def _load_password(self, password_file):
        try:
            with open(password_file, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            raise ValueError(f"Password file {password_file} not found.")

    def _pseudo_encrypt(self, data):
        return self._desHelper.encrypt(data)

    def _pseudo_decrypt(self, encrypted_data):
        return self._desHelper.decrypt(encrypted_data)

    def encrypt_dict_to_file(self, data_dict, output_file):
        # 将字典转换为JSON字符串，然后加密并保存到文件
        json_data = json.dumps(data_dict)
        encrypted_data = self._pseudo_encrypt(json_data)
        with open(output_file, 'wb') as file:
            file.write(encrypted_data)

    def decrypt_file_to_dict(self, input_file):
        # 从文件中读取加密的数据，解密并转换为字典
        with open(input_file, 'rb') as file:
            encrypted_data = file.read()
        decrypted_json = self._pseudo_decrypt(encrypted_data)
        return json.loads(decrypted_json)

    # 使用示例


# crypto_manager = PWManager('../../../resource/pw.txt')
# data_dict = {"APP_ID": "xx", "ACCESS_KEY": "xx", "SECRET_KEY": "xx"}
# # 加密字典并保存到文件
# crypto_manager.encrypt_dict_to_file(data_dict, '../../../resource/qianfan_key_id_data')
# # 从文件中解密并读取字典
# decrypted_dict = crypto_manager.decrypt_file_to_dict('../../../resource/qianfan_key_id_data')
# print(decrypted_dict)