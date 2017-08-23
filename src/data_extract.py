'''
Created on 11 Aug 2017
@author: qsongsss
'''
import unittest
import urllib2
from bs4 import BeautifulSoup

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
        page = urllib2.urlopen(self.recommendation_url)
        soup = BeautifulSoup(page, "html.parser")
        game_table = soup.findAll('tr', {'class': "menu"})
        for elm in game_table:
            game_table_td = elm.findAll ('td')
            game_in_episode = game_table_td[00].text.encode("latin1").decode("gb2312").encode('ascii','ignore')
            print  type(game_in_episode)
            game_type = game_table_td[01].text.encode("latin1").decode("gb2312").encode('ascii','ignore')
            print  type(game_type)
        return

class Test(unittest.TestCase):
    def setUp(self):
        self.test_obj = data_extract()

    def tearDown(self):
        self.test_obj = None
        return

    def test_get_game_info(self):
        self.test_obj.get_recommendation()
        # self.test_obj.get_goldenbet()
        return
