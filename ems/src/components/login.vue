<template>

  <div id="content">
    <p id="whereami">
    </p>
    <h1>
      login
    </h1>
    <table cellpadding="0" cellspacing="0" border="0"
           class="form_table">
      <tr>
        <td valign="middle" align="right">
          username:
        </td>
        <td valign="middle" align="left">
          <input type="text" class="inputgri" v-model="username"/>
        </td>
      </tr>
      <tr>
        <td valign="middle" align="right">
          password:
        </td>
        <td valign="middle" align="left">
          <input type="password" class="inputgri" v-model="password"/>
        </td>
      </tr>
    </table>
    <p>
      <el-button type="success" round @click="login_ems">登入</el-button>
      &nbsp;&nbsp;
      <router-link to="/register">去注册</router-link>
    </p>
  </div>

</template>

<script>
  export default {
    name: "login",
    data() {
      return {
        username: "",
        password: "",
      }
    },
    methods: {
      login_ems() {
        this.$axios({
          url: "http://127.0.0.1:8000/user/rt/",
          method: "get",
          params: {
            username: this.username,
            password: this.password,
          }
        }).then(res => {
          this.$message.success("登入成功,跳转到员工列表页面")
          sessionStorage['admin_name'] = this.username
          this.$router.push("/emp")
        }).catch(error => {
          this.$message.error("登入失败，请仔细检查登入信息")
        })
      }
    },
    created() {
      if (sessionStorage.admin_name) {
        this.$router.push("/emp")
      }
    }
  }
</script>

<style scoped>

</style>
