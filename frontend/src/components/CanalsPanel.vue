<script setup lang="ts">
import {ref} from "vue";
import CanalsPanelColumn from "@/components/CanalsPanelColumn.vue";

const communicationTypeOptions = ref([
    [
      {
        label: 'Коммерческий опрос',
        value: 1,
      },
      {
        label: 'Коммерческий опрос',
        value: 2,
      },
    ],
    [
      {
        label: 'Сервисная коммуникация',
        value: 3,
      },
      {
        label: 'Коммерческий опрос',
        value: 4,
      },
    ],
    [
      {
        label: 'Персональная коммуникация',
        value: 5,
      },
      {
        label: 'Коммерческий опрос',
        value: 6,
      },
    ]
])

</script>

<template>
  <section class="canals-panel">
    <h2 class="canals-panel__title">
      Каналы отправки
    </h2>
    <ul class="canals-panel__list">
      <li class="canals-panel__list-item">
        <canals-panel-column
            :options="communicationTypeOptions"
            label="Тип коммуникации"
        />
      </li>
      <li class="canals-panel__list-item">
        <canals-panel-column
            :options="communicationTypeOptions"
            label="Канал"
        />
      </li>
    </ul>
  </section>
</template>

<style scoped lang="scss">
  .canals-panel {
    &__title {
      margin-bottom: 24px;
      font-size: 22px;
      line-height: 1.2;
      font-weight: 600;
    }

    &__list {
      display: grid;
      grid-template-columns: repeat(2, 390px);
      gap: 30px;
    }
  }
</style>
