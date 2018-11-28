#-----------------------------------
# Libraries and References
#-----------------------------------
import os
import json

#-----------------------------------
# [Required]	Script Information
#-----------------------------------
ScriptName = "BirthdayList"
Website = "https://www.twitch.tv/maveleye"
Creator = "Maveleye"
Version = 0.1
Description = "Query current month from a source to display all birthdays on stream."

#-----------------------------------
# Set Variables
#-----------------------------------
SettingsFile = os.path.join(os.path.dirname(__file__), "settings.json")

#-----------------------------------
# [Required] Intialize Data
#-----------------------------------
def Init():
    global ScriptSettings
    ScriptSettings = Settings(settingsFile)
