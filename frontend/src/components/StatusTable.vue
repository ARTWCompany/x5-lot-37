<script setup lang="ts">
import { reactive } from "vue";
import ListPagination from "@/components/ListPagination.vue";

const formatter = new Intl.NumberFormat("ru");
const formatNumber = (rawNumber: number) => formatter.format(rawNumber);

const clients = reactive({
  page: 5,

  results: [
    {
      id: 1,
      canal: 'Сайт',
      clientCount: 4500,
      conversion: 95,
      transitions: 3200,
      visits: 4500,
      cost: 4500
    },{
      id: 2,
      canal: 'Сайт',
      clientCount: 4500,
      conversion: 95,
      transitions: 3200,
      visits: 4500,
      cost: 4500
    },
    {
      id: 3,
      canal: 'Сайт',
      clientCount: 4500,
      conversion: 95,
      transitions: 3200,
      visits: 4500,
      cost: 4500
    },
    {
      id: 4,
      canal: 'Сайт',
      clientCount: 4500,
      conversion: 95,
      transitions: 3200,
      visits: 4500,
      cost: 4500
    },
    {
      id: 5,
      canal: 'Сайт',
      clientCount: 4500,
      conversion: 95,
      transitions: 3200,
      visits: 4500,
      cost: 4500
    },
    {
      id: 6,
      canal: 'Сайт',
      clientCount: 4500,
      conversion: 95,
      transitions: 3200,
      visits: 4500,
      cost: 4500
    },
  ]
})
</script>

<template>
  <div>
    <table class="status-table">
      <caption class="visually-hidden">Статистика</caption>
      <tbody>
        <tr>
          <th>№</th>
          <th>Канал</th>
          <th>Зарегистрировалось</th>
          <th>Конверсия</th>
          <th>Переходы</th>
          <th>Посещения</th>
          <th>Стоимость</th>
        </tr>
        <tr
            v-for="(client, index) in clients.results"
            :key="client.id"
        >
          <td>{{ index + 1 }}</td>
          <td>{{ client.canal }}</td>
          <td>{{ formatNumber(client.clientCount) }}</td>
          <td>{{ `${ client.conversion }%` }}</td>
          <td>{{ formatNumber(client.transitions) }}</td>
          <td>{{ formatNumber(client.visits) }}</td>
          <td>{{ formatNumber(client.cost) }}</td>
        </tr>
      </tbody>
    </table>
    <list-pagination />
  </div>
</template>

<style scoped lang="scss">
  .status-table {
    width: 100%;
    text-align: left;

    &,
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
  }
</style>
