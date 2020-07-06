<template>
  <div id="app">
    <div id="wrap">
      <div id="top_content">
        <div id="header">
          <div id="rightheader">
            <p>
              {{now_date}}
              <br/>
            </p>
          </div>
          <div id="topheader">
            <h1 id="title">
              <a href="#">main</a>
            </h1>
          </div>
          <div id="navigation">
          </div>
        </div>
        <router-view></router-view>
      </div>
      <div id="footer">
        <div id="footer_bg">
          ABC@126.com
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        now_date: "2020/7/4",
      }
    },
    created() {
      let now_date = new Date()
      let year = now_date.getFullYear()
      let month = now_date.getMonth() + 1
      let day = now_date.getDate()
      this.now_date = year + "/" + month + "/" + day
      // console.log(this.now_date)
    }
  }
</script>

<style>

</style>
