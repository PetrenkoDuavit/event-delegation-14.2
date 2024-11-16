
class GroupLimitError(Exception):
    def __init__(self, message="Group size limit exceeded"):
        super().__init__(message)
