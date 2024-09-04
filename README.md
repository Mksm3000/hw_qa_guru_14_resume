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
        <li>01 Переход по ссылкам методом <code>click()</code></li>
        <li>02 Переход по ссылкам методом <code>hover()</code></li>
        <li>03 Создание аккаунта</li>
        <li>04 Ввод логина (успешный и неуспешный)</li>
        <li>05 Работа с корзиной (добавить товар, исправить, удалить)</li>
      </ul>
</details>

<h2> <img src="resources/icons/analytics.gif" height="40"> Запуск тестов и получение 
отчета</h2>
<h3>Локально</h3>
<details>
    <summary> 01. Склонировать репозиторий</summary>
      <ul>
        <li><code>git clone https://github.com/Mksm3000/hw_qa_guru_14_resume.git</code></li>
      </ul>
</details>

<details>
    <summary> 2. Установить зависимости и запустить тесты</summary>
      <ul>
        <li><code>python -m venv .venv</code></li>
        <li><code>source .venv/bin/activate</code></li>
        <li><code>pip install -r requirements.txt</code></li>
        <li><code>pytest .</code></li>
      </ul>
</details>

<details>
    <summary> 3. Получить отчет о прохождении тестов в allure</summary>
      <ul>
        <li><code>allure serve allure-results/</code></li>
      </ul>
</details>

<details>
    <summary> После выполнения команды откроется браузер с отчетом</summary>
      <img src="resources/images/allure-report screen.png" style="visibility:visible;max-width:100%;">
</details>

