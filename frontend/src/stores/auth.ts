import { defineStore } from 'pinia'
import {
  ref,
  type Ref
} from 'vue'
export const useAuthStore = defineStore('auth', () => {
  const isAuthenticated = ref(false)
  const user: Ref<Record<string, string> | null> = ref(null)
  const changeUserState = (state: boolean) => isAuthenticated.value = state;
  const setUserData = ( data: Record<string, string>) => user.value = data;
  const removeUserData = () => user.value = null;

  return {
    isAuthenticated,
    changeUserState,
    user,
    setUserData,
    removeUserData
  }
})//
