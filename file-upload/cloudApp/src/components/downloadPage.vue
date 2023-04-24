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
    sendFile(){
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
