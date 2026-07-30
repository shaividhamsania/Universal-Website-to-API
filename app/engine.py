#Gets webpage info
from app.analyzer.analyzer import analyze_page
#Turns user request into workflow
from app.workflow.planner import plan_workflow
#Matches each workflow step to an element found during page analysis
from app.workflow.resolver import resolve_element
#Carries out the workflow
from app.workflow.executor import execute_workflow


#Pulls everything together to coordinate
def run_engine(url: str, user_request: str):

    # Step 1
    analysis = analyze_page(url)

    # Step 2
    workflow = plan_workflow(
        analysis,
        user_request
    )

    # Step 3
    for step in workflow.steps:
        resolve_element(
            analysis,
            step
        )

    # Step 4
    result = execute_workflow(workflow)

    return result