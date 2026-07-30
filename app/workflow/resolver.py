#To connect analyzer and workflow
#Basically when given a workflow step, which page element does it refer to 
#For ex: finds which button to click from 3 buttons on the page, etc.

from app.analyzer.models import PageAnalysis
from app.workflow.models import WorkflowStep


def resolve_element(
    analysis: PageAnalysis,       #Everything the analyzer discovered: buttons, forms, inputs, etc.
    step: WorkflowStep,
):
    """
    Finds the webpage element that matches a workflow step.
    """

    return None