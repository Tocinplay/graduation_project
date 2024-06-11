// register.js

Page({
  data: {
    account: '', // 账号
    password: '', // 密码
    passwordagain: ''
  },

  // 监听账号输入框的输入事件
  handleAccountInput(event) {
    this.setData({
      account: event.detail.value,
    });
  },

  // 监听密码输入框的输入事件
  handlePasswordInput(event) {
   // console.log( event.detail.value),
    this.setData({
      password: event.detail.value,
    });
  },
  handlePasswordAgainInput(event) {
    //console.log( event.detail.value),
    this.setData({
      passwordagain: event.detail.value,
    });
  },

  // 点击登录按钮
  register() {
    if(!this.data.account){
      wx.showToast({
        icon: 'error',
        title: '请输入账号',
      })
      return;
    }
    if(this.data.password != this.data.passwordagain){
      wx.showToast({
        icon:"error",
        title: '两次密码不一致',
      })
      return;
    }

    const { account, password } = this.data;

    // 执行登录逻辑，例如调用云函数进行登录验证
    // 请根据实际情况进行修改
    wx.cloud.callFunction({
      name: "quickstartFunctions",
      data: {
        type: "register",
        data: {
          account,
          password,
        }
      },
      
    })
    .then((res) => {
        // 登录成功
        if(res.result.success){
        console.log('注册成功', res);
        wx.showToast({
          title: res.result.msg,
        });
        
        // 跳转到主界面
        setTimeout(function(){
            wx.switchTab({
            url: '/pages/index/index', // 替换为实际的主界面路径
          });
      },1500);
        
      }
      else {
        console.log('注册失败', res);
        wx.showToast({
          icon: "error",
          title: res.result.msg,
        });
      }
        
        
      },
      (err) => {
        // 登录失败
        console.error('注册失败', err);
      });
    return;
  },
});