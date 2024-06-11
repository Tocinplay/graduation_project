// pages/addnotice/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    class: '',
    author: '',
    content: ''
  },
  submit: function() {
    if (!this.data.class || !this.data.author || !this.data.content) {
      wx.showToast({
        title: '请填写所有字段',
        icon: 'none'
      });
      return;
    }

    wx.cloud.callFunction({
      name: 'quickstartFunctions',
      data: {
        type: 'addNotices',
        class: this.data.class,
        author: this.data.author,
        content: this.data.content
      },
    }).then((res) => {
        wx.showToast({
          title: '发布成功',
        });
        this.setData({
          class: '',
          author: '',
          content: ''
        });
    }).catch((err) => {
        console.error('[云函数] [addNotices] 调用失败', err)
        wx.showToast({
          icon: 'error',
          title: '[云函数] [addNotices] 调用失败',
        })
    });
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {

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