<script setup lang="ts">
import { ref } from "vue";
import {Portal} from "portal-vue";
import StatusBar from "@/components/StatusBar.vue";
import StatusTable from "@/components/StatusTable.vue";
import SubMenu from "@/components/SubMenu.vue";

const variants = [
  {
    label: 'Первый вариант',
    value: 1
  },
  {
    label: 'Второй вариант',
    value: 2
  },
  {
    label: 'Третий вариант',
    value: 3
  },
  {
    label: 'Четвертый вариант',
    value: 4
  }
];

const tabs = ref([
  {
    label: 'Подразделение',
    value: 1,
  },
  {
    label: 'Подразделение',
    value: 2,
  },
  {
    label: 'Подразделение',
    value: 3,
  },
  {
    label: 'Подразделение',
    value: 4,
  },
  {
    label: 'Подразделение',
    value: 5,
  },
  {
    label: 'Подразделение',
    value: 6,
  },

])
const currentVariant = ref(variants[0])
</script>

<template>
  <section class="user-statistics-page">
    <portal to="header-portal">
      <div class="user-statistics-page__controls">
        <v-select
            v-model="currentVariant"
            class="user-list-page__select"
            :items="variants"
            item-title="label"
            item-value="value"
            density="compact"
            variant="solo"
            return-object
            hide-details
        ></v-select>
        <v-text-field
            class="user-list-page__input"
            type="date"
            variant="solo"
            density="compact"
            hide-details
        >
        </v-text-field>
        <v-icon icon="mdi-arrow-right-thin"/>
        <v-text-field
            class="user-list-page__input"
            type="date"
            variant="solo"
            density="compact"
            hide-details
        >
        </v-text-field>
      </div>
    </portal>
    <sub-menu
        class="user-statistics-page__nav"
        :tabs="tabs"
    />
    <status-bar class="user-statistics-page__bar" />
    <status-table class="user-statistics-page__table"/>
  </section>
</template>

<style scoped lang="scss">
  .user-statistics-page {
    &__nav {
      margin-bottom: 16px;
    }

    &__controls {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    &__bar {
      margin-bottom: 28px;
    }

    &__table {
      width: 100%;
    }
  }
</style>
