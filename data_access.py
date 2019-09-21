# -*- coding: utf-8 -*-
"""
NOAA ERDAP Data Access and Visualizations

This file defines class(es) used to access and visualize NOAA CoastWatch data.
* ERDDAP Tutorial
https://coastwatch.pfeg.noaa.gov/projects/erddap/
* ALL ERDDAPS - Search
http://erddap.com/
"""
import requests as req

class DataAccess(object):
    """
    Define a class of data access methods and properties.
    """
    base_url = "https://coastwatch.pfeg.noaa.gov/erddap/"

    def __init__(self, **kwargs):
        """
        Now I'm just getting lazy.  This is an attempt to facilitate loading
        all necessary resource parameters.
        :param kwargs:
        """
        for k, v in kwargs:
            setattr(self, k, v)


    def gen_url(self):
        """
        All ERDDAP requests define all data request parameters
        :return: string: a URL identifying the resource we want
        """
        pass

    def fetch(self, url):
        """
        Fetch data from defined url
        :param url: a data resource identifier
        :return: resource returned from ERDDAP server
        """
        pass

    def return_data(self, file_format: str):
        """
        THIS ISN"T NEEDED, SET DURING URL CALL
        Reformat stored ata and return to caller
        :param file_format: a string defining file format to be returned
        :return:
        """
        pass
