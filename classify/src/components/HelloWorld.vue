<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <v-container>
    <v-responsive
      class="align-centerfill-height mx-auto"
      max-width="700"
    >
      <v-img
        class="mb-10 mt-10"
        height="150"
        src="@/assets/tetris.png"
      />

      <div class="text-center">
        <div class="text-body-1 font-weight-bold mb-1">Bienvenido a</div>

        <h1 class="text-h2 font-weight-bold">Classify.ai</h1>
      </div>

      <div class="py-4" />

      <v-row>
        <v-col cols="12">
          <v-card
            class="py-4"
            color="surface-light"
            rounded="lg"
            variant="elevated"
          >
            <v-card-title>
              <h4 class="text font-weight-bold">Ingresa la frase a clasificar </h4>
            </v-card-title>
            <v-form>
              <v-card-text>
                <v-text-field
                  v-model="text"
                  :loading="loading"
                  append-inner-icon="mdi-magnify"
                  label="Ingresa tu frase acá..."
                  variant="solo"
                  single-line
                  type="text"
                  @click:append-inner="onClick()"
                  ></v-text-field>
              </v-card-text>
            </v-form>
            <div class="text-center">
              <v-chip :ripple="false" link size="x-large">
                <span v-if="lastRecord.classification === 'Comentario positivo'">😃</span>
                <span v-else>🙁</span>
              </v-chip>
            </div>
          </v-card>
        </v-col>
      </v-row>

      <DataTable :results="texts" />

    </v-responsive>
  </v-container>
</template>

<script>

  import DataTable from './DataTable.vue';

  export default {
    components: {
      DataTable,
    },
    computed: {
      lastRecord() {
        return this.texts[this.texts.length - 1];
      },
    },
    data: () => ({
      loaded: false,
      loading: false,
      text: '',
      emotion: '',
      emoji: '',
      id: 1,
      texts: [{id: '', text: '', classification: '', emoji: ''}],
    }),
    methods: {
      generateId() {
        return this.id++;
      },
      async onClick () {
        this.loading = true

        setTimeout(() => {
          this.loading = false
          this.loaded = true
        }, 2000)

        await fetch('https://0712bf0e-f0df-4299-850c-16e09f87b347.mock.pstmn.io/',
        // await fetch('http://127.0.0.1:5000/analyze',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          // body: JSON.stringify(this.text)
        }).then(response => response.json()).then(x => {
          this.emotion = x;
          // console.log(x)
        });

        this.emoji = this.emotion.resultado === 'positivo' ? '😃' : '🙁';

        const newId = this.generateId();

        this.texts.push({ id: newId, text: this.text, classification: 'Comentario ' + this.emotion.resultado, emoji: this.emoji });
        // this.text = "";
        // console.log(this.texts)

        this.text = '';

      },
    },
  }
</script>
