// pages/userinfo/index.js
Page({
  data: {
    nickname: "", //昵称
    realname: "", // 姓名
    genderArray: ["男", "女"], // 性别选项
    genderIndex: 0, // 默认选中男
    age: "", // 年龄
    phoneNumber: "", // 电话号码
    school: "", // 学校
    classnum: "", // 班级
    stunum: "",
    region: ["湖南省", "益阳市", "赫山区"], //详细地址
    address: "", // 家庭住址
    account: wx.getStorageSync("token").account,
  },
  // 输入昵称
  inputNickName: function (e) {
    console.log(e.detail.value);
    this.setData({
      nickname: e.detail.value,
    });
    return;
  },
  // 输入姓名
  inputRealName: function (e) {
    console.log(e.detail.value);
    this.setData({
      realname: e.detail.value,
    });
    return;
  },
  // 选择性别
  genderChange: function (e) {
    console.log(e.detail.value);
    this.setData({
      genderIndex: e.detail.value,
    });
    return;
  },
  // 输入年龄
  inputAge: function (e) {
    this.setData({
      age: e.detail.value,
    });
    return;
  },
  // 输入电话号码
  inputPhone: function (e) {
    this.setData({
      phoneNumber: e.detail.value,
    });
    return;
  },
  // 输入学校
  inputSchool: function (e) {
    this.setData({
      school: e.detail.value,
    });
    return;
  },
  // 输入班级
  inputClass: function (e) {
    this.setData({
      classnum: e.detail.value,
    });
    return;
  },
  // 输入学号
  inputStunum: function (e) {
    this.setData({
      stunum: e.detail.value,
    });
    return;
  },
  regionChange: function (e) {
    console.log("picker发送选择改变，携带值为", e.detail.value);
    this.setData({
      region: e.detail.value,
    });
    return;
  },
  // 输入家庭住址
  inputAddress: function (e) {
    this.setData({
      address: e.detail.value,
    });
    return;
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    
  },
  submit: function (e) {
    //判断信息符合条件
    if (this.data.nickname == "") {
      wx.showToast({
        title: "昵称不能为空",
        icon: "none",
        duration: 1000,
      });
      return;
    }
    if (this.data.realname == "") {
      wx.showToast({
        title: "姓名不能为空",
        icon: "none",
        duration: 1000,
      });
      return;
    }
    if (this.data.age == "") {
      wx.showToast({
        title: "年龄不能为空",
        icon: "none",
        duration: 1000,
      });
      return;
    }
    //判断电话号码长度为11位数字，不能为空
    if (
      this.data.phoneNumber == "" ||
      this.data.phoneNumber.length != 11 ||
      isNaN(this.data.phoneNumber)
    ) {
      wx.showToast({
        title: "电话号码不合法",
        icon: "none",
        duration: 1000,
      });
      return;
    }
    if (this.data.school == "") {
      wx.showToast({
        title: "学校不能为空",
        icon: "none",
        duration: 1000,
      });
      return;
    }
    if (this.data.classnum == "") {
      wx.showToast({
        title: "班级不能为空",
        icon: "none",
        duration: 1000,
      });
      return;
    }

    //添加信息到后面
    wx.cloud
      .callFunction({
        name: "quickstartFunctions",
        data: {
          type: "addUserInfo",
          data: {
            nickname: this.data.nickname,
            realname: this.data.realname,
            gender: this.data.genderArray[this.data.genderIndex],
            age: this.data.age,
            phoneNumber: this.data.phoneNumber,
            school: this.data.school,
            classnum: this.data.classnum,
            stunum: this.data.stunum,
            region: this.data.region,
            address: this.data.address,
            account: this.data.account,
          },
        },
      })
      .then((res) => {
        //成功添加学生信息
        console.log(res);
        if (res.result.success) {
          console.log("添加信息成功");

          wx.showToast({
            title: res.result.msg,
          });
        } else {
          console.error("添加信息失败: ", res.result.msg);
          wx.showToast({
            icon: "error",
            title: res.result.msg,
          });
        }
      })
      .catch((err) => {
        console.error("[云函数] [addUserInfo] 调用失败", err);
      });
    return;
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {
    this.account = wx.getStorageSync("token").account;
    console.log(this.account)
    let u = wx.getStorageSync("userinfo");
    console.log(u);
    //如果有用户信息则显示
    if (u) {
      this.setData({
        nickname: u.nickname,
        realname: u.realname,
        genderIndex: u.gender === '男' ? 0 : 1,
        age: u.age,
        phoneNumber: u.phoneNumber,
        school: u.school,
        classnum: u.classnum,
        stunum: u.stunum,
        region: u.region,
        address: u.address,
      });
    }
  },
});
