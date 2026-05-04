from dataclasses import asdict, dataclass, field
from datetime import datetime

ALLOWED_PRIORITIES: tuple[str, ...] = ("low", "medium", "high")


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    priority: str = "medium"
    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    def __post_init__(self) -> None:
        if self.priority not in ALLOWED_PRIORITIES:
            raise ValueError(f"invalid priority: {self.priority}")

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(**data)
