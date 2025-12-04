This repository is a small, educational collection of standalone Python example scripts (in Portuguese) organized under the `python/` folder by module (e.g. `modulo 1`, `modulo 2`, ...).

**Purpose**: Provide succinct, actionable guidance so an AI coding assistant can make safe, idiomatic, and minimal edits to teaching examples without breaking runnable scripts.

**Quick Overview**
- **Layout**: Examples live in `python/<module number>/` and are individual scripts (not a package). Example: `python/modulo 1/primeiro programa.py`.
- **File style**: Files often use Portuguese text and comments, and filenames commonly contain spaces (e.g. `lista2.py` and `lista 2.py` patterns). Preserve existing naming patterns when editing.
- **Intent**: Each file is a self-contained demo (printing, simple calculations, assignments). Changes should keep the example runnable and focused on the concept in the filename.

**Editor / Runtime Notes**
- **Run examples**: Use the system Python interpreter. On Windows PowerShell wrap paths with spaces in quotes, for example:
  - `python "python/modulo 1/primeiro programa.py"`
- **Python version**: No explicit version or dependencies; assume modern Python 3 (3.8+ recommended). There is no build system or tests.
- **Encoding**: Files contain Portuguese text; treat files as UTF-8.

**Conventions observed (follow these)**
- **Variable naming**: Examples show `snake_case` for variables, UPPERCASE for constants, and occasional demonstration of alternatives in comments (camelCase). Follow existing style in the touched file.
- **Comments and language**: Keep Portuguese comments and messages; they are part of the teaching material.
- **Minimal edits**: Prefer minimal, focused edits: update the example to clarify a single teaching point rather than refactoring multiple files.

**When changing or adding examples**
- Keep the example runnable as a one-file script. If adding a new example, place it under the appropriate `python/modulo X/` directory and follow the naming/language patterns.
- Avoid renaming existing files. If a rename is necessary, update any project documentation referencing that file and explain the rationale in the commit message.

**What NOT to do**
- Do not convert this collection into a package/module layout or add a test harness unless instructed; the repository is deliberately a set of standalone learning scripts.
- Do not remove Portuguese text or replace it with English unless asked.

**Examples the assistant can safely perform**
- Fix a small bug in a single demo (e.g., correct arithmetic or formatting in `python/modulo 2/operadores aritmeticos.py`).
- Improve explanatory print statements or comments inside a file to make the intent clearer.
- Add a new example file that demonstrates a single basic concept and follows existing patterns.

**Commit / PR guidance**
- Keep changes small and focused (one file or one concept per PR).
- Use descriptive commit messages in Portuguese or English explaining the learning goal (e.g., `fix: correct division example in operadores aritmeticos.py`).

If anything here is surprising or you'd like different assistant behavior (for example, migrating examples into a package, adding tests, or standardizing filenames), tell me and I will adapt these instructions.
