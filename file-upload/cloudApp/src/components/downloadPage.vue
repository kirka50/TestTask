<template>
   <div> <p>Загрузка файлов: <file-select v-model="file" @updateParent="onFileChoose"></file-select></p> </div>
    <template v-if="file">
      <div>
        <input type="text" v-model="filename" :placeholder="file.file.name">
        <button @click="sendFile">Отправить</button>
        <p>{{filename}}</p>
      </div>
    </template>
</template>

<script>
import FileSelect from './FileSelect.vue'
import axios from 'axios'

export default {
  components: {
    FileSelect,
  },
  methods: {
    onFileChoose(file){
      this.file = file
      this.filename = file.file.name
      console.log(this.file)
    },
    sendFile(){
      this.file.name = this.filename
      axios.post('http://kaikane.ru/uploadfile/', this.file, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }})
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error.response)
          })
      console.log(this.file.name)
    }

  },

  data() {
    return {
      filename: null,
      file: null
    }
  }
}

</script>

<style>



</style>
