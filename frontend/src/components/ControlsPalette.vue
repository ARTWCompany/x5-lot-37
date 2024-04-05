<script setup lang="ts">

</script>

<template>
  <div class="controls-palette">
    <ul class="controls-palette__list">
      <li>
        <v-btn
            class="bg-white flex-grow-1"
            width="auto"
            variant="outlined"
            rounded="5"
        >
          Фильтр
        </v-btn>
      </li>
      <li>
        <v-btn
            class="bg-white flex-grow-1"
            width="фгещ"
            variant="outlined"
            rounded="5"
        >
          Добавить группу
        </v-btn>
      </li>
    </ul>
  </div>
</template>

<style scoped lang="scss">
  .controls-palette {
    padding: 10px;
    border: 1px solid black;

    &__list {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      list-style: none;
    }
  }
</style>
