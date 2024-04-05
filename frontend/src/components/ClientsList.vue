<script setup lang="ts">
import {
  computed
} from "vue";
import { plural } from "@/shared/lib/utils/text-utils";
import type { User } from "@/shared/api/User/types";
import { prettyPhone } from "@/shared/lib/utils/mask-utils";

type Props = {
  clients: User[]
}
const props = defineProps<Props>();


const clientsCount = computed(() => props.clients.length)

const clientCountText = computed(() => `${ clientsCount.value } ${plural(clientsCount.value, ['клиент', 'клиента', 'клиентов'])}`)
</script>

<template>
  <table class="client-list">
    <caption class="client-list__caption">
      <b>{{ clientCountText }}</b>
    </caption>
    <tbody>
      <tr>
        <th>
          <v-checkbox
              label="Клиент"
              density="comfortable"
              hide-details
          ></v-checkbox>
        </th>
        <th>ID</th>
        <th>Номер телефона</th>
        <th>Email</th>
      </tr>
      <tr
          v-for="client in clients"
          :key="client.id"
      >
        <td>
          <v-checkbox
              :label="client.name"
              density="comfortable"
              hide-details
          ></v-checkbox>
        </td>
        <td>
          <span>
            {{ client.id }}
          </span>
        </td>
        <td>
          <span v-if="client.phone">
            {{ prettyPhone(client.phone) }}
          </span>
        </td>
        <td>
          <span v-if="client.email">
            {{ client.email }}
          </span>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped lang="scss">
  .client-list {
    width: 100%;
    text-align: left;

    &__caption {
      text-align: left;
    }
  }
</style>
