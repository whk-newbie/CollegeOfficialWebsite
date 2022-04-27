<template>
<div class="footer">
  <div class="img">
    <div class="imgs">
    </div>
  </div>
  <div class="foot-left" >
    <a>校内链接：</a><a href="http://www.jxnu.edu.cn/" target="_blank">江西师范大学</a>
    <a href="http://jwc.jxnu.edu.cn/" target="_blank">师大教务在线</a>
    <a href="http://rsc.jxnu.edu.cn/" target="_blank">江西师大人事网</a>
    <p class="copyright"><span>Copyright©2021 江西师范大学计算机信息工程学院； 地址：江西省南昌市紫阳大道99号； 电话：0791-88120416， 88120411；邮编：330022</span></p>
    <p class="copyright"><span>技术支持：whk</span></p>
  </div>
</div>
</template>

<script>
export default {
name: "foot"
}
</script>

<style scoped>
.footer {
  margin: 0;
  border: 0;
  padding: 0;
}
.img {
  width: 100%;
  height: auto;
  background: url("https://jsjxy.jxnu.edu.cn/_upload/tpl/00/d8/216/template216/images/under1.jpg");
  background-size: cover;
}
.imgs {
  padding: 80px 50px;
}
.foot-left{
  position: relative;
  text-align: center;
}
.foot-left a{
  text-decoration: none;
  color: black;
}

</style>
