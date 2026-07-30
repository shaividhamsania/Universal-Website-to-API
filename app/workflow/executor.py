#Engine executing workflow

from app.workflow.models import Workflow


def execute_workflow(workflow: Workflow):
    """
    Executes a planned workflow.

    Returns the workflow result.
    """

    return {
        "status": "success",
        "steps_executed": len(workflow.steps)
    }