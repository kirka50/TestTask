<script setup>
import {RouterLink, RouterView} from 'vue-router'
import Navbar from "./components/navbar.vue";
</script>
<template>
  <div class="all">
    <header class="header">
      <navbar/>
    </header>
    <RouterView/>
  </div>

</template>

<style scoped>
.header {
  display: flex;
  flex-direction: column;
  justify-items: flex-end;
  background: #FFFFFF;
  border-radius: 0 0 50px 50px;
  padding: 1%;
}

.all {
  background: #F4F6FB;
  height: 100vh;
}
html, body {
  margin: 0;

}
</style>
