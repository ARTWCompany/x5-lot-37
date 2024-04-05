<script setup lang="ts">
  import { ref } from 'vue';
  const page = ref(1);
</script>

<template>
  <div class="list-pagination">
    <v-pagination
        v-model="page"
        :length="10"
        rounded="0"
    ></v-pagination>
  </div>
</template>

<style scoped lang="scss">
  .list-pagination {
    display: flex;
    justify-content: flex-end;
    padding: 24px 52px;
    background-color: #fff;
  }
</style>
