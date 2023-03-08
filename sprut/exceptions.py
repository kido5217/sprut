"""Package-specific exceptions."""


class DocumentExists(Exception):
    """Document already exists."""

    def __init__(self, id):
        self.id = id

        self.message = f"Document with id {self.id} already exists."
        super().__init__(self.message)
