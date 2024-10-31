from typing import List

import uvicorn
from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()

messages_db = []


class Message(BaseModel):
    id: int = None
    text: str


@app.get("/")
def get_all_messages() -> List[Message]:
    return messages_db


@app.get(path="/message/{message_id}")
def get_message(message_id: int) -> Message:
    try:
        return messages_db[message_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.post("/message")
def create_message(message: Message) -> str:
    message.id = len(messages_db)
    messages_db.append(message)
    return f"Message created!"


@app.put("/message/{message_id}")
def update_message(message_id: int, message: str = Body()) -> str:
    try:
        edit_message = messages_db[message_id]
        edit_message.text = message
        return f"Message updated!"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete("/message/{message_id}")
def delete_message(message_id: int) -> str:
    try:
        messages_db.pop(message_id)
        return f"Message ID={message_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")


@app.delete("/")
def kill_message_all() -> str:
    messages_db.clear()
    return "All messages deleted!"


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
