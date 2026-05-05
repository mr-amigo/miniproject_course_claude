import subprocess
from datetime import datetime
from pathlib import Path

PROMPT = (
    "проаналізуй код у папці todo/ і дай 3 пропозиції що можна покращити, "
    "plain text без markdown"
)
OUTPUT_FILE = Path(__file__).parent / "analyze_result.md"


def main() -> None:
    result = subprocess.run(
        ["claude", "-p", PROMPT],
        capture_output=True,
        text=True,
        check=True,
        cwd=Path(__file__).parent,
    )
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    OUTPUT_FILE.write_text(
        f"# Analysis Result\n\n_Generated: {timestamp}_\n\n{result.stdout}"
    )
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()
