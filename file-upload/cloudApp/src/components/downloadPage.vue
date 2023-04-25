<template>
   <div> <p>Загрузка файлов: <file-select v-model="file" @updateParent="onFileChoose"></file-select></p> </div>
    <template v-if="file">
      <div>
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
      await axios.post('http://kaikane.ru:5000/uploadfile/', this.file, {
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
