// main.js

Page({
  data: {
    userInfo: '',
    studentName: '',
    studentId: '',
  },
  onLoad() {
    let info = wx.getStorageSync("userinfo");
    console.log(info);
    if (info) {
      this.setData({
        userInfo: info,
        studentName: info.realname,
        studentId: info.stunum,
      });
      console.log(this.data.stunum);
    } else {
      //不存在则showtoast，提示用户填写个人信息
      wx.showToast({
        title: "请填写个人信息",
        icon: "none",
        duration: 2000,
      });
    }
  },
  onShow(){
    let info = wx.getStorageSync("userinfo");
    console.log(info);
    if (info) {
      this.setData({
        userInfo: info,
        studentName: info.realname,
        studentId: info.stunum,
      });
      console.log(this.data.stunum);
    } else {
      //不存在则showtoast，提示用户填写个人信息
      wx.showToast({
        title: "请填写个人信息",
        icon: "none",
        duration: 2000,
      });
    }
  },

  btn_wxlogin() {
    wx.getUserProfile({
      desc: '授权获取微信头像昵称',
      success: res => {
        console.log(res);
        let user = res.userInfo;
        wx.setStorageSync('user', user);
        this.setData({
          userInfo: user
        });
      },
      fail: res => {
        console.log("授权失败", res)
      }
    })
  },
  userinfo() {
    wx.navigateTo({
      url: '/pages/userinfo/index',
    })
  },
  btn_loginout() {
    this.setData({
      userInfo: ''
    })
    wx.setStorageSync('userinfo', null)
    wx.setStorageSync('token', null)
  },
  login: function () {
    //跳转到编辑页面
    wx.navigateTo({
      url: "/pages/login/index",
    });
  },
  register: function () {
    //跳转到编辑页面
    wx.navigateTo({
      url: "/pages/register/index",
    });
  },
});