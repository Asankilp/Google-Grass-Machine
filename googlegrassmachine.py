#谷歌全自动生草机 by Asankilp and Jerry196
#输入的句子将自动检测语言，并进行重复翻译。
from googletrans import Translator
translator = Translator(service_urls=['translate.google.cn']) #将翻译服务URL替换为国内区域名
lang = ['de','en','ja','da','fr','ny','af','af','az','eu','ml','pl','uk','he','gl','ht','sd','es','my','zh-cn'] #翻译次数及语言
choice = int(input('请选择生草来源。1：单句生草；2：从文件生草：'))
if choice == 1:
    src2 = input('请输入原句：')
    count = 0
    for mubiao in lang:
        count = count + 1 #翻译计次
        src2 = translator.translate(src2,dest=mubiao).text
        print(str(count)+"次翻译结果："+src2)
    print("最终翻译结果："+src2)
elif choice == 2:
    count2 = 0
    count3 = 0
    print('将读取脚本目录下的input.txt进行翻译。')
    Out=[]
    with open("./input.txt",encoding="utf-8") as Inputs: #打开input.txt
        for Input in Inputs:
            text = Input.split("\n")
            print('原文：'+text[0])
            count2 = 0
            for mubiao in lang:
                count2 = count2 + 1 #翻译计次
                text[0] = translator.translate(text[0],dest=mubiao).text #翻译
                print(str(count2)+'次翻译结果：'+text[0])
            Out.append(text[0]+"\n")
            with open("./output.txt",encoding="utf-8",mode="a") as Output:Output.writelines(Out) #将翻译结果写入output.txt
            count3 = count3 + 1 #段落计数
            print(str(count3)+'段翻译结果：'+text[0])
            Out=[] #重置Out值以便翻译下一段
    #with open("./output.txt",encoding="utf-8",mode="a") as Output:Output.write('--------------------------')
    print('翻译完成。共翻译了 '+str(count3)+'段。')
    print("已将翻译结果存储至output.txt。请在文件中确认。")
else:
    print('选项无效')
