
# -*- coding: utf-8 -*-


class Danmaku(object):

    def __init__(self, param_string, content):
        self._content = content
        paramList = param_string.split(",")

        # 视频中出现的秒数
        self._video_second = float(paramList[0])

        # 弹幕的模式 1..3 滚动弹幕 4底端弹幕 5顶端弹幕 6.逆向弹幕 7精准定位 8高级弹幕
        self._mode = paramList[1]

        # 字号,12非常小,16特小,18小,25中,36大,45很大,64特别大
        self._font_size = paramList[2]

        # 字体的颜色,HTML颜色的十进制
        self._color = paramList[3]

        # Unix格式的时间戳
        self._timestamp = paramList[4]

        # 弹幕池 0普通池 1字幕池 2特殊池
        self._pool_type = paramList[5]

        # 发送者ID
        self._sender_id = paramList[6]

        # 弹幕在弹幕数据库中rowID
        self._id = paramList[7]

    @property
    def id(self):
        return self._id

    @property
    def video_second(self):
        return self._video_second

    @property
    def mode(self):
        return self._mode

    @property
    def font_size(self):
        return self._font_size

    @property
    def color(self):
        return self._color

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def pool_type(self):
        return self._pool_type

    @property
    def sender_id(self):
        return self._sender_id

    @property
    def content(self):
        return self._content

