class IssueNotFoundError(Exception):
    def __init__(self, issue_id: str):
        self.issue_id = issue_id
