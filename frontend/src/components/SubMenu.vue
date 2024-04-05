<script setup lang="ts">
import { ref } from "vue";

type TabType = {
  label: string
  value: number
}
const props = defineProps<{
  tabs: TabType[]
}>()
const tab = ref(0);
</script>

<template>
  <nav class="sub-menu bg-grey-lighten-4">
    <v-tabs
        v-model="tab"
        align-tabs="start"
        color="black"
    >
      <v-tab
          v-for="(tab, index) in tabs"
          :value="tab.value"
          class="survey-page__tab"
          :key="index"
      >
        {{ tab.label }}
      </v-tab>
    </v-tabs>
    <slot />
  </nav>
</template>

<style scoped lang="scss">
  .sub-menu {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 30px;
    align-items: center;
    padding: 20px;
    border-radius: 10px;
  }
</style>
