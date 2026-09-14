class ProcessMessageUseCase:

    def execute(self, message: str) -> str:
        return f"SmartBuyer recibió: {message}"