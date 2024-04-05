<script setup lang="ts">
const props = defineProps<{
  listNumber: number,
  id: number | string,
  name: string,
  mail: string,
  gender: string,
  age: number,
  city: string,
}>()

const emit = defineEmits({
  edit: (userId) => {
    if (userId) {
      return true
    } else {
      console.warn('Invalid user id')
      return false
    }
  }
})

function editUser(userId: number | string) {
  emit('edit', userId)
}
</script>

<template>
  <div class="user-card bg-white">
    <div>{{ listNumber }}</div>
    <div>{{ name }}</div>
    <div>{{ mail }}</div>
    <div>{{ gender }}</div>
    <div>{{ age }}</div>
    <div>{{ city }}</div>
    <div class="user-card__edit">
      <v-btn
          class="flex-grow-1"
          height="46"
          variant="outlined"
          rounded="5"
          size="small"
          @click="editUser(props.id)"
      >
        Редактировать
      </v-btn>
    </div>
  </div>
</template>

<style scoped lang="scss">
  .user-card {
    display: grid;
    grid-template-columns: 100px 400px 300px 100px 120px 1fr 145px;
    align-items: center;
    gap: 6px;
    min-height: 72px;
    padding: 10px 70px 10px 30px;
    font-size: 16px;
    font-weight: 300;
    line-height: 1;
    color: #333;

    &__edit {
      display: flex;
    }
  }
</style>
