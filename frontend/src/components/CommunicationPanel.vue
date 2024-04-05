<script setup lang="ts">
import {
  ref,
  computed } from "vue";
import { plural } from "@/shared/lib/utils/text-utils";

const variants = ref([
  {
    label: 'За сутки',
    value: 1,
  },

])
const currentVariant = variants.value[0]

const fieldRules = [
  (value: number) => {
    if (value) return true

    return 'Поле обязательно для заполнения'
  },
];

const communicationCount = ref(0)

const respondentsSuffix = computed(() => plural(communicationCount.value, ['коммуникация', 'коммуникации', 'коммуникаций']))
</script>

<template>
  <section>
    <h2 class="communication-panel__title">
      Количество коммуникаций
    </h2>
    <v-checkbox
        label="Максимальное количество коммуникаций с пользователем"
        density="compact"
        hide-details
    ></v-checkbox>
    <div class="communication-panel__controls">
      <v-select
          v-model="currentVariant"
          :items="variants"
          item-title="label"
          item-value="value"
          density="compact"
          variant="solo"
          return-object
          hide-details
      ></v-select>
      <v-text-field
          type="number"
          v-model="communicationCount"
          :rules="fieldRules"
          :suffix="respondentsSuffix"
          density="compact"
          variant="solo"
          hide-details
      ></v-text-field>
    </div>
  </section>

</template>

<style scoped lang="scss">
  .communication-panel {
    &__title {
      margin-bottom: 24px;
      font-size: 22px;
      line-height: 1.2;
      font-weight: 600;
    }

    &__controls {
      display: grid;
      grid-template-columns: 292px 176px;
      gap: 16px;
    }
  }
</style>
