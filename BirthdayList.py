#-----------------------------------
# Libraries and References
#-----------------------------------
import os
import json
import codecs

#-----------------------------------
# [Required]	Script Information
#-----------------------------------
ScriptName = 'BirthdayList'
Website = 'https://www.twitch.tv/maveleye'
Creator = 'Maveleye'
Version = 0.1
Description = 'Query current month from a source to display all birthdays on stream.'

#-----------------------------------
# Set Variables
#-----------------------------------
SettingsFile = os.path.join(os.path.dirname(__file__), 'settings.json')

#-----------------------------------
# Save/Load
#-----------------------------------

class Settings():
    """ Loads settings from file if file is found. If not uses default values. """
    def __init__(self, settingsFile = None):
        try:
            with codecs.open(settingsFile, encoding='utf-8-sig', mode='r') as f: self.__dict__ = json.load(f, encoding='utf-8')
        except:

# TODO add except possibly command defaults

    def Reload(self, jsonData):
        self.__dict__ = json.loads(jsonData, encoding='utf-8-sig')
        return

    def Save(self, settingsFile):
        try:
            with codecs.open(settingsFile, encoding='utf-8-sig', mode='w+') as f:
                f.write('var settings = {0};'.format(json.dumps(self.__dict__, encoding='utf-8')))
        except:
            Parent.Log(ScriptName, 'Failed to save settings to file.')

#-----------------------------------
# [Required] Intialize Data
#-----------------------------------
def Init():
    global ScriptSettings
    ScriptSettings = Settings(settingsFile)
