// login.js

//const app = getApp(); // 获取小程序实例

Page({
  data: {
    showPassword: false, // 是否显示密码
    account: '', // 账号
    password: '', // 密码
  },

  // 监听账号输入框的输入事件
  handleAccountInput(event) {
    this.setData({
      account: event.detail.value,
    });
  },

  // 监听密码输入框的输入事件
  handlePasswordInput(event) {
    this.setData({
      password: event.detail.value,
    });
  },

  // 点击显示密码选项
  handleShowPassword() {
    this.setData({
      showPassword: !this.data.showPassword,
    });
  },

  // 点击注册按钮
  register() {
    wx.navigateTo({
      url: '/pages/register/index',
    });
  },
  // 点击登录按钮
  login() {
    const { account, password } = this.data;

    // 执行登录逻辑，例如调用云函数进行登录验证
    // 请根据实际情况进行修改
    wx.cloud.callFunction({
      name: "quickstartFunctions",
      data: {
        type: "login",
        data: {
          account,
          password,
        }
      },  
    })
    .then((res)=>{
      if(res.result.success){
        // 登录成功
        console.log('登录成功', res);
        //如果没有用户信息则跳转到用户信息界面
        let token = res.result.data;
        wx.setStorageSync('token', token);
        wx.navigateTo({
          url: '/pages/userinfo/index', // 替换为实际的主界面路径
        });

        //获取用户信息
        wx.cloud.callFunction({
          name: "quickstartFunctions",
          data: {
            type: "fetchUserInfo",
            data: {
              account,
            }
          },
        }).then((res)=>{
          //获取成功跳转主页
          if(res.result.success){
            //存储用户信息
            wx.setStorageSync('userinfo', res.result.data)
            wx.switchTab({
              url: '/pages/index/index',
            }) 
          }
          else{
            //未获取到则切换到用户信息目录
            wx.navigateTo({
              url: '/pages/userinfo/index', // 替换为实际的主界面路径
            });
          }
        })
      }
      else{
        // 登录失败
        console.error('登录失败', res.result.msg);
        wx.showToast({
          icon: "error",
          title: res.result.msg,
        })
      }
    },(err) => {
      // 登录失败
      console.error('注册失败', err);
    });
    return;
  },
  onload() {
    // let token = uni.getStorageSync('token');
    // if(!token){
      
    // }
  }
});