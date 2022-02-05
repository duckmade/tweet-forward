import logging

from tweepy.asynchronous import AsyncStream

from clients.base import BaseClient


class TweetForwarder(AsyncStream):
    '''
    Forward tweets in realtime via given clients.

    Attributes:
        clients (list[BaseClient]): A list of BaseClient class objects.
        retweets (bool): Should I send data on incoming retweets?
    '''

    def __init__(self, clients: list[BaseClient], retweets: bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clients = clients
        self.retweets = retweets

    async def __send_message(self, tweet: str):
        for client in self.clients:
            logging.info("Sending message to %s...", client)
            await client.send_message(message=tweet)

    async def on_status(self, status):
        if hasattr(status, "retweeted_status"):
            if self.retweets:
                logging.info("Received retweet...")
                try:
                    await self.__send_message(status.retweeted_status.extended_tweet["full_text"])
                except AttributeError:
                    await self.__send_message(status.retweeted_status.text)
        else:
            logging.info("Received tweet...")
            try:
                await self.__send_message(status.extended_tweet["full_text"])
            except AttributeError:
                await self.__send_message(status.text)

    async def on_request_error(self, status_code):
        if status_code in [420]:
            logging.warning('Rate limiting (%s)... ', status_code)
            return False
        logging.error('Request error (%s)...', status_code)
        self.disconnect()

    async def on_connection_error(self):
        self.disconnect()
        logging.error('Connection error... Disconnected.')


if __name__ == '__main__':
    print(TweetForwarder.__doc__)
