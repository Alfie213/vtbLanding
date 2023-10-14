<script setup>
import { defineProps, onMounted, reactive, ref } from "vue";
import btnComponent from "./btnComponent.vue";

const props = defineProps({
    address: String
})

const mapElement = ref(null);

onMounted(() => {
    ymaps.ready(init);
});

// Функция ymaps.ready() будет вызвана, когда
// загрузятся все компоненты API, а также когда будет готово DOM-дерево.
function init(){
    console.log("init");
    // Проверяем наличие элемента mapElement
    if (mapElement.value) {
        // Создание карты
        const myMap = new ymaps.Map(mapElement.value, {
            center: [55.76, 37.64],
            zoom: 7
        });
    }
}
</script>

<template>
    <div class="item">
        <div id="map" class="item__map" ref="mapElement"></div>
        <div class="item__content">
            <div class="item__content-addres">
                <p class="item__content-addres--text">Адрес: {{ address }}</p>
                <btnComponent name="Проложить маршрут" />
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

<script>
export default {
  data() {
    return {
      items: ["Первый блок", "Второй блок", "Третий блок"]
    };
  }
};
</script>

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
    
</style>