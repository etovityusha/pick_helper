import enum


class ParsingStatusEnum(enum.Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    UPDATE_REQUIRED = "UPDATE_REQUIRED"
