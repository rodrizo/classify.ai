<template>
  <v-form
      @submit.prevent="addEmotion"
      ref="form"
  >
  <v-btn
          color="success"
          class="me-4 mt-4"
          type="submit"
          prepend-icon="mdi-plus"
          rounded="lg"
        >
          Crear
        </v-btn>
  
  </v-form>
</template>

<script>
  export default {
    data: () => ({
      overlay: false,
      result: ''
    }),

    watch: {
      overlay (val) {
        val && setTimeout(() => {
          this.overlay = false
        }, 2000)
      },
    },
    methods: {
      
      async addEmotion() {
        await fetch('https://0712bf0e-f0df-4299-850c-16e09f87b347.mock.pstmn.io/',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          // body: JSON.stringify(this.text)
        }).then(response => response.json()).then(x => {
          this.result = x
          console.log(x)
        });


      }
    }
  }
</script>