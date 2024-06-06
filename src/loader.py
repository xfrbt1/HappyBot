from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


from src.dbrepo.dict_store import DictStore
from src.config.settings import get_settings


settings = get_settings()
db = DictStore(settings.data_path + settings.users_db)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
