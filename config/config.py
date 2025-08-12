from dataclasses import dataclass
from environs import Env


@dataclass
class TGbot:
    token: str

@dataclass
class LogSettings:
    level: str
    format: str

@dataclass
class GenaiAPI:
    token: str


@dataclass
class Config:
    bot: TGbot
    log: LogSettings
    gemini: GenaiAPI


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        bot=TGbot(token=env('BOT_TOKEN')),
        gemini=GenaiAPI(token=env('GEMINI_API_KEY')),
        log=LogSettings(level=env("LOG_LEVEL"),format=env("LOG_FORMAT")),
    )


