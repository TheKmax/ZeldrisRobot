class Config(object):
    LOGGER = True

    # REQUIRED
    TOKEN = "2037324684:AAEqb4l6DnNydfKhhXLu82Y5PR9AyeT-11A"  # Take from @BotFather
    OWNER_ID = 1234567890  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "Kmax_01"
    API_HASH = "kmax"  # for purge stuffs
    API_ID = 123456
    WORKERS = ( 8 )
    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "sqldbtype://username:pw@hostname:port/db_name"  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    #REDIS_URL = "redis://something@nothing/anything:10002"  # needed for afk module, get from redislab
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    DEV_USERS = (
        []
    )  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = (
        []
    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = (
        []
    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = "5000"
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = "CAACAgIAAxkBAAIaDmEGNm7RWLf4T8lmO_F-e_ZRERIlAAJQBwACRvusBIwUzzDf7E-yIAQ"  # banhammer marie sticker
    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = False  # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = "kmax"  # OpenWeather API
    SPAMWATCH_API = "kmax"  # Your SpamWatch token
    WALL_API = "kmax"
    SPAMMERS = []

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
