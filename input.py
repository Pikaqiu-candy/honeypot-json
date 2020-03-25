import json
import os
filedir = os.getcwd()+'/scan'
filenames=os.listdir(filedir)
for filename in filenames:
    filepath = filedir+'/'+filename
    with open(filepath, 'r',encoding='utf-8') as f:
        with open('results.json', 'a') as f1:
            data = json.load(f)
            data2= data['open_ports_num']
            data1 = data['ip']
            json_str1 = json.dumps(data1)
            json_str2 = json.dumps(data2)
            if data2 == 0:
                f1.write('ip:' + json_str1 + ',' + 'open_ports_num:' + json_str2 + '\n')

            data5 = data['open_ports']
            data6 = len(data5['tcp'])
            json_str5 = json.dumps(data6)
            data7 = len(data5['udp'])
            json_str6 = json.dumps(data7)
            data3 = data['open_ports_info']
            for i in data3:
                for k in i.keys():
                    json_str3 = json.dumps(k)
                    for v in i.values():
                        data4 = v['service_name']
                        json_str4 = json.dumps(data4)

                        f1.write('ip:'+json_str1 + ',' + 'open_ports_num:'+json_str2 + ','+'tcp_num:'+json_str5 +','+ 'udp_num:'+  json_str6 + ','+ 'port:' + json_str3 + ','+'service:'+ json_str4 + '\n')
