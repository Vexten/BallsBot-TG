import abc

class MediaGetter(metaclass=abc.ABCMeta):
    """
    Base class for different url media getters.\n
    Implements local `file_id` caching to avoid multiple file uploads.\n
    Files are cached based on url and extention, meaning, if original file conforms to `send_audio` and `send_video` formats, there will exist only one cached `file_id` for sending
    it as a document and as it's respective format. If original file extention differs from `MP3` or `MPEG4`, another cached `file_id` will exist for the original file.
    """

    def __init__(self, db):
        """
        Super constructor.\n
        All child classes should call `super().__init__(db)` to hook to a local cached `file_id` db.
        """
        self.__db = db

    def get_audio(self, url : str, conform : bool) -> str:
        """
        Gets audio from url.\n
        :param url: url to get audio from
        :param conform: whether or not to convert audio to `MP3` for usage with `send_audio`
        :return: `str` containig either a file_id (if the file was already uploaded before) or multipart/form-data containing requested audio.
        """
        link = self.__audio_url_filter(url)

    def get_video(self, url : str, conform : bool) -> str:
        """
        Gets video from url.\n
        :param url: url to get video from
        :param conform: whether or not to convert video to `MPEG4` for usage with `send_video`
        :return: `str` containig either a file_id (if the file was already uploaded before) or multipart/form-data containing requested video.
        """
        link = self.__video_url_filter(url)
    
    def add_video(self, url : str, file_id : str) -> bool:
        """
        Adds pair `url` and `file_id` to local cache.\n
        For usage with audio links.
        """
        link = self.__audio_url_filter(url)
        self.__add_file(link, file_id)

    def add_audio(self, url : str, file_id : str) -> bool:
        """
        Adds pair `url` and `file_id` to local cache.\n
        For usage with video links.
        """
        link = self.__video_url_filter(url)
        self.__add_file(link, file_id)

    def __add_file(self, url : str, file_id : str) -> None:
        """
        Adds `url` to `file_id` pairing to local cache.
        """
        raise NotImplementedError('No DB interface yet')

    @staticmethod
    @abc.abstractmethod
    def __audio_url_filter(url : str) -> str:
        """
        Method called to prepare the url (if needed) before the class tries to get audio from url.\n
        Should be defined by child class, leave empty if not needed.
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def __video_url_filter(url : str) -> str:
        """
        Method called to prepare the url (if needed) before the class tries to get video from url.\n
        Should be defined by child class, leave empty if not needed.
        """
        pass
