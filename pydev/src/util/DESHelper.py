from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


class DESHelper:
    def __init__(self, key):
        # DES密钥长度应为8字节（64位），但仅使用其中的56位
        # 如果提供的密钥长度不足或超过8字节，则需要调整
        self.key = key.encode('utf-8')[:8]
        self.cipher = DES.new(self.key, DES.MODE_ECB)  # 注意：ECB模式可能不安全，应使用更安全的模式如CBC

    def encrypt(self, plaintext):
        plaintext=plaintext.encode('utf-8')
        # 填充数据到8字节的倍数
        padded_text = pad(plaintext, DES.block_size)
        # 加密
        ciphertext = self.cipher.encrypt(padded_text)
        return ciphertext

    def decrypt(self, ciphertext):
        # 解密
        plaintext = self.cipher.decrypt(ciphertext)
        # 去除填充
        unpadded_text = unpad(plaintext, DES.block_size)
        return unpadded_text


if __name__ == "__main__":
    # 生成一个随机的8字节密钥（注意：在真实应用中，密钥应该是安全生成的）
    key = 'wsw526418'  # DES密钥应该是8字节

    # 创建一个DESHelper实例
    helper = DESHelper(key)
    # 待加密的明文
    plaintext = b"This is a secret message!"
    # 加密
    ciphertext = helper.encrypt(plaintext)
    print("Ciphertext:", ciphertext.hex())  # 将二进制数据转换为十六进制字符串以便打印
    # 解密
    decrypted_text = helper.decrypt(ciphertext)
    print("Decrypted text:", decrypted_text)