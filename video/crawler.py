# -*- coding: utf-8 -*-
"""Class: Crawler"""
import requests
import pandas as pd
import time
import random


class Crawler():
    """Call API to format info of each video."""
    def __init__(self, url, start_id, batch_size):
        self.url = url
        self.start_id = start_id
        self.batch_size = batch_size


    def get_info(self):
        """Download info from API and format the info."""
        df_batch = []
        for _id_ in range(self.batch_size):
            av_id = _id_ + self.start_id
            try:
                html = requests.get(self.url + str(av_id))
            except:
                print('HTML get error.')
                with open('unread_url.log', 'a+') as f:
                    f.write(html + '\n')
                continue
            time.sleep(random.random()/2)
            if html.status_code == 200:
                try:
                    df_json = html.json()
                except:
                    print('Unexpected error.')
                    continue
                try:
                    formatted_df = self.format_info(df_json=df_json, av_id=av_id)
                except:
                    print('Unexpected error.')
                    continue
            else:
                continue
            df_batch.append(formatted_df)
        try:
            df_batch = pd.concat(df_batch)
        except:
            print('No data is saved from this batch')
        with open('test_problem_about_list.log', 'a+') as f:
            f.write(df_batch + '\n')
        return df_batch


    @staticmethod
    def format_info(df_json, av_id):
        """Format json data."""
        formatted_df = pd.DataFrame({
            'av_id': [av_id],
            'tid': [df_json['data']['tid']],
            'typename': [df_json['data']['typename']],
            'arctype': [df_json['data']['arctype']],
            'play': [df_json['data']['play']],
            'review': [df_json['data']['review']],
            'video_review': [df_json['data']['video_review']],
            'favorites': [df_json['data']['favorites']],
            'title': [df_json['data']['title']],
            'description': [df_json['data']['description']],
            'author': [df_json['data']['author']],
            'mid': [df_json['data']['mid']],
            'created_at': [df_json['data']['created_at']],
            'coins': [df_json['data']['coins']]
            })
        return formatted_df
