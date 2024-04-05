<script setup lang="ts">
import { useRoute } from "vue-router";
import { computed } from "vue";
import { PortalTarget } from "portal-vue";

const props = defineProps<{
  nav?: Array<{link: string, label: string}>
  withTitle?: boolean
  isUserHeader?: boolean
}>()

const logoLink = computed(() => props.isUserHeader ? '/list' : '/editor/home')

const route = useRoute();
</script>

<template>
  <header
      :class="['header', {['header--user']: isUserHeader}]"
  >
    <router-link
        :to="logoLink"
        class="header__logo"
    >
      <v-img
          :width="128"
          :height="72"
          alt="logo"
          cover
          src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
      ></v-img>
    </router-link>
    <div
        v-if="withTitle"
        class="header__route-name"
    >
      {{ route.name }}
    </div>
    <nav
        v-if="nav?.length"
        class="header__nav"
    >
      <router-link
          v-for="(navItem, index) in nav"
          :key="index"
          :to="navItem.link"
          class="header__link"
      >
        {{ navItem.label }}
      </router-link>
    </nav>
    <router-link
        v-if="!isUserHeader"
        to="/editor/profile"
        class="header__profile"
    >
      <v-avatar
          color="grey-lighten-3"
          size="72"
          class="header__avatar"
          icon="mdi-account"
      >
      </v-avatar>
    </router-link>
    <div
        v-else
        class="header__controls"
    >
      <portal-target
          name="header-portal"
      >
      </portal-target>
    </div>
  </header>
</template>

<style lang="scss" scoped>
  .header {
    display: grid;
    grid-template-columns: 128px 1fr 128px;
    gap: 32px;
    padding: 24px 80px;
    background: white;

    &--user {
      grid-template-columns: 36px 500px 1fr;
      gap: 12px;
      padding: 14px;
      align-items: center;

      .header__logo {
        width: 36px;
        height: 36px;
      }
    }

    &__profile {
      display: flex;
      grid-column: 3 / 4;
    }

    &__avatar {
      margin-left: auto;
    }

    &__link {
      font-size: 24px;
      color: #000;
      text-decoration: none;

      &:hover {
        opacity: .7;
      }
    }

    &__nav {
      display: flex;
      flex-wrap: wrap;
      gap: 128px;
      align-items: center;
      justify-content: center;
    }

    &__route-name {
      font-size: 32px;
      font-weight: 700;
      color: #333;
    }

    &__controls {
      display: flex;
      justify-content: flex-end;
    }
  }
</style>
