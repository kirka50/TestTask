<template class="files">
  <p v-for="item in fileData.data.fileNames" :key="item" v-on:click="downloadFileByName(item)">{{item}}</p>
</template>

<script>
import axios from "axios";

export default {
  name: "fileDownload",
methods: {
  getAllFileNames() {
    axios.get("http://kaikane.ru/listAll/")
        .then(response => {
          this.fileData = response
        })
        .catch(error => {
          console.log(error.response)
        })
  },
  downloadFileByName(item)
  {
    console.log(item[0])
    axios.get("http://kaikane.ru/downloadFile/",{params: {file_name: item[0]}})
        .then(response => {
          console.log(response)
          let fileURL = window.URL.createObjectURL(new Blob([response.data]));
          let fileLink = document.createElement('a');

          fileLink.href = fileURL;
          fileLink.setAttribute('download', 'file.pdf');
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
