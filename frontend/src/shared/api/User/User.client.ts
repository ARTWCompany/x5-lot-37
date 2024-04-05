import { BaseClient } from "@/shared/api/Base/Base.client";
import routes from "./routes";
import type { User } from "./types";

export class UserClient extends BaseClient {
  async getUsersList(): Promise<User[] | undefined> {
    try {
      return await this.#fetchUsersList();
    } catch (error) {
      console.error(`getUsersList ${error}`);
    }
  }
  async #fetchUsersList(): Promise<User[]> {
    return this.sendGetRequest(routes.list)
  }
}
