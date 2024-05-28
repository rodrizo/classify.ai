<template>
  <v-container>
    <v-responsive
      class="align-centerfill-height mx-auto mt-10"
      max-width="900"
    >
      <v-data-table 
        :headers="headers"
        :items="values"
      >
      </v-data-table>
    </v-responsive>

  </v-container>
</template>

<script>
  export default {
    mounted() {
      this.getData()
    },
    props: {
      results: Array // Prop para recibir el array de usuarios
    },
    data: () => ({
      headers: [
        { align: 'start', key: 'id', title: 'Id'},
        { key: 'text', title: 'Texto' },
        { key: 'classification', title: 'Clasificacion' },
        { key: 'emoji', title: 'Emoción' },
      ],
      values: [
        {
          id: '',
          text: '',
          classification: '',
          emoji: '',
        }
      ],
    }),
    methods: {
      getData(){
        console.log("showing datatable")
        console.log(this.results)
        this.values = this.results;
      }
    }
  };
</script>