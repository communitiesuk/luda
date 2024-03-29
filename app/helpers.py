import json
from typing import Any

from starlette.responses import Response


class PrettyJSONResponse(Response):
    """JSON response with pretty formatting."""

    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        """Render the content as JSON."""
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")
