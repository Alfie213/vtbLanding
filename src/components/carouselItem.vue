<script setup>
import { defineProps, reactive } from "vue";
import btnComponent from "./btnComponent.vue";

const props = defineProps({
    address: String
})
</script>

<template>
    <div class="item">
        <img class="item__map" src="/svg-editor-image (2).svg" alt="">
        <div class="item__content">
            <div class="item__content-addres">
                <p class="item__content-addres--text">Адрес: {{ address }}</p>
                <btnComponent name="Проложить маршрут" />
            </div>
        </div>
    </div>
</template>

<style>
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