#!/usr/bin/python3
from trello import TrelloClient
import pyperclip
import os
import constants

client = TrelloClient(
    api_key=constants.TRELLO_API_KEY,
    api_secret=constants.TRELLO_API_SECRET,
)

all_boards = client.list_boards()

con_list= client.get_board(constants.TRELLO_LEARNING_BOARD_ID).get_lists(list_filter=None)

data=str(pyperclip.paste())

print(con_list[0].add_card(data))

os.system('notify-send "New Card Added" "'+data+'"')