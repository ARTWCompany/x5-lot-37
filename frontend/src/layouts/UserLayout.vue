<script setup lang="ts">
import TheHeader from "@/components/TheHeader.vue";
const menu = [
  {
    label: 'mdi-menu',
    value: '/',
  },
  {
    label: 'mdi-view-list',
    value: '/list',
  },
  {
    label: 'mdi-table-clock',
    value: '/statistics',
  },
  {
    label: 'mdi-note-multiple',
    value: '/company',
  },
  {
    label: 'mdi-api',
    value: '/api-clients',
  },
  {
    label: 'mdi-account-circle',
    value: '/settings',
  },
]
</script>

<template>
  <v-app class="app bg-white">
    <div class="app__container">
      <v-navigation-drawer
          class="app__nav bg-grey-lighten-4"
          :width="50"
      >
        <v-list-item
            v-for="(menuItem, index) in menu"
            :key="index"
        >
          <router-link :to="menuItem.value">
            <v-icon
                :icon="menuItem.label"
                size="x-small"
            />
          </router-link>
        </v-list-item>
      </v-navigation-drawer>
      <v-app-bar
          class="app__bar bg-grey-lighten-4"
          :elevation="0"
          height="50"
      >
        <v-app-bar-title>Лот 37</v-app-bar-title>
      </v-app-bar>
      <the-header
          class="app__header"
          is-user-header
          with-title
      />
      <div class="app__main">
        <v-main>
          <router-view/>
        </v-main>
      </div>
    </div>
  </v-app>
</template>

<style scoped lang="scss">
  .app {
    padding: 80px 50px 50px;

    &__container {
      display: grid;
      grid-template-columns: 50px 1fr;
    }

    &__nav {
      grid-column: 1 / 2;
      grid-row: 1 / 3;
    }

    &__header,
    &__bar {
      grid-column: 2 / -1;
    }

    &__main {
      grid-column: 2 / -1;
      max-width: 1920px;
      padding: 14px;
    }
  }
</style>
