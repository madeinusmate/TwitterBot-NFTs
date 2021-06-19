#!/usr/bin/env python
# tweepy-bots/bots/replytweets.py

import tweepy
import logging
from config import create_api
import time
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

replies = ["The SVUMMI PONTEFICES #NFTs Collection!  #nftart  #NFTCommunity #Vatican #PopeFrancis https://opensea.io/collection/svmmi-pontefices", "The #Vatican first NFT Collection! SVUMMI PONTEFICES! #NFTs #nftart  #NFTCommunity https://opensea.io/collection/svmmi-pontefices", "The first HOLY NFT! https://opensea.io/collection/svmmi-pontefices", "Blessed NFTs! https://opensea.io/collection/svmmi-pontefices",
           "1 of 1 FRANCISCVS #nftart  #NFTCommunity #Vatican #PopeFrancis https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/59593089253092528413765826124767127098219086533139661812954986797934061813761", "IOANNES PAVLVS II#nftart  #NFTCommunity #Vatican #PopeJohnPaulII  https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/59593089253092528413765826124767127098219086533139661812954986795735038558209"]



class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        reply_counter = 0
        for reply_counter in range(0,10):
            logger.info("Processing tweet id:" + str(tweet.id))
            if tweet.user.id == self.me.id:
                logger.info("This tweet is a reply or I'm its author so, ignore it")
                return

            logger.info("Answering to " + str(tweet.user.name))

            tweet.user.follow()
            logger.info("Now following " + str(tweet.user.name))
            try:
                self.api.update_status(
                    status=random.choice(replies),
                    in_reply_to_status_id=tweet.id,
                    auto_populate_reply_metadata=True
                )

                logger.info("Replied to tweet id " + str(tweet.id) + " by " + str(tweet.user.name))
                logger.info("Waiting...")
                time.sleep(120)
            except:
                pass

            reply_counter += 1

        while reply_counter == 1:
            logger.info("Waiting 20 mins to avoid ban")
            logger.info("Total Tweets sent in this session: " + str(reply_counter))
            time.sleep(1200)
            logger.info("Starting a new Session")
            reply_counter = 0



    def on_error(self, status):
        logger.error(status)



def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["en"])


if __name__ == "__main__":
    main(["#NFT", "#NFTart", "#NFTs", "#opensea", "@mintable", "@opensea", "#nftcommunity", "#nftcollection", "#cryptoart", "@rarible", "#RARI"])