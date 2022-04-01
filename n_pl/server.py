from fastapi import FastAPI


def get_app() -> FastAPI:
    application = FastAPI(title='Notifier Platform', debug=True, version='0.0.1')

    return application


app = get_app()
