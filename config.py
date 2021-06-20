# --------------------------------------------- #
# Plugin Name           : TelegramAirdropBot    #
# Author Name           : fabston               #
# File Name             : config.py             #
# --------------------------------------------- #

# Enable / disable the airdrop
airdrop_live = True

# Telegram
token = '<YOUR BOT TOKEN>'  # More: https://core.telegram.org/bots#3-how-do-i-create-a-bot
log_channel = 0  # Channel ID. Example: -1001355597767
admins = []  # Telegram User ID's. Admins are able to execute command "/airdroplist"
airdrop_cap = 100  # Max airdrop submissions that are being accepted
wallet_changes = 3  # How often a user is allowed to change their wallet address

# MySQL Database
mysql_host = 'localhost'
mysql_db = 'TelegramAirdropBot'
mysql_user = 'AirdropUser'
mysql_pw = '<YOUR PASSWORD>'

texts = {
    'start_1': 'Hi {} and welcome to our Airdrop!\n\nGet started by clicking the button below.\n\nTo apply for the airdrop you have to be in our [Telegram](https://t.me/Telegram) group, Folow us on [Twitter](https://twitter.com) and [Retweet](https://twitter.com) our pinned post.',
    'start_2': 'Hi {},\n\nYour address has been added to the airdrop list!\n\nIf you have accidentally mistyped your wallet address or twitter username when registering. No worries!\nClick >💼 *View Wallet Address*< and update your address or twitter username.\n\n',
    'airdrop_start': 'The airdrop didn\'t start yet.',
    'airdrop_address': 'Type in your address:',
    'airdrop_max_cap': 'ℹ️ The airdrop reached its max cap.',
    'airdrop_walletused': '⚠️ That address has already been used. Use a different one.',
    'airdrop_confirmation': '✅ Your address has been added to airdrop list.',
    'airdrop_wallet_update': '✅ Your address has been updated.',
    'twitter_address': '💬️ Type in your twitter username:',
    'twitter_addressused': '⚠️ This twitter username has already been used.',
    'twitter_update': '✅ Your twitter username has been changed.',    
    'twitter_confirmation': '✅ Your twitter username has been added to airdrop list.\n\nYou have successfully applied for Airdrop Event\n\nIf you have accidentally mistyped your wallet address or twitter username when registering. No worries!\nClick >💼 *View Wallet Address*< and update your address or twitter username.',
}
