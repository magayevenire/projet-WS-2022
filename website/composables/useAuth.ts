import { useRouter, useState } from "#app";
import { IUser } from "~/types/IUser"
import { LoginResponse } from "~~/types/LoginResponse";
// const conf = useRuntimeConfig()
// export const nuxtApp = () => useNuxtApp();
const DJANGO_API_BASE = "http://localhost:8000/api"

export const useAuthCookie = () => useCookie("auth_token");

export async function useUser() {
  const authCookie = useAuthCookie().value;
  const user = useState("user");

  if (authCookie && !user.value) {
    const { data, error } = await useFetch<IUser>(`${DJANGO_API_BASE}/user/me/`, {
      // headers: useRequestHeaders(["cookie"]),
      headers: {
        Authorization: `Token ${authCookie}`
      }
    });
    console.log("useAuth#useUser@data", data, error)
    user.value = data.value;
  }

  return user.value;
}

export async function userLogout() {
  const authCookie = useAuthCookie();
  await useFetch(`${DJANGO_API_BASE}/auth/token/logout/`, {
    headers: {
      Authorization: `Token ${authCookie.value}`
    },
    body: authCookie
  });
  authCookie.value = null
  useState("user").value = null;
  await useRouter().push("/");
}

export async function registerWithEmail(
  username: string,
  name: string,
  email: string,
  password: string
) {
  try {
    const { data, error } = await useFetch(`${DJANGO_API_BASE}/auth/register`, {
      method: "POST",
      body: { data: { username, name, email, password } },
    });

    if (error.value) {
      type ErrorData = {
        data: ErrorData;
      };

      const errorData = error.value as unknown as ErrorData;
      const errors = errorData.data.data as unknown as string;
      const res = JSON.parse(errors);
      const errorMap = new Map(Object.entries(res));

      return { hasErrors: true, errors: errorMap };
    }

    if (data) {
      useState("user").value = data;
      await useRouter().push("/dashboard");
    }
  } catch (e) {
    console.log("error: " + e.toString());
  }
}

export async function registerWithUsername(
  username: string,
  password: string
) {
  try {
    const { data, error } = await useFetch<IUser>(`${DJANGO_API_BASE}/auth/users/`, {
      method: "POST",
      body: { username, password },
    });

    console.log(`useAth#registerWithUsername@data`, data)

    if (error.value) {
      return { hasErrors: true, error: error.value };
    }

    if (data) {
      useState("user").value = data;
      await useRouter().push("/");
    }
  } catch (e) {
    console.log("error: " + e.toString());
  }
}

export async function loginWithEmail(email: string, password: string) {
  const user = await $fetch(`${DJANGO_API_BASE}/auth/login`, {
    method: "POST",
    body: { email: email, password: password },
  });
  useState("user").value = user;
  await useRouter().push("/dashboard");
}

export async function loginWithUsername(username: string, password: string) {
  let authCookie = useAuthCookie()
  const { auth_token } = await $fetch<LoginResponse>(
    `${DJANGO_API_BASE}/auth/token/login/`,
    {
      method: "POST",
      body: { username: username, password: password },
    }
  );
  authCookie.value = auth_token
  await useUser()
  await useRouter().push("/");
}
