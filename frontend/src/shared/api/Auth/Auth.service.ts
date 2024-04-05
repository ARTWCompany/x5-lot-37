// region Imports
import {
  AuthClient,
  useAuthClient
} from './Auth.client';
import {
  useAuthStore
} from "@/stores/auth";

import {
  getTokenExpiredDate,
  getTokenPayload,
} from "@/shared/lib/utils/token-utils";

import {
  useCookiesService
} from "@/shared/services/Cookies/Cookies.service";

// endregion

export class AuthService {
  readonly #authClient: AuthClient;
  readonly #authStore;
  readonly #cookiesService;
  private static instance: AuthService;
  private constructor(store?: ReturnType<typeof useAuthStore>) {
    this.#authStore = store ?? useAuthStore();
    this.#authClient = useAuthClient();
    this.#cookiesService = useCookiesService();
  }

  public static getInstance(store?: ReturnType<typeof useAuthStore>): AuthService {
    if (!AuthService.instance) {
      AuthService.instance = new AuthService(store);
    }
    return AuthService.instance;
  }

  async login (username: string, password: string) {
    try {
      const { refresh, access} = await this.#authClient.login({username, password})
      if (access) {
        this.allowAccess(refresh, access);
      } else {
        this.logout();
      }
    } catch (err) {
      console.error(`[AuthService/login]: ${err}`);
    }
  }

  allowAccess (refresh: string, access: string) {
    const accessPayload = getTokenPayload(access);
    this.setTokens(access, refresh);
    this.#authStore.changeUserState(true);
    this.#authStore.setUserData({userId: accessPayload.user_id, username: accessPayload.username});
  }

  logout () {
    this.#authStore.removeUserData();
    this.#authStore.changeUserState(false);
  }

  async restoreAuth () {
    try {
      if (this.accessToken && this.#authStore.isAuthenticated && this.#authStore.user) {
        return;
      }

      if (!this.accessToken && this.refreshToken) {
        await this.restoreToken(this.refreshToken);
      }

      if (this.accessToken && this.refreshToken) {
        this.allowAccess(this.accessToken, this.refreshToken);
        return;
      }

      this.logout();
    } catch (err) {
      console.error(`[AuthService/restoreAuth]: ${err}`);
      this.logout();
    }
  }

  async restoreToken(refresh: string) {
    const { access } = await this.#authClient.refresh(refresh);
    if (access) {
      this.accessToken = access;
      this.allowAccess(refresh, access)
      return;
    }
  }

  setTokens(access: string, refresh: string) {
    this.#cookiesService.setCookies('access', access, this.getTokenOptions(access));
    this.#cookiesService.setCookies('refresh', refresh, this.getTokenOptions(refresh));
  }

  get accessToken(): string | undefined {
    return this.#cookiesService.getCookies('access');
  }

  set accessToken(value: string) {
    this.#cookiesService.setCookies('access', value, this.getTokenOptions(value));
  }

  get refreshToken() {
    return this.#cookiesService.getCookies('refresh');
  }

  get authStatus() {
    return this.#authStore.isAuthenticated;
  }

  getTokenOptions(token: string) {
    const sameSite = 'lax';
    const path = '/';
    const secure = false;
    const expires = getTokenExpiredDate(token);

    return { path, secure, sameSite, expires };
  }

  removeTokens() {
    this.#cookiesService.removeCookies('access');
    this.#cookiesService.removeCookies('refresh');
  }
}

let service: AuthService | undefined;

export const useAuthClientService = (store?: ReturnType<typeof useAuthStore>) => AuthService.getInstance(store);
