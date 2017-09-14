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
    tip_dict = {}
    
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
            self.tip_dict['tip_season'] = UnicodeDammit (tip_table_td[0].text,  ["gb2312"]).unicode_markup   #第30期
            self.tip_dict['game_type'] = UnicodeDammit (tip_table_td[1].text,  ["gb2312"]).unicode_markup    #欧冠杯    
            self.tip_dict['game_time'] = UnicodeDammit (tip_table_td[2].text,  ["gb2312"]).unicode_markup    #09-14 02:45    
            self.tip_dict['game_home'] = UnicodeDammit (tip_table_td[3].text,  ["gb2312"]).unicode_markup    #皇家马德里
            self.tip_dict['game_odd'] = UnicodeDammit (tip_table_td[4].text,  ["gb2312"]).unicode_markup     #三球半
            self.tip_dict['game_guest'] = UnicodeDammit (tip_table_td[5].text,  ["gb2312"]).unicode_markup   #希腊人竞技
            self.tip_dict['tip_info'] = UnicodeDammit (tip_table_td[6].text,  ["gb2312"]).unicode_markup.split('/')[0]   #皇家马德里
            self.tip_dict['tip_value'] = UnicodeDammit (tip_table_td[6].text,  ["gb2312"]).unicode_markup.split('/')[1]  #0.85
            self.tip_dict['game_score'] = UnicodeDammit (tip_table_td[7].text,  ["gb2312"]).unicode_markup   #-
            self.tip_dict['tip_result'] = UnicodeDammit (tip_table_td[8].text,  ["gb2312"]).unicode_markup   #等待
            self.tip_dict['tip_time'] = UnicodeDammit (tip_table_td[9].text,  ["gb2312"]).unicode_markup     #09-13 20:24    
            self.tip_dict['tip_user_name'] = UnicodeDammit (tip_table_td[10].text,  ["gb2312"]).unicode_markup   #我要下天台
            tip_user_if_soup = tip_table_td[10].findAll('a' , href=True)
            self.tip_dict['tip_user_id'] = tip_user_if_soup[0].attrs['href'].split("=")[1]                   #16135
            
            print(self.tip_dict)

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
