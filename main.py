import uvicorn
from fastapi import FastAPI

from api import router


def main() -> None:
    app = FastAPI()
    app.include_router(router)
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
