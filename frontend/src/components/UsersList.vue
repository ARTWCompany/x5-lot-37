<script setup lang="ts">
import ListMenu from "@/components/ListMenu.vue";
import UserCard from "@/components/UserCard.vue";
import UsersListHead from "@/components/UsersListHead.vue";
import ListPagination from "@/components/ListPagination.vue";

const cards = [
  {
    id: 1,
    name: 'Мухин Иван Георгиевич',
    mail: 'mukhin.ig@mail.ru',
    gender: 'M',
    age: 26,
    city: 'Санкт-Петербург',
  },
  {
    id: 2,
    name: 'Борисова Вероника Егоровна',
    mail: 'borisova.veronika@yandex.ru',
    gender: 'Ж',
    age: 33,
    city: 'Санкт-Петербург',
  },
  {
    id: 3,
    name: 'Мухин Иван Георгиевич',
    mail: 'mukhin.ig@mail.ru',
    gender: 'M',
    age: 26,
    city: 'Санкт-Петербург',
  },
  {
    id: 4,
    name: 'Мухин Иван Георгиевич',
    mail: 'mukhin.ig@mail.ru',
    gender: 'M',
    age: 26,
    city: 'Санкт-Петербург',
  },
  {
    id: 5,
    name: 'Мухин Иван Георгиевич',
    mail: 'mukhin.ig@mail.ru',
    gender: 'M',
    age: 26,
    city: 'Санкт-Петербург',
  },
]

function handleUserEdit<T>(id: T) {
  console.log(`edit user with id ${id}`)
}
</script>

<template>
  <section class="user-list">
    <list-menu class="user-list__menu" />
    <users-list-head class="user-list__titles"/>
    <ul class="user-list__list">
      <li
          v-for="(card, index) in cards"
          :key="card.id"
          class="user-list__item"
      >
        <user-card
            :listNumber="index + 1"
            :id="card.id"
            :name="card.name"
            :mail="card.mail"
            :gender="card.gender"
            :age="card.age"
            :city="card.city"
            @edit="handleUserEdit"
        />
      </li>
    </ul>
    <list-pagination class="user-list__pagination" />
  </section>
</template>

<style scoped lang="scss">
  .user-list {
    &__list {
      position: relative;
      overflow: auto;
      list-style: none;
      border-right: 1px solid #bdbdbd;
      border-left: 1px solid #bdbdbd;
    }

    &__titles {
      margin-bottom: 20px;
    }

    &__item {
      min-width: fit-content;
      border-top: 1px solid #bdbdbd;
    }

    &__pagination {
      border: 1px solid #bdbdbd;
    }
  }
</style>
