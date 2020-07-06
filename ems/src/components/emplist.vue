<template>

  <div id="content">
    <p id="whereami">
    </p>
    <h1>
      欢迎 {{admin_name}} 登入员工管理系统
    </h1>
    <table class="table">
      <tr class="table_header">
        <td>ID</td>
        <td>Name</td>
        <td>Photo</td>
        <td>Salary</td>
        <td>Age</td>
        <td>Operation</td>
      </tr>
      <tr v-for="(emp,index) in emp_list" :key="emp.id" :class="index%2===0?'row1':'row2'">
        <td>{{index+1}}</td>
        <td>{{emp.emp_name}}</td>
        <td><img :src="emp.photo" style="height: 60px;"></td>
        <td>{{emp.salary}}</td>
        <td>{{emp.age}}</td>
        <td>
          <el-link type="success" @click="delete_emp(emp.id)">删除员工</el-link>
          &nbsp;

          <el-link type="success" @click="update_emp(emp.id,index)">更新员工信息</el-link>

        </td>
      </tr>
    </table>
    <p>
      <router-link to="/add">
        <el-button type="success" round>增加员工</el-button>
      </router-link>

      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <el-link type="warning" @click="quit_ems">退出登入</el-link>
    </p>
  </div>

</template>

<script>
  export default {
    name: "emplist",
    data() {
      return {
        admin_name: "",
        emp_list: []
      }
    },
    methods: {
      quit_ems() {
        sessionStorage.removeItem('admin_name')
        this.$router.push('/login')
      },
      delete_emp(emp_id) {
        let emp_url = "http://127.0.0.1:8000/api/emp/" + emp_id + "/"
        this.$axios({
          url: emp_url,
          method: "delete",
        }).then(res => {
          this.$message.success("删除成功")
          this.$router.go(0)
          // console.log(this.emp_list);
        }).catch(error => {
          this.$message.error("删除失败，请重新删除")
        })
      },
      update_emp(emp_id, index) {
        index += 1
        let url = "/update/" + emp_id + "/" + index
        this.$router.push(url)
      },
      get_emp_list() {
        this.$axios({
          url: "http://127.0.0.1:8000/api/emp/",
          method: "get",
        }).then(res => {
          this.emp_list = res.data.results.employees
          console.log(this.emp_list);
        }).catch(error => {
          this.$message.error("出现错误，请刷新页面")
        })
      }
    }
    ,
    created() {
      let admin_name = sessionStorage.admin_name
      if (admin_name) {
        this.admin_name = admin_name
        this.get_emp_list()
      } else {
        this.$message.error("您还没有登入,请登入")
        this.$router.push('/login')
      }
    }
  }
</script>

<style scoped>

</style>
