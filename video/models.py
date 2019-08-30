# -*- coding: utf-8 -*-
"""Class: VideoData"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
import datetime

BASE = declarative_base()


class VideoData(BASE):
    """Attributes of created table."""
    __tablename__ = 'bilibili_video_crawler'

    id = Column(Integer, primary_key=True)
    av_id = Column(Integer, default=None, comment='av号')
    tid = Column(Integer, default=None, comment='分区id')
    typename = Column(Text, default=None, comment='分区名称')
    arctype = Column(Text, default=None, comment='稿件类型')
    play = Column(Integer, default=None, comment='播放量')
    review = Column(Integer, default=None, comment='评论数')
    video_review = Column(Integer, default=None, comment='弹幕量')
    favorites = Column(Integer, default=None, comment='收藏数')
    title = Column(Text, default=None, comment='视频标题')
    description = Column(Text, default=None, comment='视频简介')
    author = Column(Text, default=None, comment='up主名称')
    mid = Column(Integer, default=None, comment='up主id')
    created_at = Column(DateTime, default=None, comment='投稿时间')
    coins = Column(Integer, default=None, comment='投币数')
    last_update = Column(DateTime, default=datetime.datetime.now)
