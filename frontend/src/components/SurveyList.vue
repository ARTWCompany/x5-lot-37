<script setup lang="ts">
import ListMenu from "@/components/ListMenu.vue";
import SurveyCard from "@/components/SurveyCard.vue";

const cards = [
  {
    id: 1,
    title: 'Удовлетворенность покупателей магазина',
    time: 1711204012763,
    answersCount: 120,
    dateStart: 1711204012763,
    dateEnd: 1712204012763,
    status: 'Завершен'
  },
  {
    id: 2,
    title: 'Оценка развития новых направлений',
    time: 1711204012763,
    answersCount: 120,
    dateEnd: 1712204012763,
    status: 'Завершен'
  },
  {
    id: 3,
    title: 'Определение целевой аудитории',
    time: 1711204012763,
    answersCount: 120,
    dateEnd: 1712204012763,
    status: 'Завершен'
  },
  {
    id: 4,
    title: 'Оценка развития новых направлений',
    time: 1711204012763,
    answersCount: 12,
    dateStart: 1711204012763,
    dateEnd: 1712204012763,
    status: 'Завершен'
  },
  {
    id: 5,
    title: 'Оценка доступности информации о услугах и акциях магазина',
    time: 1711507012763,
    answersCount: 12,
    dateStart: 1711204012763,
    dateEnd: 1712204012763,
    status: 'Завершен'
  },
]
</script>

<template>
  <section class="survey-list">
    <list-menu class="survey-list__menu" />
    <ul class="survey-list__list">
      <li
          v-for="card in cards"
          :key="card.id"
          class="survey-list__item"
      >
        <survey-card
            :title="card.title"
            :date-start="card.dateStart"
            :answers-count="card.answersCount"
            :time="card.time"
            :date-end="card.dateEnd"
            :status="card.status"
        />
      </li>
    </ul>
  </section>
</template>

<style scoped lang="scss">
  .survey-list__list {
    list-style: none;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 64px;
  }
</style>
