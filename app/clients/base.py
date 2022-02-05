import asyncio
import logging


class BaseClient:
    '''
    This is a base class for creating clients.
    '''

    def __init__(self):
        '''
        The constructor for BaseClient class.
        '''
        self.client = None

    def __str__(self):
        '''
        String represenation for the BaseClient class.
        '''
        return self.__class__.__name__

    async def send_message(self, message: str):
        '''
        The function sends a message.

        Parameters:
            message (str): The message to send.
        '''
        await asyncio.sleep(2.0)
        logging.info('Message: %s', message)


if __name__ == '__main__':
    print(BaseClient.__doc__)
