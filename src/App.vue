<script setup>
import { ref, onMounted } from 'vue'
import headerComponent from './components/headerComponent.vue';
import carouselItem from './components/carouselItem.vue';
import formComponent from './components/formComponent.vue';

const state = {}
let canSee = ref(true)

const carouselItems = ref([])
const carouselList = ref([])
const elems = ref([])
onMounted(() => {
  carouselList.value = document.querySelector('.carousel__list')
  carouselItems.value = document.querySelectorAll('.carousel__item')
  elems.value = Array.from(carouselItems.value);
})

const carouselClick = (event) => {
  let newActive = event.target
  let isItem = newActive.closest('.carousel__item');

  if (!isItem || newActive.classList.contains('carousel__item_active')) {
    return
  }

  update(newActive)
}

const getPos = function (current, active) {
  const diff = current - active;

  if (Math.abs(current - active) > 2) {
    return -current
  }

  return diff;
}

const update = (newActive) => {
  const newActivePos = newActive.dataset.pos;
  
  const current = elems.value.find((elem) => elem.dataset.pos == 0);
  const prev =  elems.value.find((elem) => elem.dataset.pos == -1);
  const next =  elems.value.find((elem) => elem.dataset.pos == 1);
  const first =  elems.value.find((elem) => elem.dataset.pos == -2);
  const last =  elems.value.find((elem) => elem.dataset.pos == 2);

  console.log(current)

 current.classList.remove('carousel__item_active')
 let arr = [current, prev, next, first, last]

 arr.forEach(item => {
    let itemPos = item.dataset.pos;

    item.dataset.pos = getPos(itemPos, newActivePos)
  });
}

let dataForm = ref({})

const handleUpdateData = (data) => {
  dataForm = data;
  canSee.value = false;
}

</script>

<template>
  <div class="container">
    <headerComponent/>
    <div class="carousel">
      <formComponent v-if="canSee" @updateData="handleUpdateData"/>
      <ul v-show="!canSee" @click="carouselClick" class="carousel__list">
        <li class="carousel__item" data-pos="-2"><carouselItem address="ул. Вишневая, д. 14"/></li>
        <li class="carousel__item" data-pos="-1"><carouselItem address="ул. Арбат, д. 19"/></li>
        <li class="carousel__item" data-pos="0"><carouselItem address="ул. Пушкина, д. Колотушкина"/></li>
        <li class="carousel__item" data-pos="1"><carouselItem address="ул. Мира, д. 9"/></li>
        <li class="carousel__item" data-pos="2"><carouselItem address="ул. Энтузиастов, д. 21"/></li>
      </ul>
    </div>
  </div>
</template>

<style>
  * {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }

  body {
    min-height: 100vh;
    margin: 0;
    font-family: 'Roboto', sans-serif;
  }

  .container {
    max-width: 1920px;
    display: flex;
    flex-direction: column;
    height: 100vh;
    background-color: #aaa;
    margin: 0 auto;
    overflow: hidden;
  }

  .carousel {
    background-color: #0b0c0f;
    display: flex;
    height: 100vh;
    justify-content: center;
    align-items: center;
    overflow: hidden;
  }

  .carousel__list {
    display: flex;
    justify-content: center;
    align-items: center;
    list-style: none;
    overflow: hidden;
  }

  .carousel__item {
    width: 950px;
    height: 600px;
    border-radius: 12px;
    position: absolute;
    transition: all .3s ease-in;
    z-index: 100;
  }

  .carousel__item:nth-child(1) {
    background: rgba(29, 32, 42, 1);
  } 

  .carousel__item:nth-child(2) {
    background: rgba(29, 32, 42, 1);
  }

  .carousel__item:nth-child(3) {
    background: rgba(29, 32, 42, 1);
  }

  .carousel__item:nth-child(4) {
    background: rgba(29, 32, 42, 1);
  }

  .carousel__item:nth-child(5) {
    background: rgba(29, 32, 42, 1);
  }

  .carousel__item[data-pos="0"] {
    z-index: 5;
    border: 4px solid rgba(0,57,255,1);
    border-radius: 12px;
  }
    
  .carousel__item[data-pos="-1"],
  .carousel__item[data-pos="1"] {
    opacity: 0.2;
    filter: blur(1px) grayscale(10%);
  }
    
  .carousel__item[data-pos="-1"] {
    transform: translateX(-35%) scale(.9);
    z-index: 4;
  }
    
  .carousel__item[data-pos="1"] {
    transform: translateX(35%) scale(.9);
    z-index: 4;
  }
    
  .carousel__item[data-pos="-2"],
  .carousel__item[data-pos="2"] {
     opacity: 0.4;
      filter: blur(3px) grayscale(20%);
      display: none;
  }
    
  .carousel__item[data-pos="-2"] {
    transform: translateX(-65%) scale(.8);
    z-index: 3;
  }
    
  .carousel__item[data-pos="2"] {
    transform: translateX(65%) scale(.8);
    z-index: 3;
  }

  .carousel__item[data-pos="-2"]:hover,
  .carousel__item[data-pos="2"]:hover,
  .carousel__item[data-pos="-1"]:hover,
  .carousel__item[data-pos="1"]:hover {
    scale: 1.01;
  }

</style>
