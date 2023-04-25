<template>
  <label class="file-select">
    <div class="select-button">
      <span v-if="file" >Выбранный файл: {{ file.name }}</span>
      <span v-else>Выберите файл</span>
    </div>
    <input type="file" id="file" ref="file" v-on:change="handleFileUpload"/>
  </label>
</template>

<script>
export default {
  props: {

  },
  data(){
    return{
     file:''
    }
  },
  methods: {
    handleFileUpload() {
      this.file = this.$refs.file.files[0]
      this.$emit('updateParent',{
        file: this.file
      })
     // console.log(this.file)
    }
  }
}
</script>

<style scoped>
.file-select > .select-button {
  padding: 1rem;

  color: white;
  background-color: #2EA169;

  border-radius: .3rem;

  text-align: center;
  font-weight: bold;
}

.file-select > input[type="file"] {
  display: none;
}
</style>
