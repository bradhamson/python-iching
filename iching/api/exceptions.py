class APIError(Exception):
    pass

class EnvironmentValueError(APIError):
    
    def __init__(self, env: str) -> None:
        message = f'Environment value: "{env}" is not supported.'
        super().__init__(message=message)