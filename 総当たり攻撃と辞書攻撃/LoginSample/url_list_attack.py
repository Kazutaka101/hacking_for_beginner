import requests

BASE_URL = ("http://localhost:8080/")
WORD_LIST = ('./directory-list-2.3-small.txt')
dir_words = [] 
response = requests.get(BASE_URL)

#①　ディレクトリリストを、リストに入れる
with open(WORD_LIST) as f:
    for line in f:
        if line[0] != '#':
            line = line.replace('\n', '')
            dir_words.append(line)

def dir_attack():
    list_len = len(dir_words)
    for i in range(list_len):
        url = BASE_URL + dir_words[i]
        #②  レスポンスを送信して、エラーだった場合は、飛ばす。
        try:
            response = requests.get(url)
        except:
            continue
        #③  レスポンスステータスコードが、200(OK)ならurlを出力
        #404なら飛ばす。それ以外なら出力する 
        if response.status_code == 200:
            print(f'{response.status_code}:{url}')
        elif response.status_code == 404:
            continue
        else:
            print(f'{response.status_code}:{url}')

dir_attack()
