
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import zlib
def calculate_crc32(data):
    return zlib.crc32(data) & 0xffffffff
def decrypt_aes_cbc(encrypted_data, key, iv):
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(encrypted_data)
        return unpad(decrypted, AES.block_size)
    except Exception as e:
        return None
def generate_key_from_strings(c2_str, w1_str):
    c2_part = c2_str[4:10]  
    w1_part = w1_str[2:5]   
    combined = c2_part + w1_part
    combined_bytes = combined.encode('utf-8')
    crc32_value = calculate_crc32(combined_bytes)
    doubled = str(crc32_value) + str(crc32_value)
    key_string = doubled[:16]
    
    return key_string.encode('utf-8'), combined, crc32_value
def decrypt_file_with_key(input_filename, key, iv, output_filename=None):
   
    with open(input_filename, 'rb') as f:
        encrypted_data = f.read()
  
    decrypted_data = decrypt_aes_cbc(encrypted_data, key, iv)
    
    with open(output_filename, 'wb') as f:
        f.write(decrypted_data)
def targeted_decrypt(input_filename):
   
    c2 = "https://flare-on.com/evilc2server/report_token/report_token.php?token="
    w1 = "wednesday"
    iv_str = "abcdefghijklmnop"
    
    key, combined, crc32_val = generate_key_from_strings(c2, w1)
    iv = iv_str.encode('utf-8')
    
    print(" Parameters:")
    print(f"   c2[4:10] = '{c2[4:10]}'")
    print(f"   w1[2:5] = '{w1[2:5]}'") 
    print(f"   combined = '{combined}'")
    print(f"   CRC32 = {crc32_val}")
    print(f"   key = '{key.decode('utf-8')}'")
    print(f"   IV = '{iv_str}'")
    
    decrypt_file_with_key(input_filename, key, iv, "decrypted_playerscore.png")
targeted_decrypt("iv.png")
