<script setup lang="ts">
import dayjs from "dayjs";
import {computed} from "vue";

const props = defineProps<{
  title: string
  time: number
  answersCount: number
  dateStart?: number
  dateEnd?: number
  status: string
}>()

const formatDate = (date?: number) => dayjs(date).format('DD.MM.YYYY')

const formattedTime = computed(() => {
  return dayjs(props.time).format('h:mm')
})

const date = computed(() => {
  if (props.dateStart && props.dateEnd) {
    return `Дата: ${formatDate(props.dateStart)} - ${formatDate(props.dateEnd)}`
  }
  return `Дата: ${formatDate(props.dateStart || props.dateEnd)}`
});
</script>

<template>
  <article class="survey-card">
    <header class="survey-card__header bg-grey-lighten-1">
      <h3 class="survey-card__title">{{ title }}</h3>
      <v-btn
          class="bg-grey-lighten-1"
          size="small"
          variant="text"
          icon=""
      >
        <i class="material-icons">more_vert</i>
      </v-btn>
    </header>
    <div class="survey-card__content">
      <div class="survey-card__cell">
        <span class="survey-card__result">{{ answersCount }}</span>
        <span class="survey-card__result-name">
          ответов<br> получено
        </span>
      </div>
      <div class="survey-card__cell">
        <span class="survey-card__result">{{ formattedTime }}</span>
        <span class="survey-card__result-name">
          время<br> заполнения
        </span>
      </div>
      <div class="survey-card__cell survey-card__cell--date">
        <div
            v-if="dateEnd || dateStart"
            class="survey-card__date">
          {{ date }}
        </div>
        <div class="survey-card__status">{{ status }}</div>
      </div>
    </div>
  </article>
</template>

<style scoped lang="scss">
  .survey-card {
    &__header {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 20px;
      padding: 34px 24px 34px 44px;
      border-radius: 12px 12px 0 0;
    }

    &__title {
      font-size: 24px;
      line-height: 34px;
      font-weight: 400;
    }

    &__content {
      display: grid;
      grid-template-columns: 220px 220px 1fr;
      min-height: 220px;
      padding: 32px 0;
      background-color: white;
      border-radius: 0 0 12px 12px;
    }

    &__cell {
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      padding: 0 10px;
      text-align: center;
      border-right: 1px solid #eee;

      &--date {
        align-items: flex-start;
        justify-content: flex-start;
        padding: 26px 32px;
      }
    }

    &__result {
      margin-bottom: 4px;
      font-size: 56px;
      font-weight: 500;
      line-height: 1;
    }

    &__result-name {
      font-size: 20px;
      font-weight: 400;
      line-height: 1.2;
    }

    &__date {
      margin-bottom: 16px;
      font-size: 20px;
      font-weight: 500;
    }

    &__status {
      display: grid;
      place-content: center;
      min-height: 40px;
      padding: 10px;
      min-width: 130px;
      font-size: 16px;
      font-weight: 400;
      border-radius: 6px;
      border: 1px solid #bdbdbd;
    }
  }
</style>
