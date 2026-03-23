from fastapi import APIRouter, status, HTTPException
from app.schemas import *
from app.storage import *
from app.errors import IssueNotFoundError
import uuid

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])


@router.get("/", response_model=list[IssueOut])
def get_issues():
    """Retrieve all issues."""
    issues = load_data()
    return issues


@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
def create_issue(payload: IssueCreate):
    """Create a new issue."""
    issues = load_data()
    new_issue = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.description,
        "priority": payload.priority,
        "status": IssueStatus.open
    }
    issues.append(new_issue)
    save_data(issues)
    return new_issue


@router.get("/issue/{issue_id}", response_model=IssueOut)
def get_issue(issue_id: str):
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            return issue
    raise IssueNotFoundError(issue_id=issue_id)


@router.put("/issue/{issue_id}", response_model=IssueOut)
def update_issue(issue_id: str, payload: IssueUpdate):
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            updated_issue = issue.copy()

            update_data = payload.model_dump(
                exclude_unset=True, exclude_none=True)
            updated_issue.update(update_data)

            issues[index] = updated_issue
            save_data(issues)
            return updated_issue
        raise IssueNotFoundError(issue_id=issue_id)


@router.delete("/issue/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id: str):
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            issues.pop(index)
            save_data(issues)
            return
        raise IssueNotFoundError(issue_id=issue_id)
