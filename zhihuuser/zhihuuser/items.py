# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import item,Field


class UserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    name = Field()
    avatar_url = Field()
    headline = Field()
    type = Field()
    url_token = Field()
    gender = Field()
    follower_count = Field()
    url = Field()
    avatar_url_template = Field()
    articles_count = Field()
    answer_count = Field()


