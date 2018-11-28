#-----------------------------------
#   Import Libraries
#-----------------------------------
import os
import json
import codecs

#-----------------------------------
#   [Required] Script Information
#-----------------------------------
ScriptName = 'BirthdayList'
Website = 'https://www.twitch.tv/maveleye'
Creator = 'Maveleye'
Version = '0.1'
Description = 'Query current month from a source to display all birthdays on stream.'

#-----------------------------------
#   Set Variables
#-----------------------------------
SettingsFile = os.path.join(os.path.dirname(__file__), 'settings.json')

#-----------------------------------
#   Save/Load
#-----------------------------------

class Settings():
    """ Loads settings from file if file is found. If not uses default values. """
    def __init__(self, settingsFile = None):
        try:
            with codecs.open(settingsFile, encoding='utf-8-sig', mode='r') as f: self.__dict__ = json.load(f, encoding='utf-8')
        except:
            return
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
#   [Required] Intialize Data (Only called on load)
#-----------------------------------
def Init():
    global ScriptSettings
    ScriptSettings = Settings(settingsFile)
    return

#---------------------------------------
#	[Required] Execute Data / Process Messages
#---------------------------------------
def Execute():
    #   Check if the proper command is used, the command is not on cooldown, and the user has permission to use the command
    if data.IsChatMessage() and data.GetParam(0).lower() == ScriptSettings.Command and not Parent.IsOnCooldown(
            ScriptName, ScriptSettings.Command) and Parent.HasPermission(data.User, ScriptSettings.Permission,
                                                                         ScriptSettings.Info):
        Parent.SendStreamMessage(ScriptSettings.Response)  # Send your message to chat
        Parent.AddCooldown(ScriptName, ScriptSettings.Command, ScriptSettings.Cooldown)  # Put the command on cooldown
    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return


# ---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters)
# ---------------------------
def Parse(parseString, userid, username, targetid, targetname, message):
    if "$myparameter" in parseString:
        return parseString.replace("$myparameter", "I am a cat!")

    return parseString