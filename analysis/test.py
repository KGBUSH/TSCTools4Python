#encoding: utf-8


import jieba
import jieba.analyse
import chardet
import re


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
            return True
    else:
            return False



if __name__ == '__main__':
    a = u' \u54c8\u54c8\u54c8\u54c8{}{【】。。  \u597d\u53ef\u7231\u7684\u96e8 \u54c8\u54c8\u54c8\u54c8 \u4f60\u8fd9\u5df2\u7ecf\u5728\u602a\u4e86\u561b\u2026\u2026 \u8fd9\u4ef6\u8863\u670d \u5367\u69fd \u54c8\u54c8\u54c8\u554a\u597d \u53f8\u673a:\u5b8c\u4e86\u6211\u4e0d\u4f1a\u5f00\u8f66 \u54c8\u54c8\u54c8\u54c8'
    print a


    pattern= ['！', '￥', '……', '（', '）', '—', '【', '】', '{', '}', '、', '；', '：', '‘', '’', '“',
                  '”', '，', '。', '《', '》', '「', '」', '『', '』', '？','~']
    pattern2 = [",",".","!","?","/","\\",":",";","...","=","-","←","#","@","$","%","`","*","&","(",")","\"","+",
                "，","。","！","？","/","：","；","。。。","……","（","）","“","”","‘","’"]
    pattern.extend(pattern2)


    sorce_encoding = chardet.detect('h')['encoding']
    print 'type汉字:',sorce_encoding
    print '是否为汉字：',is_chinese('權'.decode('utf-8'))
    # jieba.set_dictionary('dict.txt.big')

    thewords = '话说不是应该做一种假的世界地图，2333把片场伪造成整个世界么。。。直接展示真实的世界地图难道没问题？QWQ!!!!真相啊，这妹子动真感情了'

    thewords = '话说不是应该'
    print thewords
    # thewords = ''.join([x for x in thewords if is_chinese(x.decode('utf-8'))])
    # print 'thewords:', thewords



    s="一根稻草，压不死骆[]【】驼；压死骆驼的是最后一根！"
    s = ''.join([x for x in a if x.encode('utf-8') not in pattern])
    print 'out: ',s, 'len(a):', len(a)
















    seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
    # jieba.add_word('QAQ')
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式

    seg_list = jieba.cut("我来到北京清华大学还遇见了金凯瑞和凯文加内特在打篮球", cut_all=False)
    seg_list = jieba.cut('233333333333', cut_all=False)
    for data in seg_list:
        # if len(data) > 1:
        print data,type(data)
    print("Default Mode: " + "/ ".join(seg_list))  # 精确模式













    content = "23333333也要像楚门那样勇敢追求自由与平等"
    seg_list = jieba.cut("今天,QAQfqrouter作者在Twitter正式宣布fqrouter停止使用,之后的日子,我们可能将慢慢面对那无法逾越的高墙,不过让我们努力肉身fq,即使无法肉身fq,也要像楚门那样勇敢追求自由与平等")  # 默认是精确模式
    print(", ".join(seg_list))
    print type((", ".join(seg_list)))
    tags = jieba.analyse.extract_tags(content, 10)
    print "tags: "
    for tag in tags:
        print tag,
    print '\n'

    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
    print(", ".join(seg_list))