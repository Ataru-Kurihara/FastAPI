from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Padding
from hashlib import pbkdf2_hmac
# 暗号
def encrypt(text, passPhrase):
    salt = get_random_bytes(16)
    iv = get_random_bytes(16)
    key = pbkdf2_hmac('sha256', bytes(passPhrase, encoding='utf-8'), salt, 50000, int(128/8))

    aes = AES.new(key, AES.MODE_CBC, iv)
    data = Padding.pad(text.encode('utf-8'), AES.block_size, 'pkcs7')
    encrypt

    # return {
    #     'salt': salt,
    #     'iv': iv,
    #     'encrypted': aes.encrypt(data)
    # }
    return aes.encrypt(data)

# 復号
def decrypt(encryptedData, passPhrase):
    key = pbkdf2_hmac('sha256', bytes(passPhrase, encoding='utf-8'), encryptedData['salt'], 50000, int(128/8))
    aes = AES.new(key, AES.MODE_CBC, encryptedData['iv'])
    plainText = aes.decrypt(encryptedData['encrypted'])

    return plainText.decode(encoding='utf-8')

# targetText = 'Hello World!'
# passPhrase = 'password_1234567'

# encryptedData = encrypt(targetText, passPhrase)
# decryptedText = decrypt(encryptedData, passPhrase)

# print(f'暗号化: ' + encryptedData['encrypted'].hex())
# print(f'復号化: {decryptedText}')