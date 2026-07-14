# Vernean Voyages Wiki — 本地配置

WIKI_LANG=en
WIKI_NAME=Vernean Voyages Wiki
PORT=1828
TIMEZONE=Europe/Paris

# Python 解释器（RFC-munger-0002）
PYTHON_ENV=system
PYTHON_BIN=python3
PIP_CMD=pip3

# 发布与引擎
DEPLOY_TARGET=cloudflare
CDN_BASE=https://baojie.github.io/memex/dist

# 主题
PRIMARY_COLOR=a02128

# 路径
MEMEX_ROOT=/Users/mac/memex
PROJECT_ROOT=/Users/mac/memex/wiki-jules-verne-36

# 语料
CORPUS_SOURCE=The Collected Works of Jules Verne (36 Novels and Short Stories) — Jules Verne
CORPUS_LICENSE=public-domain
CORPUS_PATH=corpus/raw/doc_final.md

# Butler 实例命名（Phase 10-F，主题取自 Verne 作品人物）
BUTLER_INSTANCE_DISCOVER=Nemo
BUTLER_INSTANCE_CREATE=Harding
BUTLER_INSTANCE_ENRICH=Aronnax
BUTLER_INSTANCE_PUBLISH=Ardan
BUTLER_INSTANCE_HOUSEKEEPING=Fogg
