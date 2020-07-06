<template>

  <div id="content">
    <p id="whereami">
    </p>
    <h1>
      增加员工
    </h1>
    <table cellpadding="0" cellspacing="0" border="0"
           class="form_table">
      <tr>
        <td valign="middle" align="right">
          name:
        </td>
        <td valign="middle" align="left">
          <input type="text" class="inputgri" v-model="emp_name"/>
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
          <input type="number" class="inputgri" v-model="salary"/>
        </td>
      </tr>
      <tr>
        <td valign="middle" align="right">
          age:
        </td>
        <td valign="middle" align="left">
          <input type="number" class="inputgri" v-model="age"/>
        </td>
      </tr>
    </table>
    <p>
      <el-button type="success" round @click="add_emp">提交</el-button>
    </p>
  </div>

</template>

<script>
  export default {
    name: "addEmp",
    data() {
      return {
        emp_name: "",
        salary: "",
        age: "",

      }
    },
    methods: {
      add_emp() {
        let formData = new FormData()
        formData.append("emp_name", this.emp_name)
        formData.append("photo", this.$refs.photo.files[0])
        formData.append("salary", this.salary)
        formData.append("age", this.age)
        this.$axios({
          url: "http://127.0.0.1:8000/api/emp/",
          method: "post",
          data: formData,
          headers: {
            'content-type': 'multipart/form-data'
          },
        }).then(res => {
          console.log(res);
          this.$message.success("添加成功")
          this.$router.push('/emp')
        }).catch(error => {
          let error_data = error.response.data
          let error_info = ""
          if (error_data[0]) {
            error_info = error_data[0]
          } else {
            let error_key = Object.keys(error_data)[0]
            error_info = error_data[error_key][0].slice(1)
          }
          this.$message.error(error_info)
        })
      }
    },

    created() {
      let admin_name = sessionStorage.admin_name
      if (!admin_name) {
        this.$message.error("您还没有登入,请登入")
        this.$router.push('/login')
      }

    }
  }
</script>

<style scoped>

</style>
