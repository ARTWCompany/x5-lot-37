<script setup lang="ts">
const props = defineProps<{
  title?: string
}>()
</script>

<template>
  <div class="toolbar bg-white">
    <h1
        v-if="title"
        class="toolbar__title"
    >
      {{ title }}
    </h1>
    <div class="toolbar__slot">
      <slot/>
    </div>
  </div>
</template>

<style scoped lang="scss">
  .toolbar {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 32px;
    padding: 24px 54px;
    border-radius: 10px;

    &__title {
      font-weight: 500;
      font-size: 34px;
      line-height: 1.2;
    }

    &__slot {
      display: flex;
      min-width: 188px;
      grid-column: 2 / -1;
    }
  }
</style>
