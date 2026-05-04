# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal notes repository for a Claude Code course mini-project. There is **no source code, no build system, no tests, and no dependencies**. Do not suggest installing tooling, running tests, or scaffolding a project unless the user explicitly asks for it.

## Layout

Notes follow the course curriculum:

```
modules/
  01-what-is-claude-code/
  02-getting-hands-on/
  03-hooks-and-sdk/
  04-quiz/
```

Each module contains numbered lesson directories (e.g. `01-ai-coding-assistant/`, `08-mcp-servers/`). The lesson numbering is **continuous across modules** (module 02 starts at `03-setup`, module 03 starts at `10-hooks-intro`) — preserve that scheme when adding lessons.

Most lessons that have been worked through contain a single file: `my_conclusions.txt`. Empty lesson directories are placeholders for lessons not yet completed.

## Conventions for notes

- Notes are written in **Ukrainian**. When the user asks you to add or edit notes, write in Ukrainian and match the existing register: lowercase prose, comma-separated thoughts, minimal punctuation, no headings or bullet lists.
- File name is always `my_conclusions.txt` inside the relevant lesson directory.
- One file per lesson; do not split notes across multiple files.
