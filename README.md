## Гайд по бесплатному развертыванию Telegram-бота с GPT на GitHub Actions (для пользователей GitHub)

Этот гайд поможет вам развернуть копию Telegram-бота с GPT, используя код из репозитория https://github.com/sorry0not1kot2/telebotGPT, на платформе GitHub и использовать его бесплатно. 

**Что вам понадобится:**

* Аккаунт на GitHub.
* Базовое понимание работы с Git.
* Установленный Telegram и аккаунт в нем.

**Важно:** Бот написан на Python и использует библиотеку `g4f` для доступа к API ChatGPT через сторонних поставщиков. Этот метод бесплатный, но может перестать работать в любой момент. 

**Шаг 1: Создание копии репозитория (Fork)**

1. Откройте репозиторий https://github.com/sorry0not1kot2/telebotGPT на GitHub.
2. Нажмите кнопку "Fork" в правом верхнем углу страницы.
3. Подтвердите создание форка в вашем аккаунте.

**Шаг 2: Создание бота и команд в BotFather**

1. Откройте Telegram и найдите бота @BotFather.
2. Создайте нового бота, следуя инструкциям BotFather.
3. **Создайте две команды для бота:**
   - Выберите вашего бота из списка ботов в BotFather.
   - Выберите опцию `Edit Bot` -> `Edit Commands` -> `Edit Custom Commands`.
   - Вставьте следующий текст и отправьте:
     ```
     start - Старт бота
     clear - Очистка истории бота
     ```
4. Сохраните токен, который вам выдал BotFather при создании бота. **Это очень важно!**

**Шаг 3: Создание секрета репозитория GitHub для хранения токена**

1. Перейдите в настройки вашего форка репозитория на GitHub.
2. Выберите "Settings" -> "Secrets" -> "Actions" -> "New repository secret".
3. В поле "Name" введите `TELEGRAM_BOT_TOKEN`.
4. В поле "Value" вставьте ваш токен, полученный от BotFather.
5. Нажмите "Add secret".

**Шаг 4: Настройка GitHub Actions**

1. В вашем репозитории на GitHub нажмите "Actions".
2. Выберите "set up a workflow yourself".
3. Скопировать из моего репозитория python-app.yml 
по адресу:
https://github.com/sorry0not1kot2/telebotGPT/tree/main/.github/workflows
Или самостоятельно отредактируйте свой, заменив весь текст в файле на следующий код:

```yaml
name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        
    - name: Run main.py
      env:
        TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
      run: |
        python main.py

```
 скачайте requirements.txt из https://github.com/sorry0not1kot2/telebotGPT
 и сохраните его у себя в репозитории рядом с файлом main.py

4. Нажмите "Start commit", добавьте сообщение к коммиту (например, "Настройка GitHub Actions") и подтвердите.

**Шаг 5: Запуск бота**

GitHub Actions автоматически запустит workflow после предыдущего шага.

* Вы можете следить за процессом сборки и запуска на вкладке "Actions" вашего репозитория.
* После успешного завершения workflow ваш бот будет запущен и готов к работе!

**Важно:**

* Если в коде бота нужно внести изменения, сделайте это в своем репозитории (форке) и сделайте `git push`, чтобы изменения вступили в силу.
* GitHub Actions автоматически перезапустит бота после каждого пуша в ветку `main`.
* **На GitHub Actions workflow может работать не более 6 часов подряд. После этого вам нужно будет перезапустить его вручную. Для этого перейдите на вкладку "Actions" вашего репозитория, выберите последний workflow и нажмите кнопку "Re-run jobs".**
* Помните, что бесплатный доступ к API ChatGPT через библиотеку `g4f` может быть закрыт в любое время. 
* Используйте команды `/start` и `/clear` в чате с вашим ботом для его запуска и очистки истории соответственно. 

**Готово!** Теперь у вас есть собственная копия Telegram-бота с GPT, работающая на GitHub Actions. 

**Дополнительно:**

При желании вы можете запустить бота на любом другом сервере, поддерживающем запуск приложений из `.yml` или `.yaml` файлов. Вам нужно будет разобраться с документацией выбранного сервиса и адаптировать файл workflow под его требования. 
