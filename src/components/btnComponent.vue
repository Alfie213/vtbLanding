<script setup>
import { defineProps, reactive } from "vue";

const props = defineProps({
    name: String
})
</script>

<template>
    <button class="btnItem">{{ name }}</button>
</template>

<style>
.btnItem {
    color: #fff;
    background: linear-gradient(90deg, rgba(0,57,255,1) 0%, rgba(0,133,255,1) 100%);
    padding: 10px 17px;
    outline: none;
    border: none;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
}
</style>