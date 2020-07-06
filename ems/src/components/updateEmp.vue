<template>

  <div id="content">
    <p id="whereami">
    </p>
    <h1>
      更新员工信息
    </h1>
    <form action="emplist.html" method="post">
      <table cellpadding="0" cellspacing="0" border="0"
             class="form_table">
        <tr>
          <td valign="middle" align="right">
            id:
          </td>
          <td valign="middle" align="left">
            {{$route.params.index}}
          </td>
        </tr>
        <tr>
          <td valign="middle" align="right">
            name:
          </td>
          <td valign="middle" align="left">
            <input type="text" class="inputgri" name="name" v-model="emp_name"/>
          </td>
        </tr>
        <tr>
          <td valign="middle" align="right">
            photo:
          </td>
          <td valign="middle" align="left">
            <input type="file" ref="photo"/>
          </td>
        </tr>
        <tr>
          <td valign="middle" align="right">
            salary:
          </td>
          <td valign="middle" align="left">
            <input type="text" class="inputgri" name="salary" v-model="salary"/>
          </td>
        </tr>
        <tr>
          <td valign="middle" align="right">
            age:
          </td>
          <td valign="middle" align="left">
            <input type="text" class="inputgri" v-model="age"/>
          </td>
        </tr>
      </table>
      <p>
        <el-button type="success" round @click="update_emp">提交</el-button>
      </p>
    </form>
  </div>

</template>

<script>
  export default {
    name: "updateEmp",
    data() {
      return {
        emp_name: "",
        salary: "",
        age: "",
        emp_name_2: "",
      }
    },
    methods: {
      get_emp() {
        let emp_url = "http://127.0.0.1:8000/api/emp/" + this.$route.params.id + "/"
        this.$axios({
          url: emp_url,
          method: "get",
        }).then(res => {
          let emp_info = res.data.results.employees
          this.emp_name = emp_info.emp_name
          this.emp_name_2 = emp_info.emp_name
          this.salary = emp_info.salary
          this.age = emp_info.age
        }).catch(error => {
          this.$message.error("出现错误，请刷新页面")
        })
      },
      update_emp() {
        let emp_url = "http://127.0.0.1:8000/api/emp/" + this.$route.params.id + "/"
        let formData = new FormData()
        if (this.emp_name !== this.emp_name_2) {
          formData.append("emp_name", this.emp_name)
        }
        let photo = this.$refs.photo.files[0]
        if (photo) {
          formData.append("photo", photo)
        }
        formData.append("salary", this.salary)
        formData.append("age", this.age)
        this.$axios({
          url: emp_url,
          method: "patch",
          data: formData,
          headers: {
            'content-type': 'multipart/form-data'
          },
        }).then(res => {
          console.log(res);
          this.$message.success("更新成功")
          this.$router.push('/emp')
        }).catch(error => {
          this.$message.error("更新失败，请查看信息是否符合条件")
        })
      },
    },
    created() {
      let admin_name = sessionStorage.admin_name
      if (!admin_name) {
        this.$message.error("您还没有登入,请登入")
        this.$router.push('/login')
      }
      this.get_emp()
    }
  }
</script>

<style scoped>

</style>
