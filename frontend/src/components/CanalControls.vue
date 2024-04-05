<script setup lang="ts">
import {
  computed, reactive,
  ref
} from "vue";
import { plural } from "@/shared/lib/utils/text-utils";

const fieldRules = [
  (value: number) => {
    if (value) return true

    return 'Поле обязательно для заполнения'
  },
];

const blockDays = ref(0)
const communicationCount = ref(0)
const blockDaysSuffix = computed(() => plural(blockDays.value, ['день', 'дня', 'дней']))
const communicationCountSuffix = computed(() => plural(communicationCount.value, ['коммуникация', 'коммуникации', 'коммуникаций']))
const optionsSelectedValue = reactive({
  days: 'за сутки',
  communication: 'не доставленно'
})
</script>

<template>
  <section class="canal-controls">
    <h2 class="canals-controls__title">
      Блокировки
    </h2>
    <div class="canals-controls__container">
      <div class="canals-controls__condition bg-grey-lighten-4">
        <v-checkbox
            label="Блокировать на"
            density="compact"
            hide-details
        ></v-checkbox>
        <v-text-field
            type="number"
            v-model="blockDays"
            :rules="fieldRules"
            :suffix="blockDaysSuffix"
            density="compact"
            variant="solo"
            hide-details
        ></v-text-field>
      </div>
      <div class="canals-controls__action bg-grey-lighten-4">
        <span>Если</span>
        <v-select
            v-model="optionsSelectedValue.days"
            :items="['за сутки']"
            item-title="label"
            item-value="value"
            density="compact"
            hide-details
            eager
            variant="solo"
        ></v-select>
        <v-text-field
            v-model="communicationCount"
            type="number"
            :rules="fieldRules"
            :suffix="communicationCountSuffix"
            density="compact"
            variant="solo"
            hide-details
        ></v-text-field>
        <v-select
            v-model="optionsSelectedValue.communication"
            :items="['не доставленно']"
            item-title="label"
            item-value="value"
            density="compact"
            hide-details
            eager
            variant="solo"
        ></v-select>
      </div>
      <v-btn
          height="40"
          width="auto"
          variant="text"
          rounded="5"
      >
        + Добавить условие
      </v-btn>
    </div>
    <div class="canals-controls__buttons">
      <v-btn
          class="bg-light-blue-darken-2"
          height="40"
          width="auto"
          variant="flat"
          rounded="5"
      >
        Сохранить
      </v-btn>
      <v-btn
          class="bg-white"
          height="40"
          width="auto"
          variant="outlined"
          rounded="5"
      >
        Применить ко всем подразделениям
      </v-btn>
    </div>
  </section>
</template>

<style scoped lang="scss">
  .canals-controls {
    &__title {
      margin-bottom: 24px;
      font-size: 22px;
      line-height: 1.2;
      font-weight: 600;
    }

    &__buttons {
      display: flex;
      gap: 16px;
      margin-top: 40px;
    }

    &__container {
      display: grid;
      grid-template-columns: auto auto;
      align-items: start;
      gap: 12px;
      width: fit-content;
    }

    &__condition {
      display: grid;
      grid-template-columns: 1fr 100px;
      align-items: center;
      gap: 10px;
      padding: 10px;
      border-radius: 10px;
    }

    &__action {
      display: grid;
      grid-template-columns: auto repeat(3, 200px);
      align-items: center;
      gap: 10px;
      padding: 10px;
      border-radius: 10px;
    }
  }
</style>
