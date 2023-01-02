import telebot
import json
import codecs

class BallsBot():

    __bot : telebot.TeleBot = None
    __locale : (str | None) = None
    __msg_dict : (dict | None) = None

    @classmethod
    def __get_key(cls) -> str:
        """
        Get bot API key\n
        Key must be inside of a 'key.txt' file on the first line
        """
        f = open('key.txt')
        key = f.readline()
        f.close()
        return key
    
    @classmethod
    def set_locale(cls, locale : str):
        """
        Set the bot locale.\n
        All locales are defines as .json files in ./locale folder.\n
        After creating the bot instance, all messages will be displayed using selected locale.\n
        If given locale is not found, defaults to en-US.
        """
        cls.__locale = locale
    
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
            if (cls.__locale == None):
                print('Please, set the locale first')
                return
            else:
                loc = None
                try:
                    loc = open("./locales/" + cls.__locale + ".json",encoding='utf_8_sig')
                except FileNotFoundError:
                    loc = open("./locales/en-US.json",encoding='utf_8_sig')
            cls.__msg_dict = json.load(loc)
            key = cls.__get_key()
            cls.__bot = telebot.TeleBot(key)
            cls.__create_handlers()
        else:
            print('Bot instance exists, use start() or stop()')

    @classmethod
    def __create_handlers(cls) -> None:
        @cls.__bot.message_handler(commands=['start'])
        def __start(message):
            """
            Start using the bot\n
            Users should use this to register (for ball scratching)
            """
            BallsBot.__bot.reply_to(message, BallsBot.__msg_dict["hello"])

        @cls.__bot.message_handler(commands=['help'])
        def __help(message):
            """
            Show all bot commands
            """
            BallsBot.__bot.reply_to(message, BallsBot.__msg_dict["help"])

        @cls.__bot.message_handler(commands=['scratch'])
        def __scratch_balls(message):
            """
            This is the glorious method used to\n
            SCRATCH BALLS.
            """
            BallsBot.__bot.reply_to(message, BallsBot.__msg_dict["not_implemented"])
        
        @cls.__bot.message_handler(commands=['scratch_info'])
        def __scratch_balls(message):
            """
            Get scratching statistics
            """
            BallsBot.__bot.reply_to(message, BallsBot.__msg_dict["not_implemented"])