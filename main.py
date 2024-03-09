
from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel



app = FastAPI()

class Memo(BaseModel):
    id: str
    content: str

memos = []

@app.post('/memos')
def create_memo(memo:Memo):
    memos.append(memo)
    return '메모추가 성공'

@app.get('/memos')
def read_memo():
    return memos

@app.put("/memos/{memo_id}")
def put_memo(req_memo:Memo):
    for memo in memos:
        if memo.id == req_memo.id:
            memo.content = req_memo.content
            return '성공했습니다.'
    return '실패'

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id):
    for index, memo in enumerate(memos):
        if memo.id == memo_id:
            memos.pop(index)
            return '성공했습니다.'
    return '실패'

app.mount("/", StaticFiles(directory="static",html=True), name="static")