<template>
   <div> <p>Загрузка файлов: <file-select v-model="file" @updateParent="onFileChoose"></file-select></p> </div>
    <template v-if="file">
      <div>
        <input type="text" v-model="filename" placeholder="file.name">
        <p>{{filename}}</p>
        <button @click="sendFile">Отправить</button>
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
   async sendFile(){
      console.log(this.filename)
      await axios.post('http://kaikane.ru/uploadfile/', this.file, {
        headers: {
          "filename": this.filename,
          'Content-Type': 'multipart/form-data'
        }})
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log('errr')
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
