<script setup lang="ts">
  const COLUMNS_NAMES = [
    '№',
    'Имя',
    'Эл. почта',
    'Пол',
    'Возраст',
    'Город',
    null
  ]
</script>

<template>
  <div class="user-list-head bg-grey-lighten-3">
    <div
        v-for="(name, index) in COLUMNS_NAMES"
        :key="index"
    >
      {{ name || '' }}
    </div>
  </div>
</template>

<style scoped lang="scss">
  .user-list-head {
    display: grid;
    grid-template-columns: 100px 400px 300px 100px 120px 1fr 145px;
    align-items: center;
    gap: 6px;
    min-height: 72px;
    padding: 10px 70px 10px 30px;
    font-size: 16px;
    font-weight: 300;
    line-height: 1;

    div {
      color: rgba(0, 0, 0, .35);
    }
  }
</style>
