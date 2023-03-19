import os
#from urllib.parse import urlparse
#import urllib
#print(os.getenv("API_BOT_161"))
#print(os.environ.get("API_BOT_161"))

api_reg = os.getenv("API_BOT_161")#.split(":")
api_bot_reg = api_reg.split(":")
bot_login = api_bot_reg[0]
api_key = api_bot_reg[1]
#print(f"login {bot_login}, api {api_key}")
