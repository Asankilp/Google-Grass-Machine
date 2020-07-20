#谷歌全自动生草机 by Asankilp
#输入的句子将自动检测语言，并进行重复翻译。
#请使用Python3运行此程序，使用前请安装googletrans。
#使用命令：pip install googletrans来安装依赖包。
from googletrans import Translator
translator = Translator(service_urls=['translate.google.cn']) #将翻译服务URL替换为国内区域名
lang = ['de','en','ja','da','fr','ny','af','af','az','eu','ml','pl','uk','he','gl','ht','sd','es','my','zh-cn'] #翻译次数及语言
choice = input('请选择生草来源。1：单句生草；2：从文件生草')
if choice == 1;
    src2 = input('请输入原句：')
    count = 0
    for mubiao in lang:
        count = count + 1 #翻译计次
        src2 = translator.translate(src2,dest=mubiao).text
        print(str(count)+"次翻译结果："+src2)
    print("最终翻译结果："+src2)
elif choice == 2;
    #文件生草代码
else;
    print('选项无效')
