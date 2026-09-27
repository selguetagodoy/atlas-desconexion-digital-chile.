#!/usr/bin/env python3
"""Comprueba que las URLs oficiales del registro de fuentes sigan accesibles."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "source_registry.json"
USER_AGENT = "Mozilla/5.0 (compatible; AtlasSourceCheck/1.0; +https://selguetagodoy.github.io/)"
TIMEOUT = 20


def request_status(url: str) -> tuple[int | None, str, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT}, method="HEAD")
    try:
        with urlopen(request, timeout=TIMEOUT) as response:
            return response.status, "OK", "responde"
    except HTTPError as exc:
        if exc.code == 405:
            fallback = Request(
                url,
                headers={"User-Agent": USER_AGENT, "Range": "bytes=0-0"},
                method="GET",
            )
            try:
                with urlopen(fallback, timeout=TIMEOUT) as response:
                    return response.status, "OK", "responde por GET"
            except HTTPError as fallback_exc:
                exc = fallback_exc
            except URLError as fallback_exc:
                return None, "DEAD", str(fallback_exc.reason)

        if exc.code in {401, 403, 404, 410, 429}:
            return exc.code, "WARN", "HTTP 4xx; revisar manualmente o posible bloqueo"
        if exc.code >= 500:
            return exc.code, "DEAD", "HTTP 5xx"
        return exc.code, "WARN", f"HTTP {exc.code}"
    except URLError as exc:
        return None, "DEAD", str(exc.reason)
    except Exception as exc:  # noqa: BLE001
        return None, "DEAD", str(exc)


def main() -> int:
    payload = json.loads(REGISTRY.read_text(encoding="utf-8"))
    sources = payload.get("sources", [])
    if not sources:
        print("ERROR: source_registry.json no contiene fuentes.")
        return 2

    dead = 0
    warnings = 0
    print(f"# Source URL Liveness — {len(sources)} fuentes\n")

    for source in sources:
        source_id = source.get("id", "sin_id")
        institution = source.get("institution", "sin institución")
        url = source.get("official_url")
        if not url:
            print(f"- DEAD {source_id}: falta official_url")
            dead += 1
            continue

        status, label, detail = request_status(url)
        status_text = str(status) if status is not None else "network"
        print(f"- {label} [{status_text}] {institution} — {url} ({detail})")

        if label == "DEAD":
            dead += 1
        elif label == "WARN":
            warnings += 1

    print(f"\nResumen: {len(sources) - dead - warnings} OK · {warnings} WARN · {dead} DEAD")
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
