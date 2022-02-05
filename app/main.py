import os
import logging

import asyncio

from tweet_forwarder import TweetForwarder
from clients.telegram import TelegramClient


async def main():
    '''
    TweetForward, an application that forwards incoming tweets to clients.
    '''

    # Required parameters
    try:
        API_KEY = os.environ['API_KEY']
        API_SECRET = os.environ['API_SECRET']
        ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
        ACCESS_SECRET = os.environ['ACCESS_SECRET']
    except KeyError as error:
        logging.error("Required key not found: %s", error)

    # Optional parameters
    FOLLOW = os.environ.get('FOLLOW', '').split(',')
    TRACK = os.environ.get('TRACK', '').split(',')
    RETWEETS = os.environ.get('RETWEETS', False)
    CLIENTS = os.environ.get('CLIENTS')

    logging.info('Creating clients...')
    clients = []
    if CLIENTS:
        for client in CLIENTS.split(','):
            if client == 'telegram':
                try:
                    TELEGRAM_ID = os.environ['TELEGRAM_ID']
                    TELEGRAM_HASH = os.environ['TELEGRAM_HASH']
                    TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
                    TELEGRAM_CHANNEL = os.environ['TELEGRAM_CHANNEL']
                    clients.append(
                        TelegramClient(
                            api_id=TELEGRAM_ID,
                            api_hash=TELEGRAM_HASH,
                            bot_token=TELEGRAM_TOKEN,
                            channel=TELEGRAM_CHANNEL
                        ))
                except KeyError as client_error:
                    logging.error('Required key not found: %s', client_error)
            else:
                logging.warning('Client not supported : %s', client)
    logging.info('Done.')

    if len(clients) > 0:
        stream = TweetForwarder(
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_SECRET,
            clients=clients,
            retweets=RETWEETS)
        try:
            logging.info('Starting stream...')
            await stream.filter(
                follow=FOLLOW,
                track=TRACK,
                stall_warnings=True
            )
        except KeyboardInterrupt:
            logging.info('Stopped.')
        finally:
            logging.info('Done.')
            stream.disconnect()
    else:
        logging.warning("No supported clients specified... Stopped.")


if __name__ == '__main__':
    logging.basicConfig(
        format='%(levelname)s: %(message)s', level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Stopped.')
