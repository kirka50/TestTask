<template class="files">
  <p v-for="item in fileData.data.fileNames" :key="item" v-on:click="downloadFileByName(item)">{{item}}</p>
</template>

<script>
import axios from "axios";

export default {
  name: "fileDownload",
methods: {
  async getAllFileNames() {
  await axios.get("http://kaikane.ru/listAll/")
        .then(response => {
          this.fileData = response
        })
        .catch(error => {
          console.log(error.response)
        })
  },
 async downloadFileByName(item)
  {
    console.log(item[0])
    await axios.get("http://kaikane.ru/downloadFile/",{params: {file_name: item[0]}})
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
  beforeMount(){
    this.getAllFileNames()
    },

  data(){
    return {
      fileData: ''
    }
  }
}
</script>


<style scoped>
.files{
  display: flex;
  flex-direction: row;
}
</style>
