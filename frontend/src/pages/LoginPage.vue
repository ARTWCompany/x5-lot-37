<script setup lang="ts">
// region Imports
import {
  computed,
  ref
} from "vue";
import {
  useAuthClientService
} from "@/shared/api/Auth/Auth.service";
import {
  useRouter
} from "vue-router";
// endregion

  const ANIMATION_DURATION_IN_MS = 1000;
  const login= ref('');
  const password= ref('');
  const isLoading = ref(false);

  const AuthService = useAuthClientService();

  const form = ref<null | HTMLFormElement>(null)
  const isFormShaking = ref(false)

  const validationRules = {
    loginRules: [
      (value:string) => !!value || 'Имя пользователя обязательно',
      (value:string) => (value && value.length >= 3) || 'Имя пользователя должно быть длиннее 3 символов',
    ],
    passwordRules: [
      (value:string) => !!value || 'Пароль обязателен',
      (value:string) => (value && value.length >= 4) || 'Пароль должно быть длиннее 4 символов',
    ],
  }

  const router = useRouter();

  const shakeForm = () => {
    isFormShaking.value = true;
    setTimeout(() => isFormShaking.value = false, ANIMATION_DURATION_IN_MS)
  }
  const handleSubmit = async function () {
    isLoading.value = true;
    const isFormValid = await form.value!.validate();
    if (!isFormValid.valid) {
      shakeForm();
      return;
    }
    await AuthService.login(login.value, password.value);
    if (AuthService.authStatus) {
      await router.push('/list')
    } else {
      shakeForm();
    }
    isLoading.value = false;
  }
</script>

<template>
  <div class="login-page">
    <v-sheet class="login-page__modal bg-grey-lighten-4">
      <v-form
          ref="form"
          fast-fail
          :ripple="false"
          :class="['login-page__form', {['login-page__form--shaking']: isFormShaking}]"
          @submit.prevent="handleSubmit"
      >
        <v-text-field
            v-model="login"
            label="Ваше имя"
            :rules="validationRules.loginRules"
            variant="solo"
            density="comfortable"
        />
        <v-text-field
            v-model="password"
            label="Пароль"
            :rules="validationRules.passwordRules"
            variant="solo"
            density="comfortable"
        />
        <a href="#" class="text-body-2 font-weight-regular">Забыли пароль?</a>
        <v-btn
            type="submit"
            color="light-blue-darken-2"
            block class="mt-2"
            :loading="isLoading"
        >
          Войти
        </v-btn>
      </v-form>
      <div class="login-page__recommendation">
        <p class="text-body-2">Нет аккаунта? <a href="#">Зарегистрироваться</a></p>
      </div>
    </v-sheet>
  </div>
</template>

<style scoped lang="scss">
  .login-page {
    display: grid;
    place-content: center;
    height: 100vh;

    &__modal {
      width: 416px;
      padding: 32px;
      border-radius: 10px;
    }

    &__recommendation {
      margin-top: 6px;
    }

    &__form {
      &--shaking {
        animation: shake 1s ease;
        animation-iteration-count: infinite;
      }
    }
  }
</style>
