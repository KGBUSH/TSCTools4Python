# coding:utf-8


import jieba



class JiebaUtil(object):
    """
    利用结巴分词做分词处理
    """

    @staticmethod
    def PrecisionMode(thewords):
        """
        jieba精确模式分词
        :param thewords: 需要分词的句子
        :return: list,存储分好的词
        """

        wordslist = []

        seg_list = jieba.cut(thewords, cut_all=False)
        for data in seg_list:
            if len(data) > 1:  # 只保留长度在2以上的词
                wordslist.append(data)

        return wordslist
