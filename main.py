from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Application Automator')

class ApplyRequest(BaseModel):
    job_url: str

@app.post('/apply')
async def apply(req: ApplyRequest):
    # TODO: Playwright automation with safety
    return {'status': 'submitted', 'note': 'Human review recommended for CAPTCHA'}