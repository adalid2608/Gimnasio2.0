<script setup>
  import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <RouterView />
  <Menu></Menu>
</template>

<script>
  import Menu from '@/components/Menu.vue'
</script>

<style lang="css">
  @import 'styles/menu.css';
</style>