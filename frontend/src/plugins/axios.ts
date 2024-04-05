import axios from 'axios'
import type {App} from 'vue'
import { type AxiosInstance } from "axios";

interface AxiosOptions {
  baseUrl?: string
  token?: string
}

let apiInstance: AxiosInstance;

export default {
  install: (app: App, options: AxiosOptions) => {
    apiInstance = axios.create({
      baseURL: options.baseUrl,
      headers: {
        Authorization: options.token ? `Bearer ${options.token}` : '',
      }
    })
    app.config.globalProperties.$axios = apiInstance;
  }
}

export const useApiInstance = () => apiInstance;
