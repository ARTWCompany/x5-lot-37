<script setup lang="ts">
  import { ref } from "vue";
  import StatusCard from "@/components/StatusCard.vue";

  const cards = ref(
      [
        {
          id: 1,
          status: 'Отправлено',
          readyStatusCount: 5533909,
          readyToSendCount: 5915543,
        },
        {
          id: 2,
          status: 'Отправлено',
          readyStatusCount: 5533909,
          readyToSendCount: 5915543,
        },
        {
          id: 3,
          status: 'Отправлено',
          readyStatusCount: 5533909,
          readyToSendCount: 5915543,
        },
        {
          id: 4,
          status: 'Отправлено',
          readyStatusCount: 5533909,
          readyToSendCount: 5915543,
        }
      ]
  )
</script>

<template>
  <section class="status-bar">
    <h2 class="visually-hidden">
      Статусы
    </h2>
    <ul  class="status-bar__list">
      <li
          v-for="card in cards"
          :key="card.id"
      >
        <status-card
            :status="card.status"
            :ready-status-count="card.readyStatusCount"
            :ready-to-send-count="card.readyToSendCount"
        />
      </li>
    </ul>
  </section>
</template>

<style scoped lang="scss">
  .status-bar {
    &__list {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 28px;
      list-style: none;
    }
  }
</style>
