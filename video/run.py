# -*- coding: utf-8 -*-
"""Main executor for crawler."""
from argparse import ArgumentParser
import time
import random
from crawler import Crawler
from models import VideoData
from tables import Storage
from config import CRAWLER_URL, START_ID, BATCH_SIZE

def parser_scheduler():
    """Command-line interfaces."""
    parser = ArgumentParser()
    parser.add_argument('--go', type=bool, nargs='?', default=False)
    return parser


if __name__ == '__main__':
    parser = parser_scheduler()
    args = parser.parse_args()

    if args.go == True:
        while(True):
            c = Crawler(
                url = CRAWLER_URL,
                start_id = START_ID,
                batch_size = BATCH_SIZE
            )
            batch_result = c.get_info()
            
            if len(batch_result) == 0:
                continue

            s = Storage(
                model = VideoData,
                df = batch_result
            )
            s.save_data()
            START_ID += BATCH_SIZE
            time.sleep(random.random()*5)
