import uvicorn

from n_pl.server import app


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8484)  # todo: put to settings
