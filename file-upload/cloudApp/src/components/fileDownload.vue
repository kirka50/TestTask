<template>
  <div class="bodyContainer">

      <p class="file" v-for="item in fileData.data.fileNames" :key="item" v-on:click="downloadFileByName(item)">{{ item[0] }}</p>

  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "fileDownload",
  methods: {
    async getAllFileNames() {
      await axios.get("http://kaikane.ru:5000/listAll/")
          .then(response => {
            this.fileData = response
          })
          .catch(error => {
            console.log(error.response)
          })
    },
    async downloadFileByName(item) {
      console.log(item[0])
      await axios.get("http://kaikane.ru:5000/downloadFile/", {
        params: {'file_name': item[0]},
        responseType: "blob"
      })
          .then(response => {
            console.log(response)
            let fileURL = window.URL.createObjectURL(new Blob([response.data]));
            let fileLink = document.createElement('a');

            fileLink.href = fileURL;
            fileLink.setAttribute('download', item[0]);
            document.body.appendChild(fileLink);

            fileLink.click();
          })
          .catch(error => {
            console.log(error)
          })
    },
  },
  beforeMount() {
    this.getAllFileNames()
  },

  data() {
    return {
      fileData: ''
    }
  }
}
</script>


<style scoped>

.file {

  padding: 1%;
  align-items: center;
  background: white;
  border-radius: 50px;
}
.bodyContainer{
  margin: 1%;



}
</style>
