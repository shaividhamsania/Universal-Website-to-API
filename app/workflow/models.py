#Workflow basically defines what website to open, what to enter, select, click, extract etc.

from dataclasses import dataclass, field
from app.workflow.actions import Action

@dataclass
class WorkflowStep:      #Each step is 1 browser action
    action: Action       #For ex: "type"            #Also no accidental strings, only valid actions defined in Action
    target: str       #For ex: "Destination"
    value: str = ""       #For ex: "New York"


@dataclass
class Workflow:
    url: str

    #List of workflowsteps
    #Cause one workflow consists of many browser actions
    #Basically what the executor will run
    steps: list[WorkflowStep] = field(default_factory=list)