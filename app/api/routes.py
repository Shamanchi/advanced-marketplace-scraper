from fastapi import APIRouter

router = APIRouter()

@router.get('/health')
async def health():
    return {'status': 'ok'}

@router.post('/scrape')
async def scrape(data: dict):
    return {'status': 'queued', 'urls': data.get('urls', [])}