<template>
   <div class="firstContainer"> <p><file-select v-model="file" @updateParent="onFileChoose" class="fileSelectCont"></file-select></p> </div>
    <template v-if="file">
      <div style="display: flex; flex-direction: column; justify-content: center">
        <button @click="sendFile" class="sendFileBut">Отправить</button>
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
     this.file = null
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

.firstContainer{
  margin: 1%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  font-family: Roboto, sans-serif;
  ;
}
.fileSelectCont{
}
.sendFileBut{
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
