import Cookies from 'js-cookie';

export class CookiesService {
  setCookies(name: string, value: string, options?: Record<string, string | number | boolean | Date>): void {
    Cookies.set(name, value, options)
  }

  getCookies(name: string) {
    return Cookies.get(name);
  }

  removeCookies(name: string) {
    Cookies.remove(name);
  }
}

export const useCookiesService = () => new CookiesService()
