import telebot
from helpers.LocaleGetter import LocaleGetter

class BallsBot():

    __bot : telebot.TeleBot = None
    __msg_dict : (dict | None) = None

    @staticmethod
    def _get_key() -> str:
        """
        Get bot API key\n
        Key must be inside of a 'key.txt' file on the first line
        """
        f = open('key.txt')
        key = f.readline()
        f.close()
        return key
    
    @classmethod
    def start(cls) -> None:
        """
        Start polling for messages.\n
        Bot instance should exist beforehand.
        """
        if (cls.__bot != None):
            cls.__bot.infinity_polling()

    @classmethod
    def stop(cls) -> None:
        """
        Stop polling for messages\n
        Bot instance should exist beforehand.
        """
        if (cls.__bot != None):
            cls.__bot.stop_polling()

    @classmethod
    def create(cls) -> None:
        """
        Create a new bot instance, if it doesn't exist
        """
        if (cls.__bot == None):
            locale_getter = LocaleGetter("./locales")
            cls.__msg_dict = locale_getter.get_message_strings()
            key = BallsBot._get_key()
            cls.__bot = telebot.TeleBot(key)
            cls.__create_handlers()
        else:
            print('Bot instance exists, use start() or stop()')

    @classmethod
    def __get_user_locale(cls, locale_code : str) -> str:
        """
        Filter locale codes for unsupported locales and default to 'en'
        """
        if locale_code in cls.__msg_dict.keys():
            return locale_code
        else:
            return 'en'

    @classmethod
    def __create_handlers(cls) -> None:
        @cls.__bot.message_handler(commands=['start'])
        def __start(message : telebot.types.Message):
            """
            Start using the bot\n
            Users should use this to register (for ball scratching)
            """
            loc = BallsBot.__get_user_locale(message.from_user.language_code)
            BallsBot.__bot.reply_to(message, BallsBot.__msg_dict[loc]["hello"].format(user=message.from_user.full_name))

        @cls.__bot.message_handler(commands=['help'])
        def __help(message : telebot.types.Message):
            """
            Show all bot commands
            """
            loc = BallsBot.__get_user_locale(message.from_user.language_code)
            BallsBot.__bot.reply_to(message, BallsBot.__msg_dict[loc]["help"])

        @cls.__bot.message_handler(commands=['scratch'])
        def __scratch_balls(message : telebot.types.Message):
            """
            This is the glorious method used to\n
            SCRATCH BALLS.
            """
            loc = BallsBot.__get_user_locale(message.from_user.language_code)
            BallsBot.__bot.reply_to(message, BallsBot.__msg_dict[loc]["not_implemented"])
        
        @cls.__bot.message_handler(commands=['scratch_info'])
        def __scratch_info(message : telebot.types.Message):
            """
            Get scratching statistics
            """
            loc = BallsBot.__get_user_locale(message.from_user.language_code)
            BallsBot.__bot.reply_to(message, BallsBot.__msg_dict[loc]["not_implemented"])
        
        @cls.__bot.message_handler(commands=['shop'])
        def __scratch_shop(message : telebot.types.Message):
            """
            Shop for items in BALLS shop
            """
            loc = BallsBot.__get_user_locale(message.from_user.language_code)
            BallsBot.__bot.reply_to(message, BallsBot.__msg_dict[loc]["not_implemented"])
        
        @cls.__bot.message_handler(commands=['get_audio'])
        def __get_audio(message : telebot.types.Message):
            """
            Get audio from provided url
            """
            loc = BallsBot.__get_user_locale(message.from_user.language_code)
            file = None
            BallsBot.__bot.send_audio(message.chat.id,file,reply_to_message_id=message.id)
