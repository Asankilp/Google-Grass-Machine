from googletrans import Translator
translator = Translator(service_urls=['translate.google.cn'])
#谷歌全自动生草机 by Asankilp
#输入的句子将自动检测语言，并进行生草。
#请使用Python3运行此程序，使用前请安装googletrans和openssl。
#使用命令：pip install googletrans , pip install openssl
src2 = input('请输入原句：')
count = 0
lang = ['de','en','my','da','fr','ny','af','af','az','eu','ml','pl','uk','he','gl','ht','sd','es','zh-cn']
for mubiao in lang:
    count = count + 1
    src2 = translator.translate(src2,dest=mubiao).text
    print(str(count)+"次翻译结果："+src2)
print("最终翻译结果:"+src2)