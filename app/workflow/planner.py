from app.analyzer.models import PageAnalysis

from app.workflow.actions import Action
from app.workflow.models import Workflow, WorkflowStep

#Doesn't execute just plans
def plan_workflow(
    analysis: PageAnalysis,
    user_request: str,
) -> Workflow:

    workflow = Workflow(url=analysis.url)

    workflow.steps.append(
        WorkflowStep(
            action=Action.CLICK,
            target="Search"       #TEMPORARY TO TEST THE PIPELINE WORKS
        )
    )

    return workflow