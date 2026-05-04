import json
from pathlib import Path

from .models import Task

DEFAULT_PATH = Path("tasks.json")


def load(path: Path = DEFAULT_PATH) -> list[Task]:
    if not path.exists():
        return []
    with path.open() as f:
        return [Task.from_dict(d) for d in json.load(f)]


def save(tasks: list[Task], path: Path = DEFAULT_PATH) -> None:
    with path.open("w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2, ensure_ascii=False)


def next_id(tasks: list[Task]) -> int:
    return max((t.id for t in tasks), default=0) + 1
