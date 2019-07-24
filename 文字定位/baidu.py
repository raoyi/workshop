# -*- coding: UTF-8 -*-
from aip import AipOcr
 
# 定义常量
APP_ID = '11352343'
API_KEY = 'Nd5Z1NkGoLDvHwBnD2bFLpCE'
SECRET_KEY = 'A9FsnnPj1Ys2Gof70SNgYo23hKOIK8Os'
 
# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
 
# 读取图片
filePath = "test.png"
 
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
 
# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}
 
# 调用通用文字识别接口
result = aipOcr.general(get_file_content(filePath), options)
#print(result)
words_result=result['words_result']
#print(words_result)
for i in range(len(words_result)):
    print(words_result[i]['words'])
    print(words_result[i]['location'])
