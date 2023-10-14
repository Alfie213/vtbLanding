<script setup>
import {ref, defineModel, defineEmits} from 'vue'

const city = ref(defineModel())
const street = ref(defineModel())
const house = ref(defineModel())

const emits = defineEmits(['updateData'])

const updateData = () => {
    const data = ref({
        cityData: city.value, 
        streetData: street.value, 
        houseData: house.value
    })
    emits('updateData', data.value);
    
}

</script>

<template>
    <form class="form" action="#">
        <h2 class="form__title">Укажите необходимую информацию</h2>
        <label for="form__title-serv" class="labelForm">Выберите услугу</label>
        <select name="service" id="form__title-serv" class="inputForm">
            <option class="optionForm" value="get">Получение карты</option>
            <option class="optionForm" value="nal">Кредит наличными</option>
            <option class="optionForm" value="ecspr">Экспресс кредит</option>
            <option class="optionForm" value="ref">Рефинансирование</option>
            <option class="optionForm" value="zalog">Кредит под залог недвижимости</option>
            <option class="optionForm" value="more">Другие услуги</option>
        </select>
        <label for="form__city" class="labelForm">Город:</label>
        <input type="text" id="form__city" class="inputForm" placeholder="Ввод" v-model="city">

        <label for="form__street" class="labelForm">Улица:</label>
        <input type="text" id="form__street" class="inputForm" placeholder="Ввод" v-model="street">

        <label for="form__house" class="labelForm">Дом:</label>
        <input type="text" id="form__house" class="inputForm" placeholder="Ввод" v-model="house">

        <p class="labelForm">Наличие пандуса:</p>
        <div class="redioInput">
            <input type="radio" id="yes" name="info" value="yes">
            <label for="yes">Важно</label>
        </div>
        <div class="redioInput">
            <input type="radio" id="no" name="info" value="no">
            <label for="no">Неважно</label>
        </div>

        <a @click="updateData" href="#" class="form__link" >Получить информацию о банках</a>
    </form>
</template>

<style>
.form {
    color: #fff;
    display: flex;
    flex-direction: column;
    background-color: #1d202a;
    padding: 20px 60px;
    border: 1px solid #ccc;
    border-radius: 12px;
}

.form__title {
    margin-bottom: 20px;
}

.labelForm {
    color: #eee;
    font-size: 14px;
    margin-bottom: 3px;
    opacity: 0.8;
}

.inputForm {
    margin-bottom: 15px;
    background-color: transparent;
    border: 1px solid #eee;
    color: #eee;
    outline: none;
    padding: 10px;
}

.optionForm {
    color: #111
}

.form__link {
    margin: 20px auto;
    text-decoration: none;
    color: #eee;
    border: 1px solid #eee;
    padding: 10px 40px; 
    border-radius: 12px;
    transition: all .3s;
}

.form__link:hover {
    border-radius: 0;
    background-color: #eee;
    color: #1d202a;
}

.redioInput {
    display: flex;
    gap: 10px;
}

</style>