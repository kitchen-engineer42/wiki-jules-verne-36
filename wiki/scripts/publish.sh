#!/usr/bin/env bash
# publish.sh — 发布脚本，委托 memex 统一管道
set -euo pipefail
MEMEX_ROOT="${MEMEX_ROOT:-$HOME/memex}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec "$MEMEX_ROOT/wiki/scripts/publish.sh" --wiki-root "$(cd "$SCRIPT_DIR/../.." && pwd)" "$@"
