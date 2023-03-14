# Простая программа для управления личными финансами
#### (учебный проект для курса по практике программирования на Python)

[Техническое задание](specification.md)

Структура файлов и каталогов (модулей и пакетов) отражает архитектуру:

📁 bookkeeper - исполняемый код 

- 📁 models - модели данных

    - 📄 budget.py - бюджет
    - 📄 category.py - категория расходов
    - 📄 expense.py - расходная операция
- 📁 repository - репозиторий для хранения данных

    - 📄 abstract_repository.py - описание интерфейса
    - 📄 memory_repository.py - репозиторий для хранения в оперативной памяти
    - 📄 sqlite_repository.py - репозиторий для хранения в sqlite

- 📁 view - графический интерфейс
    - 📄 add_expense_widget.py - виджет добавления расхода
    - 📄 budget_widget.py - виджет бюджета
    - 📄 category_widget.py - виджет категорий
    - 📄 expenses_list_widget.py - виджет со списком расходов
    - 📄 main_window.py - главное окно приложения


- 📄 bookkeeper_presenter.py - презентер приложения, объединяет работу с данными и графический интерфейс
- 📄 run_bookkeeper - файл, содержит функцию запускающую приложение
- 📄 run_simple_client - «мини-презентер» для запуска простой консольной программы
- 📄 simple_client.py - консольная утилита, работающая в оперативной памяти
- 📄 sql_simple_client.py - консольная утилита, работающая с SQLite 
- 📄 utils.py - вспомогательные функции

📁 tests - тесты (структура каталога дублирует структуру bookkeeper)

```
poetry install
```

Команды для запуска тестов:
```
poetry run pytest --cov
poetry run mypy --strict bookkeeper
poetry run pylint bookkeeper
poetry run flake8 bookkeeper
```
