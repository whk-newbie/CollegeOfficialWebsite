<template>
  <Header/>
  <Homebody/>
  <Footer/>
</template>

<script>
import Header from "@/components/Header";
import Homebody from "@/components/Homebody";
import Footer from "@/components/Footer";
export default {
  name: "Home",
  components: { Header,Homebody,Footer}
}
</script>

<style scoped>

</style>
