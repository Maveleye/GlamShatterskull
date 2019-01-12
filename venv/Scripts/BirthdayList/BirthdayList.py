#-----------------------------------
#   Import Libraries
#-----------------------------------
import os
import json
import codecs
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references


import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

#   Import your Settings class Comeback to this
from Settings_Module import MySettings

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
global SettingsFile
SettingsFile = os.path.join(os.path.dirname(__file__), 'settings.json')
global ScriptSettings
ScriptSettings = Settings(settingsFile)

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
    #   Create Settings Directory
    directory = os.path.join(os.path.dirname(__file__), "Settings")
    if not os.path.exists(directory):
        os.makedirs(directory)

    #   Load settings
    SettingsFile = os.path.join(os.path.dirname(__file__), "Settings\settings.json")
    ScriptSettings = MySettings(SettingsFile)
    ScriptSettings.Response = "Overwritten pong! ^_^"
    return

#-----------------------------------
#	[Required] Execute Data / Process Messages
#-----------------------------------
def Execute():
    #   Check if the proper command is used, the command is not on cooldown, and the user has permission to use the command
    if data.IsChatMessage() and data.GetParam(0).lower() == ScriptSettings.Command and not Parent.IsOnCooldown(
            ScriptName, ScriptSettings.Command) and Parent.HasPermission(data.User, ScriptSettings.Permission,
                                                                         ScriptSettings.Info):
        Parent.SendStreamMessage(ScriptSettings.Response)  # Send your message to chat
        Parent.AddCooldown(ScriptName, ScriptSettings.Command, ScriptSettings.Cooldown)  # Put the command on cooldown
    return

#-----------------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#-----------------------------------
def Tick():
    return


#-----------------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters)
#-----------------------------------
def Parse(parseString, userid, username, targetid, targetname, message):
    if "$myparameter" in parseString:
        return parseString.replace("$myparameter", "I am a cat!")

    return parseString

#-----------------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#-----------------------------------
def ReloadSettings(jsonData):
    # Execute json reloading here
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SettingsFile)
    return

#-----------------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
#-----------------------------------
def Unload():
    return

#-----------------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
#-----------------------------------
def ScriptToggled(state):
    return
