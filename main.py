from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.routes.issues import router
from app.errors import IssueNotFoundError

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_request: Request, _exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": "Invalid request bodya"}
    )


@app.exception_handler(IssueNotFoundError)
async def issue_not_found_handler(_request: Request, _exc: IssueNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": "Issue not found"}
    )

app.include_router(router)
