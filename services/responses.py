from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class ApiResponse(BaseModel):
    success: bool = True
    message: str = "Success"
    data: Optional[Any] = None
    errors: Optional[List[str]] = None


def success_response(data: Any = None, message: str = "Success") -> Dict:
    return {"success": True, "message": message, "data": data}


def error_response(message: str, errors: List[str] = None) -> Dict:
    return {"success": False, "message": message, "errors": errors or []}


def paginated_response(items: List, total: int, page: int, per_page: int) -> Dict:
    return {
        "success": True,
        "data": {
            "items": items,
            "total": total,
            "page": page,
            "per_page": per_page,
            "total_pages": (total + per_page - 1) // per_page,
        },
    }
