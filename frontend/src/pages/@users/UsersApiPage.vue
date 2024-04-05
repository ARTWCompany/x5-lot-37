<script setup lang="ts">
import { Portal } from "portal-vue";
import CompanyTable from "@/components/CompanyTable.vue";

</script>

<template>
  <section class="user-api-page">
    <portal to="header-portal">
      <div class="user-api-page__controls">
        <v-btn
            class="bg-light-blue-darken-2"
            height="40"
            variant="flat"
            rounded="5"
        >
          Добавить
        </v-btn>
      </div>
    </portal>
    <company-table />
  </section>
</template>

<style scoped lang="scss">
  .user-api-page {
    &__controls {
      display: flex;
      align-items: center;
      gap: 16px;
    }
  }
</style>
