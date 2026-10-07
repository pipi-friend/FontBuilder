import os
import shutil
import sys
import json

def md(path=str,nam = str,tff = str):
    try:
        p=os.path.basename(tff)
        os.makedirs(path +'\\'+ nam + '/assets/minecraft/font')
        with open(path+'\\'+nam+'/pack.mcmeta','w') as f:
            f.write('{"pack":{\n        "description": "",\n            "pack_format": 9999,\n        "supported_formats": [0, 9999],\n        "min_format": 0,\n        "max_format": 9999\n    }\n}')

        with open(path+'\\'+nam+'/assets/minecraft/font/'+'default.json','w') as f:
            f.write('{\n    "providers": [\n        {\n            "type": "ttf",\n            "file": "minecraft:f_font.ttf",\n            "shift": [0, 1.0],\n                "size": 8,\n                "oversample": 6,\n                "skip": ""\n        }\n    ]\n}')

        shutil.copy(tff,path +'\\'+ nam + '/assets/minecraft/font/f_font.ttf')
        print('我们正在生成,坐和放宽')
        time.sleep(4)
        input('完成,按下任意键返回')
    except:
        print('出现问题,请将录像反馈至管理员')
        input('按下任意键返回')