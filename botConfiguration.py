import json
from configparser import ConfigParser


def users_phrases_config():
    fileOpenName = 'phrasesUser.json'
    with open(fileOpenName, encoding="utf-8") as fl:
        phrases = json.load(fl)
        return phrases


def bot_phrases_config():
    fileOpenName = 'phrasesBot.json'
    with open(fileOpenName, encoding="utf-8") as fl:
        phrases = json.load(fl)
        return phrases


def read_db_config(filename='config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    return db


def read_vk_config(filename='config.ini', section='vk'):
    parser = ConfigParser()
    parser.read(filename)
    tokes = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            tokes[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    return tokes
