from dataclasses import dataclass

@dataclass
class BaseConfig:
    DEBUG: bool

@dataclass
class DevConfig(BaseConfig):
    DEBUG: bool = True

@dataclass
class ProdConfig(BaseConfig):
    DEBUG: bool = False

configs = {'prod': ProdConfig, 'dev': DevConfig}