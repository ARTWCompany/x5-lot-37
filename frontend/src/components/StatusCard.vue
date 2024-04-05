<script setup lang="ts">
import { computed } from "vue";

const props = defineProps<{
  status: string,
  readyStatusCount: number,
  readyToSendCount: number,
}>()

const formatter = new Intl.NumberFormat("ru");
const normalizedReadyStatusCount = computed(() => formatter.format(props.readyStatusCount))
const normalizedReadyToSendCount = computed(() => formatter.format(props.readyToSendCount))
</script>

<template>
  <div class="status-card">
    <div class="status-card__head">
      <b  class="status-card__status">
        {{ status }}
      </b>
      <v-icon
          icon="mdi-arrow-right-thin"
          color="grey-lighten-1"
          size="x-large"
      ></v-icon>
    </div>
    <div class="status-card__total-count">
      {{ normalizedReadyStatusCount }}
    </div>
    <div class="status-card__in-progress-count">
      {{ normalizedReadyToSendCount }}
    </div>
  </div>
</template>

<style scoped lang="scss">
  .status-card {
    display: flex;
    flex-direction: column;
    min-height: 170px;
    padding: 26px 18px;
    border: 1px solid #bdbdbd;
    border-radius: 10px;

    &__status {
      font-size: 18px;
    }

    &__total-count {
      margin-top: auto;
      margin-bottom: 8px;
      font-size: 24px;
      font-weight: 600;
    }

    &__in-progress-count {
      font-size: 15px;
      font-weight: 300;
      line-height: 1.2;
    }

    &__head {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 10px;
      margin-bottom: 10px;
    }
  }
</style>
