import glob
import os
from pdfminer.pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfminer.layout import LAParams
from pdfminer.pdfminer.converter import TextConverter
from pdfminer.pdfminer.pdfpage import PDFPage
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
#author---Cary.Chen

#提取pdf文字
def extract_pdf_content(pdf):
    rsrcmgr = PDFResourceManager()
    outfp = StringIO() #输出方式
    laparams = LAParams()
    device = TextConverter(rsrcmgr=rsrcmgr, outfp=outfp, laparams=laparams)
    with open(pdf, 'rb') as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        pagenos=set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=0, password="",caching=True, check_extractable=True):
            interpreter.process_page(page)
    mystr = outfp.getvalue()
    device.close()
    outfp.close()
    return mystr

#将字典和文章字数制成统计图
def dict_to_gragh(mydict):
   df = pd.DataFrame.from_dict(mydict, orient='index').reset_index() #将字典转换为数据框
   df.columns = ["path", "content"] #key-value变为path-content
   df["length"] = df.content.apply(lambda x: len(x)) #统计内容长度并length加入数据框架
   #%matplotlib inline #（在IDE中运行需要注释掉
   plt.figure(figsize=(14, 6)) #图片的长宽比例
   df.set_index('path').length.plot(kind='bar') #和坐标是path 纵坐标是length的柱状图
   plt.xticks(rotation=45,fontproperties='SimHei') #pdf文件名称以倾斜45
   plt.legend(prop={'family': 'SimHei', 'size': 15})
   plt.show()

#创建文件夹
def mkdir(resultpath):
    isExists = os.path.exists(resultpath)# 判断路径是否存在
    if not isExists:
        os.makedirs(resultpath)
        print
        resultpath + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print
        resultpath + ' 目录已存在'
        return False

#将dict转化为文件保存
def savetxt(mydict,resultpath):
    mkdir(resultpath)
    for pdf in mydict:
        filename = pdf.split('.')[-2]+'.docx'
        f = open(resultpath+'/'+filename,'w')
        f.write(mydict[pdf])
        f.close()


pdf_path = "pdf/" #pdf 文件所在路径为其中的pdf文件夹
pdf_dict = {} #以文章题目为key,文章内容为value的字典
resultpath = "Result"
pdfs = glob.glob("{}/*.pdf".format(pdf_path)) #获得所有 pdf 文件的路径
for pdf in pdfs:
    key = pdf.split('/')[-1] #提取文件名
    if not key in pdf_dict:
        print("Extracting content from {} ...".format(pdf))
        pdf_dict[key] = extract_pdf_content(pdf) #将文件名与文件内容以key-value形式存储起来
savetxt(pdf_dict,resultpath)






