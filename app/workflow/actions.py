#This file defines every browser action the platform supports
#and every subsytem uses the same vocab now

#Enumerate feature
#to define random strings like "click" "type" through an official list
from enum import Enum

class Action(str, Enum):       #str so that JSON responses look like word "click" not like Action.CLICK
    NAVIGATE = "navigate"

    CLICK = "click"

    TYPE = "type"

    SELECT = "select"

    CHECK = "check"

    UNCHECK = "uncheck"

    WAIT = "wait"

    SCROLL = "scroll"

    EXTRACT = "extract"

    UPLOAD = "upload"

    DOWNLOAD = "download"