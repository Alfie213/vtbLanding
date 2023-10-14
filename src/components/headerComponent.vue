<script setup>

</script>

<template>
    <header class="header">
        <div class="header__inner">
            <img src="/logo.png" alt="logo_VTB" class="header__logo">
            <nav class="navigation">
                <div class="nav__top">
                    <ul class="nav__top-items">
                        <li class="nav__top-item"><a href="#" class="nav__top-link active">Частным лицам</a></li>
                        <li class="nav__top-item"><a href="#" class="nav__top-link">Самозанятым</a></li>
                        <li class="nav__top-item"><a href="#" class="nav__top-link">Малый и средний бизнес</a></li>
                        <li class="nav__top-item"><a href="#" class="nav__top-link">Крупный бизнес</a></li>
                    </ul>
                    <a href="#" class="nav__top-btn">ВТБ ОНЛАЙН</a>
                </div>
                <div class="nav__bottom">
                    <ul class="nav__bottom-items">
                        <li class="nav__bottom-item"><a href="#" class="nav__bottom-link">Кредиты</a></li>
                        <li class="nav__bottom-item"><a href="#" class="nav__bottom-link">Карты</a></li>
                        <li class="nav__bottom-item"><a href="#" class="nav__bottom-link">Ипотека</a></li>
                        <li class="nav__bottom-item"><a href="#" class="nav__bottom-link">Автокредиты</a></li>
                        <li class="nav__bottom-item"><a href="#" class="nav__bottom-link">Вклады и счета</a></li>
                        <li class="nav__bottom-item"><a href="#" class="nav__bottom-link">Инвестиции</a></li>
                        <li class="nav__bottom-item"><a href="#" class="nav__bottom-link">Онлайн-сервисы</a></li>
                        <li class="nav__bottom-item"><a href="#" class="nav__bottom-link">Платежи и переводы</a></li>
                        <li class="nav__bottom-item"><a href="#" class="nav__bottom-link">Другие услуги</a></li>
                        <li class="nav__bottom-item"><a href="#" class="nav__bottom-link">Привилегия</a></li>
                        <li class="nav__bottom-item"><a href="#" class="nav__bottom-link">Private Banking</a></li>
                    </ul>
                </div>
            </nav>
        </div>
    </header>
</template>

<style>
.header__inner {
    padding: 15px 100px;
    display: flex;
    gap: 20px;
    align-items: center;
    background-color: #1d202a;
    border-bottom: 1px solid #b9c0d3;
}

.header__logo {
    width: 100px;
    position: relative;
    top: -10px;
}

.navigation {
    flex-grow: 1;
}

.nav__top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid #b9c0d3;
}

.nav__top-items {
    display: flex;
    align-items: center;
    list-style: none;
    gap: 20px;
    padding-bottom: 11px;
}

.nav__top-link {
    color: #b9c0d3;
    text-decoration: none;
    font-weight: 700;
    font-size: 13px;
    transition: all .4s;
}

.active {
    color: #fff; 
    position: relative;   
}

.active::before {
    content: '';
    position: absolute;
    left: 0;
    bottom: -14px;
    width: 100%;
    height: 4px;
    border-radius: 3px;
    background-color: #fff;
}

.nav__top-btn {
    color: #5ab0ff;
    text-decoration: none;
    font-size: 18px;
    border: 2px solid #5ab0ff;
    padding: 3px 10px;
    border-radius: 5px;
    position: relative;
    top: -5px;
    transition: .3s;
}

.nav__top-btn:hover {
    color: #fff;
    border-color: #fff;
}

.nav__top-link:hover {
    color: #54a3ec;
    opacity: .9;
}

.nav__bottom-items {
    display: flex;
    gap: 20px;
    list-style: none;
    margin: 18px 0 10px;
}

.nav__bottom-link {
    color: #eee;
    text-decoration: none;
    transition: all .3s;
}

.nav__bottom-link:hover {
    color: #54a3ec;
    opacity: .9;
}
</style>