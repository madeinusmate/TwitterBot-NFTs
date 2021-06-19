#!/usr/bin/env python
# tweepy-bots/bots/replytweets.py


import tweepy
import logging
from config import create_api
import time
import pandas as pd
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

NFT_df = pd.read_csv("bancavaticana_nft_database.csv")
hashtags = "#nft #nfts #nftart #nftcollectors #vatican #pope #vaticanart "
def daily_tweets(api):
    daily_counter = 0
    while daily_counter < 1:
        logger.info("Retrieving the Tweet")
        randomizer = random.randrange(0,51)
        # try:
        api.update_status(
            status="Introducing " + NFT_df["nft_name"][randomizer] + "! Explore the " + NFT_df["collection"][randomizer] + " #nftcollection! " + hashtags + NFT_df["url"][randomizer],
            auto_populate_reply_metadata=True)
        logger.info("Tweet Sent!")
        daily_counter += 1
        # except:
        #     logger.info("Trying Again...")

    while daily_counter == 1:
        logger.info("Waiting  8hrs for next Tweet")
        time.sleep(28800)
        logger.info("Wait is over!")
        daily_counter = 0



def main():
    api = create_api()
    daily_tweets(api)

if __name__ == "__main__":
    main()




