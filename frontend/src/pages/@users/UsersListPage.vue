<script setup lang="ts">
import {
  onMounted,
  ref,
  type Ref
} from "vue";
import { Portal } from "portal-vue";
import { useApiInstance } from "@/plugins/axios";
import { UserClient } from "@/shared/api/User/User.client";

import ControlsPalette from "@/components/ControlsPalette.vue";
import ClientsList from "@/components/ClientsList.vue";
import type { User } from "@/shared/api/User/types";

const clients: Ref<User[]> = ref([]);

const UserApiClient = new UserClient(useApiInstance())
onMounted(async () => {
  try {
    clients.value = await UserApiClient.getUsersList() || [];
  } catch (error) {
    console.error('Failed to fetch data:', error);
  }
});
</script>

<template>
  <section class="user-list-page">
    <portal to="header-portal">
      <div class="user-list-page__controls">
        <v-btn
          class="bg-white"
          variant="outlined"
          width="auto"
          rounded="5"
        >
          Экспорт
        </v-btn>
        <v-btn
            class="bg-white"
            width="auto"
            variant="outlined"
            rounded="5"
            prepend-icon="mdi-plus"
        >
          Добавить пользователя
        </v-btn>
      </div>
    </portal>
    <controls-palette  class="user-list-page__palette" />
    <transition>
      <clients-list
          v-if="clients?.length"
          :clients="clients"
      />
    </transition>
  </section>
</template>

<style scoped lang="scss">
  .user-list-page {
    &__controls {
      display: flex;
      justify-content: flex-end;
      gap: 20px;
      width: 500px;
    }

    &__palette {
      margin-bottom: 20px;
    }
  }
</style>
