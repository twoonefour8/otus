import json
from fastapi import FastAPI, Response

app = FastAPI()


@app.get('/ping')
def pong():
    return Response(
        status_code=200,
        content=json.dumps({'message': 'pong'})
    )
