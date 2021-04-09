# Google-Grass-Machine
Google生草机（重复翻译同一句子） 
代码贡献者：[Jerry1962325](https://github.com/Jerry1962325)    
此脚本使用了[googletrans](https://pypi.python.org/pypi/googletrans)包以调用Google翻译API。  
## 用法
安装googletrans：  
```
pip install googletrans==4.0.0-rc1
```
**\*由于googletrans默认版本3.0.0存在翻译时异常抛出`AttributeError: 'NoneType' object has no attribute 'group'`错误的漏洞，故需安装4.0.0-rc1来临时修复。**
安装完毕后，使用Python3运行： 
```
python googlegrassmachine.py
```
