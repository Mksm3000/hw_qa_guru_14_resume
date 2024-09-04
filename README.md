<p align="center" dir="auto">
  <a href="https://magento.softwaretestingboard.com/" rel="nofollow">
  <themed-picture data-catalyst-inline="true" data-catalyst=""><picture>
<img alt="LUMA" src="resources/images/logo.svg" width="300" height="100" 
style="visibility:visible;max-width:100%;">
    </picture></themed-picture>
  </a>
</p>


<h2 align="center"> Demo auto-tests LUMA store </h2>
<h3 align="center"> Используемые инструменты в проекте </h3>

<div class="image-container">
    <img src="resources/icons/python.svg" height="40">
    <img src="resources/icons/pycharm.svg" height="40">
    <img src="resources/icons/pytest.svg" height="40">
    <img src="resources/icons/selenium.svg" height="40">
    <img src="resources/icons/github.svg" height="40">
    <img src="resources/icons/allure-report.svg" height="40">
    <img src="resources/icons/jenkins.svg" height="40">
    <img src="resources/icons/selenoid.svg" height="40">
    <img src="resources/icons/allure_testops.svg" height="40">
    <img src="resources/icons/jira.svg" height="40">
    <img src="resources/icons/telegram.svg" height="40">
</div>


<details>
    <summary><h2><img src="resources/icons/flow-chart.gif" height="40"> Структура 
каталогов проекта</h2></summary>
      <ul>
        <li><code>pages:</code> Модули (классы страниц сайта и их методы)</li>
        <li><code>resources:</code> Ресурсы (иконки, скриншоты, gif)</li>
        <li><code>tests:</code> Тесты</li>
        <li><code>user:</code> Несколько типов юзеров для тестов</li>
        <li><code>utils:</code> Вспомогательные функции для работы с вложенями</li>
        <li><code>pytest.ini</code> Файл настроек и параметров тестирования</li>
        <li><code>requirements.txt</code> Файл с требованиями к проекту</li>
      </ul>
</details>

<details>
    <summary><h2><img src="resources/icons/ux.gif" height="40"> Список 
тестов</h2></summary>
      <ul>
        <li>1) Переход по ссылкам методом <code>click()</code></li>
        <li>2) Переход по ссылкам методом <code>hover()</code></li>
        <li>3) Создание аккаунта</li>
        <li>4) Ввод логина (успешный и неуспешный)</li>
        <li>5) Работа с корзиной (добавить товар, исправить, удалить)</li>
      </ul>
</details>

<h2> <img src="resources/icons/analytics.gif" height="40"> Запуск тестов и получение 
отчета</h2>
<h3>Локально <img src="resources/icons/home-office.gif" height="40"></h3>
<details>
    <summary> 1) Склонировать репозиторий</summary>
      <ul>
        <li><code>git clone https://github.com/Mksm3000/hw_qa_guru_14_resume.git</code></li>
      </ul>
</details>

<details>
    <summary> 2) Установить зависимости и запустить тесты</summary>
      <ul>
        <li><code>python -m venv .venv</code></li>
        <li><code>source .venv/bin/activate</code></li>
        <li><code>pip install -r requirements.txt</code></li>
        <li><code>pytest .</code></li>
      </ul>
</details>

<details>
    <summary> 3) Получить отчёт о прохождении тестов в allure</summary>
      <ul>
        <li><code>allure serve allure-results/</code></li>
      </ul>
</details>

<details>
    <summary> После выполнения команды откроется браузер с отчетом</summary>
      <img src="resources/images/allure-report screen.png">
</details>


<h3>Удалённо <img src="resources/icons/remote-access.gif" height="40"></h3>
<details>
    <summary> 1) Необходимо открыть проект на Jenkins <img src="resources/icons/jenkins.svg" height="40"></summary>
        <ol>
            <a href="https://jenkins.autotests.cloud/job/C13-ShamelessMax-14_Resume/">C13-ShamelessMax-14_Resume</a>
        </ol>
</details>


<details>
    <summary> 2) Для выполнения тестов нажать на <code>Build Now</code></summary>
      <img src="resources/images/jenkins page.png">
</details>

<details>
    <summary> 3) По окончанию тестов для просмотра результатов нажать на иконку 
<code>Allure Report</code></summary>
      <img src="resources/images/jenkins page allure.png">
</details>

<h3>Дополнительно</h3>
<details>
    <summary> Уведомление о выполнении тестов может быть отправлено через Telegram 
<img src="resources/icons/play.gif" height="40">
</summary>
        <img src="resources/images/telegram screen.png">
</details>
<details>
    <summary>Процесс выполнения теста может быть сохранён в формате видео<img 
src="resources/icons/video.gif" height="40">
</summary>
        <img src="resources/images/video.gif">
</details>
