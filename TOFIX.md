# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/sql_injection/docker-compose.yml:3` - the `mysql` service uses `image: mysql_reconfigured`, which is not built anywhere in the repo (no Dockerfile or build script references it), so `docker-compose-up.sh` fails with "pull access denied". Add the Dockerfile/build step that produces it, or use the official `mysql` image (with the commented `command:` on line 6 if the auth plugin change is what "reconfigured" meant).
- `src/sql_injection/app/app.py:183-185` - the `safe=1` (parameterized) path calls `cursor.execute(query, values)` without `multi=True`, which returns `None`, then iterates it (`for _ in iterator`) and raises `TypeError` - so the "fixed" half of the demo always crashes. Drop the loop on that branch.
- `src/suid/Dockerfile:13` - `COPY --chmod=600:600` is not a valid mode (`--chmod` takes a single octal/symbolic mode), so the image build fails. Use `--chmod=600`.

## Medium

- `src/suid/Dockerfile:12,16` - `adduser mark` / `adduser hacker` are interactive (password and GECOS prompts) and do not work unattended in `docker build`. Use `adduser --disabled-password --gecos "" mark` (same for `hacker`).
- `src/shell_injection/README.md:5` - describes "an app that allows users to search for files in an archive", but the directory contains only the README; the demo code is missing. Add it (`src/sql_injection/app/app.py:197` `do_something` already has a `shell=True` injection that could be moved/linked here) or remove the directory.
- `src/xss/app.py:63` - `/add` always runs `html.escape(value)`, so posting `hack.txt` never triggers the XSS the demo is named for; only the mitigated version exists. Add a `safe` toggle like `sql_injection/app/app.py:173` so both the vulnerable and fixed behaviour can be shown.
- `src/sql_injection/connect.sh:4` - connects as `root` with no password, but `docker-compose.yml:14` sets `MYSQL_ROOT_PASSWORD`, so the login is refused. Pass the password from the `env_db_password` that `.auto.enter.sh` exports (e.g. `MYSQL_PWD="${env_db_password}" mysql ...`).
- `src/sql_injection/app/app.py:25` - prints the DB password to stdout (container logs) at startup; this is not part of the SQL-injection lesson. Remove the `print(f"{password=}")`.

## Low

- `src/sql_injection/app/app.py:115` - `tag("buttom")` emits a non-existent `<buttom>` element; should be `button` (or just the `<a>`).
- `src/xss/app.py:4,60` - docstrings say "Web server that can add two numbers" / "add two numbers" (copy-paste); describe the chat instead. Same docstring-less `add()` naming for the download route in `src/unrestricted_file_download/app.py:31`.
- `src/sql_injection/app/run.py:1` - shebang is `#!/usr/bin/env python` while every other script uses `python3`; the `python:3-alpine` image has both, but be consistent (`src/xss/app.py:1` too).
- `pyproject.toml:107` - `mypy_path = "src:python:scripts"` lists `python` and `scripts`, which do not exist in this repo; set it to `"src"`.
- `README.md:5-25` - static README shows a "black" code-style badge (the repo uses ruff) and five PyPI badges for a package that is not published (`pyproject.toml:103` `package = false`), and lists none of the demos under `src/`. Replace the badges with a short index of the demo directories.
