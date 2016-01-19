# encoding: utf-8


from Entity.Danmaku import *
from Util.JiebaUtil import *

from collections import *


class ExtractUtil(object):
    """
    一个工具类
    """

    @staticmethod
    def SortDanmakuList(unsorted_danmakuList):
        """
        对还没有排序的整篇电影弹幕 按照弹幕出现的时间进行一次排序
        :param unsorted_danmakuList:  初始的list<Danmaku>
        :return:  list<Danmaku> (已经排好序)
        """
        return sorted(unsorted_danmakuList, key=lambda Danmaku: Danmaku.video_second)


    @staticmethod
    def ExtractUser(danmakuList):
        """
        提取UserID
        :param danmakuList: 整篇电影弹幕
        :return: List<String> userID
        """
        userID = []
        for danma in danmakuList:
            if danma.sender_id not in userID:
                userID.append(danma.sender_id)
        return userID


    @staticmethod
    def ExtractWords(userid, danmakulist):
        """
        在每个window的list<Danmaku>，汇总每个userid的words

        thinking：结巴分词加在这里

        :param userid:  某个userid
        :param danmakulist:  某window的list<Danmaku>
        :return: words（str）
        """
        userwords = ""
        # pattern="[！￥……（）——【】{}、；：‘’“”，。《》「」『』？]"
        pattern= ['！', '￥', '……', '（', '）', '—', '【', '】', '{', '}', '、', '；', '：', '‘', '’', '“',
                  '”', '，', '。', '《', '》', '「', '」', '『', '』', '？','~']
        pattern2 = [",",".","!","?","/","\\",":",";","...","=","-","←", '→', '•',"#","@","$","%","`","*","&","(",")","\"","+",
                    "，","。","！","？","/","：","；","。。。","……","（","）","“","”","‘","’"]
        pattern.extend(pattern2)

        for danma in danmakulist:
            if danma.sender_id == userid:
                if danma.content is None:
                    continue
                if len(userwords) > 0:
                    userwords += ' '
                userwords += danma.content

        extract_userwords = ''.join([x for x in userwords if x.encode('utf-8') not in pattern])  # 去掉特殊字符只留下字母数字汉字

        Set_userwords = Counter()
        Set_userwords.update(JiebaUtil.PrecisionMode(extract_userwords))  # 参数是list
        Dict_userwords = {}
        for word in Set_userwords:
            Dict_userwords.update({word: Set_userwords[word]})

        return Dict_userwords



    @staticmethod
    def Adjustwords():
        """
        词的调整
        :return:
        """
