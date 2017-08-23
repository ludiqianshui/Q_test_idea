'''
Created on 11 Aug 2017
@author: qsong
'''
# coding:utf-8
import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup
import chardet
import sys
import requests
from bs4 import UnicodeDammit

class data_extract(object):
    '''
    This module provides data_extract
    '''
    recommendation_url = "http://www.pk2018.net/game_show.asp"

    def __init__(self):
        '''
        Constructor
        '''
        return

    def __del__(self):
        return

    def get_recommendation(self):
        web_data = requests.get(self.recommendation_url)
        web_data.coding = 'utf-8'
        soup = BeautifulSoup(web_data.content, 'lxml')
        tip_table = soup.findAll('tr', {'class': "menu"})
        for elm in tip_table:
            tip_table_td = elm.findAll ('td')
            if len(tip_table_td) < 10:
                continue
            tip_season = UnicodeDammit (tip_table_td[0].text,  ["gb2312"]).unicode_markup
            game_type = UnicodeDammit (tip_table_td[1].text,  ["gb2312"]).unicode_markup
            game_time = UnicodeDammit (tip_table_td[2].text,  ["gb2312"]).unicode_markup
            game_home = UnicodeDammit (tip_table_td[3].text,  ["gb2312"]).unicode_markup
            game_odd = UnicodeDammit (tip_table_td[4].text,  ["gb2312"]).unicode_markup
            game_guest = UnicodeDammit (tip_table_td[5].text,  ["gb2312"]).unicode_markup
            tip_info = UnicodeDammit (tip_table_td[6].text,  ["gb2312"]).unicode_markup.split('/')[0]
            tip_value = UnicodeDammit (tip_table_td[6].text,  ["gb2312"]).unicode_markup.split('/')[1]
            game_score = UnicodeDammit (tip_table_td[7].text,  ["gb2312"]).unicode_markup
            tip_result = UnicodeDammit (tip_table_td[8].text,  ["gb2312"]).unicode_markup
            tip_time = UnicodeDammit (tip_table_td[9].text,  ["gb2312"]).unicode_markup
            tip_user_name = UnicodeDammit (tip_table_td[10].text,  ["gb2312"]).unicode_markup
            tip_user_if_soup = tip_table_td[10].findAll('a' , href=True)
            tip_user_id = tip_user_if_soup[0].attrs['href'].split("=")[1]
            
            print(tip_user_name)

        return


class Test(unittest.TestCase):
    def setUp(self):
        self.test_obj = data_extract()

    def tearDown(self):
        self.test_obj = None
        return

    def test_get_tip_info(self):
        self.test_obj.get_recommendation()
        # self.test_obj.get_goldenbet()
        return
