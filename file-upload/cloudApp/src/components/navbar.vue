<template>
<div class="navbar">
  <button @click="$router.push('/')" class="button">Отправить</button>
  <button @click="$router.push('/fileDownload')" class="button">Загрузить</button>
</div>
</template>

<script>
export default {
  name: "navbar"
}
</script>

<style scoped>
.button{
  background: #007BFB;
  border-radius: 50px;
  border: none;
  font-family: Roboto,sans-serif;
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 29px;
  color: white;
  margin: 0.5%;
  padding: 0.5%;
}
</style>