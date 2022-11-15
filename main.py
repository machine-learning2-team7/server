import os

import uvicorn

port = os.environ.get("PORT", 8000)
is_production = os.environ.get("PRODUCTION", False)

if __name__ == "__main__":
    uvicorn.run(
        "src.app:app",
        host="0.0.0.0",
        port=port,
        reload=not is_production,
    )
