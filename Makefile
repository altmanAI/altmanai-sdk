install:
	pnpm install
	python -m pip install -e packages/python/altmanai[dev]

build:
	pnpm --filter @altmanai/core build
	python -m build packages/python/altmanai

test:
	pnpm --filter @altmanai/core test
	pytest packages/python/altmanai/tests

lint:
	pnpm --filter @altmanai/core lint
	python -m ruff check packages/python/altmanai/src packages/python/altmanai/tests

format:
	pnpm --filter @altmanai/core format
	python -m ruff format packages/python/altmanai/src packages/python/altmanai/tests
