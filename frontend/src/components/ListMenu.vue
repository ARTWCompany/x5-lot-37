<script setup lang="ts">

</script>

<template>
  <div class="list-menu bg-grey-lighten-4">
      <v-autocomplete
          variant="underlined"
          density="comfortable"
          placeholder="Поиск"
          style="max-width: 280px;"
          no-data-text="Нет данных"
          item-props
      >
        <template #append-inner>
          <i class="material-icons">search</i>
        </template>
      </v-autocomplete>
      <div class="list-menu__sort">
        <span>Сортировать</span>
        <div class="list-menu__controls">
          <button
              class="list-menu__sort-btn bg-grey-lighten-4"
              type="button"
              aria-label="сортировать по возрастанию"
          >
            <i class="material-icons">arrow_drop_up</i>
          </button>
          <button
              class="list-menu__sort-btn bg-grey-lighten-4"
              type="button"
              aria-label="сортировать по убыванию"
          >
            <i class="material-icons">arrow_drop_down</i>
          </button>
        </div>
      </div>
  </div>
</template>

<style scoped lang="scss">
  .list-menu {
    position: relative;
    overflow: hidden;
    display: flex;
    justify-content: flex-end;
    gap: 80px;
    height: 72px;

    &__sort {
      display: flex;
      align-items: center;
      align-self: flex-start;
      min-height: 52px;
      gap: 6px;
    }

    &__controls {
      display: flex;
      flex-direction: column;
    }

    &__sort-btn {
      width: 20px;
      height: 20px;
      transition: opacity .3s ease;

      &:hover {
        opacity: .7;
      }

      i {
        font-size: 20px;
      }
    }
  }
</style>
