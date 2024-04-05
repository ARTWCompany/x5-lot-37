<script setup lang="ts">
type Option = Array<{label: string, value: number | string}>
  type Props = {
    options: Option[]
    label: string
  }
  defineProps<Props>()
</script>

<template>
  <section class="canals-panel-column bg-grey-lighten-4">
    <h3 class="canals-panel-column__title">
      {{ label }}
    </h3>
    <ul class="canals-panel-column__list">
      <li
          v-for="(option, index) in options"
          :key="index"
          class="canals-panel-column__item"
      >
        <v-select
            class="canals-panel-column__select"
            :items="option"
            item-title="label"
            item-value="value"
            :label="label"
            density="compact"
            variant="solo"
            return-object
            hide-details
        ></v-select>
      </li>
    </ul>
  </section>
</template>

<style scoped lang="scss">
  .canals-panel-column {
    padding: 20px 16px 30px;
    border-radius: 10px;

    &__item {
      margin-bottom: 14px;

      &:last-child {
        margin-bottom: 0;
      }
    }

    &__title {
      margin-bottom: 20px;
      color: #797979;
      font-size: 16px;
      line-height: 1;
      font-weight: 400;
    }
  }
</style>
