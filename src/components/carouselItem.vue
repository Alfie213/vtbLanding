<script setup>
import { defineProps, onMounted, toRefs, ref, watch } from "vue";
import btnComponent from "./btnComponent.vue";

const props = defineProps({
    bankObj: Object
})
const {bankObj} = toRefs(props)
console.log(bankObj.value.latitude)
const isVisible = ref(false);

// let latitude
// let longitude

// тут мы получаем долготу и широту нашего
// if ('geolocation' in navigator) {
//     navigator.geolocation.getCurrentPosition(function(position) {
//         latitude = position.coords.latitude;
//         longitude = position.coords.longitude;
//     }, function(error) {
//         console.error('Ошибка геолокации:', error);
//     });
// } else {
//     console.error('Геолокация не поддерживается в этом браузере');
// }

const mapElement = ref(null);
onMounted(() => {
    ymaps.ready(init);
});


function init(){
    if (mapElement.value) {
        const myMap = new ymaps.Map(mapElement.value, {
            center: [bankObj.value.latitude, bankObj.value.longitude],
            zoom: 16
        }, {
            searchControlProvider: 'yandex#search'
        })

        myMap.geoObjects
        .add(new ymaps.Placemark([bankObj.value.latitude, bankObj.value.longitude], {
            balloonContent: `${bankObj.value.address}`
        }, {
            preset: '{islands#dotIcon}',
            iconColor: '#735184'
        }))
    }
}
const loc = "https://yandex.ru/maps/?rtext=~" + bankObj.value.latitude + "," + bankObj.value.longitude
</script>

<template>
    <div class="item">
        <div id="map" class="item__map" ref="mapElement"></div>
        <div class="item__content">
            <div class="item__content-addres">
                <p class="item__content-addres--text">Адрес: {{ bankObj.address}}</p>
            </div>
            <div class="item__content-info">
                <p class="item__content-addres--text">Дистанция: {{ bankObj.distance.toFixed(2) }} км.</p>
                <p class="item__content-addres--text">Время в очереди: {{ bankObj.time }} мин.</p>
                <p class="item__content-addres--text">Пандус: {{ bankObj.hasRamp === "N" ? "Отсутствует" : bankObj.hasRamp === "" ? "Отсутствует" : "Присутствует"}}</p>
            </div>
            <div class="item__content-link">
                <a :href="loc" :target="_blank" class="btnItem">Проложить маршрут</a>
            </div>
        </div>
    </div>
    <div class="blocks-container">
      <div v-for="(item, index) in items" :key="index" class="my-block">
        <p>Блок {{ index + 1 }}</p>
        <p>{{ item }}</p>
      </div>
    </div>
</template>

<style>
    .blocks-container {
    text-align: center; /* Центрировать блоки по горизонтали */
    }

    .my-block {
    display: inline-block; /* Выстраиваем блоки в ряд */
    margin: 10px; /* Добавляем отступ между блоками */
    padding: 10px;
    border: 1px solid #ccc;
    background-color: lightblue;
    }

    .item {
        display: flex;
        flex-direction: column;
        padding: 20px;
    }

    .item__map {
        border-radius: 12px;
        height: 300px;
        opacity: 0.7;
        margin-bottom: 15px;
    }

    .item__content-addres {
        display: flex;
        align-items: baseline;
        gap: 10px;
        color: #eee;
        font-size: 18px;
    }

    .btnItem {
    color: #fff;
    background: linear-gradient(90deg, rgba(0,57,255,1) 0%, rgba(0,133,255,1) 100%);
    padding: 10px 17px;
    outline: none;
    border: none;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
    }

    .item__content-link {
        position: relative;
        top: 15px;
    }
    
    .item__content-addres--text {
        color: #ccc;
        font-size: 18px;
        margin-bottom: 10px;
    }   
</style>