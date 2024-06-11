// pages/index/index.js
Page({
  data: {
    ifLogin: '',
    accessList: [],
    name: "",
    stunum: "",
  },
  onShow() {
    let u = wx.getStorageSync("userinfo");
    if (u) {
      this.setData({
        ifLogin: u,
        name: u.realname,
        stunum: u.stunum,
      });
    }else {
      this.setData({
        ifLogin: '',
        accessList: [],
        name: "",
        stunum: "",
      })
      //不存在则showtoast，提示用户填写个人信息
      wx.showToast({
        title: "请填写个人信息",
        icon: "none",
        duration: 2000,
      });
    }
  },
  onLoad() {
    
    let info = wx.getStorageSync("userinfo");
    console.log(info);
    if (info) {
      this.setData({
        ifLogin: true,
        name: info.realname,
        stunum: info.stunum,
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
    this.refreshAccessList();
  },
  onPullDownRefresh() {
    this.refreshAccessList().then(() => {
      wx.stopPullDownRefresh(); // 结束下拉刷新
    });
  },
  formatTime(dateStr) {
    let date = new Date(dateStr);
    let year = date.getFullYear();
    let month = date.getMonth() + 1; // getMonth() 返回的月份从 0 开始
    let day = date.getDate();
    let hour = date.getHours();
    let minute = date.getMinutes();

    // 如果月、日、小时、分钟小于10，前面补0
    month = month < 10 ? "0" + month : month;
    day = day < 10 ? "0" + day : day;
    hour = hour < 10 ? "0" + hour : hour;
    minute = minute < 10 ? "0" + minute : minute;

    return `${year}-${month}-${day} ${hour}:${minute}`;
  },
  refreshAccessList() {
    return new Promise((resolve, reject) => {
      wx.request({
        url: `https://tocin.top:8443/api/get_face_data/${this.data.stunum}`,
        method: "GET",
        success: (res) => {
          console.log(res.data); // 打印服务器返回的数据

          // 将获取到的数据保存到页面的数据中
          this.setData({
            accessList: res.data.map((item) => ({
              studentId: item.face_id,
              name: item.face_name,
              time: this.formatTime(item.entry_time),
              accessInfo: item.entry_status,
            })),
          });
          this.setData({
            accessList: this.data.accessList.slice().reverse(),
          });
          resolve(); // 请求成功，解析 Promise
        },
        fail: (err) => {
          console.error(err);
          reject(); // 请求失败，拒绝 Promise
        },
      });
    });
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
