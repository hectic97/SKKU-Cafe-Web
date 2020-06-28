import json
with open('Tr.json', encoding='iso-8859-1') as f:
    json_data = jason.load(f, encoding='uft-8')
    for i in range(len(json_data)):
        for j in json_data[i]['sentence']:
            print(j.encode('iso-8859-1').decode('euc-kr', 'ignore'))
