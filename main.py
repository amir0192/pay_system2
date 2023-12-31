from fastapi import FastAPI


app = FastAPI(docs_url='/')

# импорт всех компонентов
from api.convert import convert_api
from api.profile import profile_api
from api.transfer import transfers_api

