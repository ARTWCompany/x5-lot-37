<script setup lang="ts">
import { Portal } from "portal-vue";
import {ref} from "vue";
import SubMenu from "@/components/SubMenu.vue";
import CompanyTable from "@/components/CompanyTable.vue";

const tabs = ref([
  {
    label: 'Названия',
    value: 1,
  },
  {
    label: 'Группы',
    value: 2,
  },
])
</script>

<template>
  <section class="user-company-page">
    <portal to="header-portal">
      <div class="user-company-page__controls">
        <v-autocomplete
            variant="solo"
            placeholder="Поиск"
            style="width: 200px;"
            no-data-text="Нет данных"
            density="compact"
            item-props
            hide-details
        >
          <template #append-inner>
            <i class="material-icons">search</i>
          </template>
        </v-autocomplete>
        <v-text-field
            class="user-company-page__input"
            type="date"
            variant="solo"
            density="compact"
            hide-details
        >
        </v-text-field>
        <v-icon icon="mdi-arrow-right-thin"/>
        <v-text-field
            class="user-company-page__input"
            type="date"
            variant="solo"
            density="compact"
            hide-details
        >
        </v-text-field>
      </div>
    </portal>
    <sub-menu
        class="user-company-page__nav"
        :tabs="tabs"
    >
      <div class="user-company-page__nav-controls">
        <v-btn
            class="bg-white flex-grow-1"
            height="40"
            variant="flat"
            rounded="5"
        >
          Добавить группу
        </v-btn>
        <v-btn
            class="bg-light-blue-darken-2 flex-grow-1"
            height="40"
            variant="flat"
            rounded="5"
        >
          Создать
        </v-btn>
      </div>
    </sub-menu>
    <company-table />
  </section>
</template>

<style scoped lang="scss">
  .user-company-page {
    &__nav {
      margin-bottom: 16px;
      padding: 20px;
      border-radius: 10px;
    }

    &__controls {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    &__table {
      width: 100%;
    }

    &__nav-controls {
      display: flex;
      gap: 20px;
    }
  }
</style>
