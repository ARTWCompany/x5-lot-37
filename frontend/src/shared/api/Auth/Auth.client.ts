import { BaseClient } from "@/shared/api/Base/Base.client";
import routes from "./routes";
import { useApiInstance } from "@/plugins/axios";
import type { Token } from "./types";

export class AuthClient extends BaseClient {
  login(data: { username: string, password: string }):Promise<Token> {
    return  this.sendPostRequest(routes.login, data)
  }

  refresh(refresh: string):Promise<Pick<Token, 'access'>> {
    return  this.sendPostRequest(routes.refresh, { refresh })
  }
}

export const useAuthClient = () => new AuthClient(
  useApiInstance(),
);
