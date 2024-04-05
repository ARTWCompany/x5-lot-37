import type {
  AxiosResponse,
  AxiosInstance } from 'axios';

const ERROR_MESSAGE = 'Нет данных от API';

abstract class BaseClient {
  #apiInstance: AxiosInstance;

  constructor($apiInstance: AxiosInstance) {
    this.#apiInstance = $apiInstance;
  }

  protected async sendGetRequest<ResponseType>(
    url: string,
    query: Record<string, unknown> = {}
  ): Promise<ResponseType> {
    const response = await this.#apiInstance.get<ResponseType>(
      url,
      { params: query }
    );

    if (!response) {
      throw new Error(ERROR_MESSAGE);
    }

    return response.data;
  }

  protected async sendPostRequest<ResponseType = AxiosResponse>(
    url: string,
    data: any,
    query: Record<string, unknown> = {}
  ): Promise<ResponseType> {
    const response = await this.#apiInstance.post<ResponseType>(
      url,
      data,
      { params: query }
    );

    if (!response) {
      throw new Error(ERROR_MESSAGE);
    }

    return response.data;
  }
}

export { BaseClient };
