<template>
  <!-- <router-view></router-view> -->

  <the-nav/>
  <the-search/>


</template>

<script>
import TheNav from './components/nav/navigation.vue'
import TheSearch from './components/mainBody/search.vue'




export default {
  components : {
    TheNav,
    TheSearch,

  }
}
</script>

<style>
*{
  margin: 0;
  padding: 0;
}
</style>