<script setup lang="ts">
import ListPagination from "@/components/ListPagination.vue";
import {reactive, ref} from "vue";
import dayjs from "dayjs";

const formatter = new Intl.NumberFormat("ru");
const formatNumber = (rawNumber: number) => formatter.format(rawNumber);
const formatDate = (date: number) => dayjs(date).format('DD.MM.YYYY')

const companies = reactive({
  page: 5,

  results: [
    {
      id: 1,
      type: 'Массовая',
      date: 1711204012763,
      group: 'Акционная',
      status: 'Завершена',
      author: 'avtor.aa',
      conversion: 4500,
    },
    {
      id: 2,
      type: 'Массовая',
      date: 1711204012763,
      group: 'Акционная',
      status: 'Завершена',
      author: 'avtor.aa',
      conversion: 4500,
    },
    {
      id: 3,
      type: 'Массовая',
      date: 1711204012763,
      group: 'Акционная',
      status: 'Завершена',
      author: 'avtor.aa',
      conversion: 4500,
    },
    {
      id: 4,
      type: 'Массовая',
      date: 1711204012763,
      group: 'Акционная',
      status: 'Завершена',
      author: 'avtor.aa',
      conversion: 4500,
    },
    {
      id: 5,
      type: 'Массовая',
      date: 1711204012763,
      group: 'Акционная',
      status: 'Завершена',
      author: 'avtor.aa',
      conversion: 4500,
    }
  ]
})

const variants = [
  {
    label: 'Первый вариант',
    value: 1
  },
  {
    label: 'Второй вариант',
    value: 2
  },
  {
    label: 'Третий вариант',
    value: 3
  },
  {
    label: 'Четвертый вариант',
    value: 4
  }
]
const currentVariant = ref(variants[0])
</script>

<template>
  <div class="company-table">
    <div class="company-table__filters">
      <v-select
          v-model="currentVariant"
          class="company-table__select"
          :items="variants"
          item-title="label"
          item-value="value"
          density="compact"
          variant="solo"
          return-object
          hide-details
      ></v-select>
      <v-select
          v-model="currentVariant"
          class="company-table__select"
          :items="variants"
          item-title="label"
          item-value="value"
          density="compact"
          variant="solo"
          return-object
          hide-details
      ></v-select>
      <v-select
          v-model="currentVariant"
          class="company-table__select"
          :items="variants"
          item-title="label"
          item-value="value"
          density="compact"
          variant="solo"
          return-object
          hide-details
      ></v-select>
      <div class="company-table__sort">
        <v-select
            v-model="currentVariant"
            class="company-table__select"
            :items="variants"
            item-title="label"
            item-value="value"
            density="compact"
            variant="solo"
            return-object
            hide-details
        ></v-select>
      </div>
    </div>
    <table>
      <caption class="visually-hidden">Компании</caption>
      <tbody>
      <tr>
        <th>№</th>
        <th>Тип</th>
        <th>Дата</th>
        <th>Группа</th>
        <th>Статус</th>
        <th>Автор</th>
        <th>Конверсия</th>
      </tr>
      <tr
          v-for="(company, index) in companies.results"
          :key="company.id"
      >
        <td>{{ index + 1 }}</td>
        <td>{{ company.type }}</td>
        <td>{{ formatDate(company.date) }}</td>
        <td>{{ company.group }}</td>
        <td>
          <div class="company-table__status">{{ company.status }}</div>
        </td>
        <td>{{ company.author }}</td>
        <td>{{ formatNumber(company.conversion) }}</td>
      </tr>
      </tbody>
    </table>
    <list-pagination />
  </div>
</template>

<style scoped lang="scss">
  .company-table {
    text-align: left;

    table {
      width: 100%;
    }

    table,
    th,
    td {
      border: 1px solid #bdbdbd;
      border-collapse: collapse;
    }

    td,
    th {
      height: 48px;
      padding-left: 10px;
    }

    &__status {
      display: grid;
      place-content: center;
      width: fit-content;
      min-height: 32px;
      padding: 2px 6px;
      min-width: 130px;
      font-size: 16px;
      font-weight: 400;
      border-radius: 6px;
      border: 1px solid #bdbdbd;
    }

    &__filters {
      display: grid;
      grid-template-columns: repeat(3, 200px) 1fr;
      gap: 20px;
      margin-bottom: 20px;
    }

    &__sort {
      display: flex;
      justify-content: flex-end;

      & > * {
        max-width: 200px;
      }
    }
  }
</style>
