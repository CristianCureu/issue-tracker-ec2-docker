from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class IssueStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"


class IssuePriority(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"


class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=300)
    priority: IssuePriority = IssuePriority.medium


class IssueUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    priority: Optional[IssuePriority] = None
    status: Optional[IssueStatus] = None


class IssueOut(BaseModel):
    id: str
    title: str
    description: str
    priority: IssuePriority
    status: IssueStatus
