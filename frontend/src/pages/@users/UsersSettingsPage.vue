<script setup lang="ts">

import CommunicationPanel from "@/components/CommunicationPanel.vue";

const tabs = new Array(5);
tabs.fill(null).forEach((el, index) => {
  tabs[index] = {
    label: 'Подразделение',
    value: index + 1,
  };
});
import SubMenu from "@/components/SubMenu.vue";
import CanalsPanel from "@/components/CanalsPanel.vue";
import CanalControls from "@/components/CanalControls.vue";
</script>

<template>
  <section class="user-settings-page">
    <sub-menu
        class="user-settings-page__nav"
        :tabs="tabs"
    >
    </sub-menu>
    <communication-panel class="user-settings-page__menu"/>
    <v-divider  class="user-settings-page__divider"/>
    <canals-panel class="user-settings-page__canals" />
    <v-divider  class="user-settings-page__divider"/>
    <canal-controls />
  </section>
</template>

<style scoped lang="scss">
  .user-settings-page {
    &__nav {
      margin-bottom: 34px;
    }

    &__menu {
      margin-bottom: 34px;
    }

    &__divider {
      margin-bottom: 24px;
      max-width: 725px;
    }

    &__canals {
      margin-bottom: 32px;
    }
  }
</style>
