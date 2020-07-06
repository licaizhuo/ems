<template>

  <div id="content">
    <p id="whereami">
    </p>
    <h1>
      注册
    </h1>
    <table cellpadding="0" cellspacing="0" border="0"
           class="form_table">
      <tr>
        <td valign="middle" align="right">
          用户名:
        </td>
        <td valign="middle" align="left">
          <input type="text" class="inputgri" v-model="username"/>
        </td>
      </tr>
      <tr>
        <td valign="middle" align="right">
          真实姓名:
        </td>
        <td valign="middle" align="left">
          <input type="text" class="inputgri" v-model="real_name"/>
        </td>
      </tr>
      <tr>
        <td valign="middle" align="right">
          密码:
        </td>
        <td valign="middle" align="left">
          <input type="password" class="inputgri" v-model="password"/>
        </td>
      </tr>
      <tr>
        <td valign="middle" align="right">
          确认密码:
        </td>
        <td valign="middle" align="left">
          <input type="password" class="inputgri" v-model="con_password"/>
        </td>
      </tr>
      <tr>
        <td valign="middle" align="right">
          性别:
        </td>
        <td valign="middle" align="left">
          <input type="radio" class="inputgri" name="sex" value="m" @click="gender=0" checked/>
          男
          <input type="radio" class="inputgri" name="sex" @click="gender=1"/>
          女
        </td>
      </tr>

    </table>
    <p>
      <el-button type="success" round @click="add_user">注册</el-button>
    </p>
  </div>

</template>

<script>
  export default {
    name: "register",
    data() {
      return {
        username: "",
        real_name: "",
        password: "",
        con_password: "",
        gender: 0,
      }
    },
    methods: {
      add_user() {
        this.$axios({
          url: "http://127.0.0.1:8000/user/rt/",
          method: "post",
          data: {
            username: this.username,
            real_name: this.real_name,
            password: this.password,
            con_password: this.con_password,
            gender: this.gender,
          }
        }).then(res => {
          this.$message.success("注册成功，跳转到登入页面")
          this.$router.push("/login")
        }).catch(error => {
          let error_data = error.response.data
          let error_info =""
          // console.log(error_data);
          if (error_data[0]) {
            error_info = error_data[0]
          } else {
            let error_key = Object.keys(error_data)[0]
            error_info = error_data[error_key][0].slice(1)
          }

          this.$message.error("注册失败,请仔细填写信息,注意" + error_info)
        })
      }
    }
  }
</script>

<style scoped>

</style>
