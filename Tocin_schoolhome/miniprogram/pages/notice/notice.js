// pages/notice.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    notices:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    this.getNotices()
    
  },

  getNotices: function(){
    wx.cloud.callFunction({
      name: 'quickstartFunctions',
      data: {
        type: 'getNotices',
      },
    }).then((res) => {
      //成功获取数据
        console.log(res)
        if (res.result.success) {
          let notices = res.result.data;
          notices.forEach(notice => {
            let date = new Date(notice.time);
            notice.time = `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()} ${date.getHours()}:${date.getMinutes()}`;
          });
          notices.reverse();
          this.setData({
            notices: notices
          });
        } else {
          console.error('获取通知失败: ', res.result.errorMessage)
        }
    }).catch((err) => {
      console.error('[云函数] [getNotices] 调用失败', err)
  });
  },
  edit: function() {
    //跳转到编辑页面
    wx.navigateTo({
      url: '/pages/addnotice/index'
    });
  },

  refresh: function() {
    this.getNotices();
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})