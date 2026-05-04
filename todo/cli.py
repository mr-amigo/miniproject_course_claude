import argparse

from .models import Task
from .storage import load, next_id, save


def cmd_add(args: argparse.Namespace) -> None:
    tasks = load()
    task = Task(id=next_id(tasks), title=args.title)
    tasks.append(task)
    save(tasks)
    print(f"added #{task.id}: {task.title}")


def cmd_list(args: argparse.Namespace) -> None:
    tasks = load()
    visible = tasks if args.all else [t for t in tasks if not t.done]
    if not visible:
        print("no tasks")
        return
    for t in visible:
        mark = "x" if t.done else " "
        print(f"[{mark}] {t.id}: {t.title}")


def cmd_done(args: argparse.Namespace) -> None:
    tasks = load()
    for t in tasks:
        if t.id == args.id:
            t.done = True
            save(tasks)
            print(f"done #{t.id}")
            return
    print(f"no task #{args.id}")


def cmd_rm(args: argparse.Namespace) -> None:
    tasks = load()
    remaining = [t for t in tasks if t.id != args.id]
    if len(remaining) == len(tasks):
        print(f"no task #{args.id}")
        return
    save(remaining)
    print(f"removed #{args.id}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="tiny todo CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    add = sub.add_parser("add", help="add a task")
    add.add_argument("title")
    add.set_defaults(func=cmd_add)

    lst = sub.add_parser("list", help="list tasks (open by default)")
    lst.add_argument("--all", action="store_true", help="include done tasks")
    lst.set_defaults(func=cmd_list)

    done = sub.add_parser("done", help="mark task as done")
    done.add_argument("id", type=int)
    done.set_defaults(func=cmd_done)

    rm = sub.add_parser("rm", help="remove task")
    rm.add_argument("id", type=int)
    rm.set_defaults(func=cmd_rm)

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)
