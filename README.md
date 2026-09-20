# Advanced Marketplace Scraper

**Архитектура промышленного парсера. 100K+ товаров/сутки: CDP, Playwright, прокси-пулы, Redis, Celery**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![Playwright](https://img.shields.io/badge/Playwright-1.45-green?logo=playwright)](https://playwright.dev)
[![License](https://img.shields.io/badge/License-Shamanchi-green)](LICENSE)

---

## Описание

Промышленный парсер маркетплейсов с:
- CDP (Chrome DevTools Protocol) для обхода защиты
- Playwright для рендеринга JS
- Прокси-пулы с ротацией
- Redis для очередей и кэша
- Celery для распределенной обработки
- PostgreSQL для хранения

---

## Быстрый старт
`ash
git clone https://github.com/Shamanchi/advanced-marketplace-scraper
cd advanced-marketplace-scraper
cp .env.example .env
docker-compose up -d
`

### Переменные окружения
| Переменная | Описание |
|------------|----------|
| SCRAPER_CONCURRENCY | Параллельные воркеры |
| SCRAPER_DELAY_MIN/MAX | Задержки между запросами |
| PROXY_LIST | Файл с прокси |
| HEADLESS | Режим браузера |
| CDP_ENDPOINT | Chrome DevTools endpoint |

---

## Тесты
`ash
pytest -v
`

---

## Docker
`ash
docker build -t advanced-marketplace-scraper .
docker-compose up -d
`

---

## Структура
`
├── app/
│   ├── api/routes.py
│   ├── core/config.py
│   ├── core/logging.py
│   ├── services/scraper.py
│   └── main.py
├── tests/test_api.py
├── .github/workflows/ci.yml
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
`

---

## CI/CD
GitHub Actions: Ruff, MyPy, Pytest, Docker build

---

## Лицензия
Лицензия Shamanchi 1.0 (source-available) — см. [LICENSE](LICENSE).
---

> Источник темы: Каталог портфолио, запись advanced-marketplace-scraper