from pyrogram import Client

from .base import BaseClient


class TelegramClient(BaseClient):
    '''
    This is a class creates a Telegram client and send messages to a given channel.

    Attributes:
        api_id (int | str): Telegram api id.
        api_hash (str): Telegram api hash.
        bot_token (str): Telegram bot token.
        channel (str): Telegram channel to send to.
    '''

    def __init__(self, api_id: int | str, api_hash: str, bot_token: str, channel: str):
        '''
        The constructor for TelegramClient class.

        Parameters:
            api_id (int | str): Telegram api id.
            api_hash (str): Telegram api hash.
            bot_token (str): Telegram bot token.
            channel (str): Telegram channel to send to.
        '''
        super().__init__()
        self.client = Client("my_bot", api_id=api_id,
                             api_hash=api_hash, bot_token=bot_token)
        self.channel = channel

    async def send_message(self, message: str):
        '''
        The function sends a message to a given Telegram channel.

        Parameters:
            message (str): The message to send.
        '''
        async with self.client:
            await self.client.send_message(self.channel, message)


if __name__ == '__main__':
    print(TelegramClient.__doc__)
