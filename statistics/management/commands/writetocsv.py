#!-*- coding:utf-8 -*-
__author__ = 'valeriy'

from statistics.models import Data
from postgres_copy import CopyMapping
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Class that creates a command to manage.py
    Use: in terminal type
    python3 manage.py writetocsv
    """
    def handle(self, *args, **kwargs):
        """
        Copies data from eFw3Cefj.csv to DB in fields of model Data
        :param args:
        :param kwargs:
        :return:
        """
        c = CopyMapping(Data, 'eFw3Cefj.csv', dict(region='Регион', country='Страна', value='Значение'))
        c.save()
        self.stdout.write("CSV is readed")