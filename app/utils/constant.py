from enum import Enum, EnumMeta

MODEL_PATH = "app/models/model.sav"


class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True


class BaseEnum(Enum, metaclass=MetaEnum):
    pass


class Emotion(str, BaseEnum):
    sadness = "sadness"
    anger = "anger"
    love = "love"
    fear = "fear"
    happy = "happy"


class Sentiment(str, BaseEnum):
    positive = "positive"
    neutral = "neutral"
    negative = "negative"
