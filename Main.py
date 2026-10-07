print('正在初始化')
from void import md
from art import text2art
import time
import sys

print('done')
print('FontBuilder是一款开源软件,用于制作MineCraft字体资源包。输入资源包路径,输入资源包名称和字体路径,然后开始使用。反馈请至https://github.com/pipi-friend/FontBuilder/issues')
print(text2art('FontBuilder'))
a = input('请输入资源包路径')
b = input('请输入字体包名称')
c = input('请输入字体路径')

md(a,b,c)

