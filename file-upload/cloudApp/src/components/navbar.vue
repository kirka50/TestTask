<template>
<div class="navbar">
  <div>Навигация</div>
  <button @click="$router.push('/')">Отправить</button>
  <button @click="$router.push('/fileDownload')">Загрузить</button>
</div>
</template>

<script>
export default {
  name: "navbar"
}
</script>

<style scoped>

</style>