from typing import Any, Dict
import hashlib
import json


class SessionManager:
    def __init__(self):
        self._sessions = {}

    def create_session(self, user_id: int, data: Dict = None) -> str:
        session_id = hashlib.sha256(f"{user_id}".encode()).hexdigest()[:32]
        self._sessions[session_id] = {"user_id": user_id, "data": data or {}}
        return session_id

    def get_session(self, session_id: str) -> Dict:
        return self._sessions.get(session_id)

    def delete_session(self, session_id: str):
        if session_id in self._sessions:
            del self._sessions[session_id]

    def update_session(self, session_id: str, data: Dict):
        if session_id in self._sessions:
            self._sessions[session_id]["data"].update(data)


session_manager = SessionManager()
