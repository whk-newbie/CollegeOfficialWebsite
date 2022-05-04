<template>
  <Graduate/>
</template>

<script>
import Graduate from '@/views/education/Graduate'

export default {
  name: "Undergraduate",
  components: {Graduate},
  data() {
    return {
      activeIndex: this.$route.path,
      isCollapse: false
    }
  },
}
</script>

<style scoped>
.body {
  margin: 2% 2% 2% 10%;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}
</style>
