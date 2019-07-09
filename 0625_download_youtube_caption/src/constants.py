import json
from collections import OrderedDict
import glob
from datetime import datetime
import pafy
from pydub import AudioSegment
import os


PROJECT_PATH = "/Users/alan/alan_project/english_listening_test/0625_download_youtube_caption/"
AUDIO_PATH = PROJECT_PATH + 'audio/'
SEGMENT_PATH = PROJECT_PATH + 'segment/'
DATABASE_PATH = PROJECT_PATH + 'database/'
URL_NEW_PATH = PROJECT_PATH + 'new_url.txt'
YOUTUBE_PREFIX = "https://www.youtube.com/watch?v="

INVALID_CHARS = '<>:\"\/|?*'
