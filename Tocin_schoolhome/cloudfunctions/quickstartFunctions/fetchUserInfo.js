const cloud = require("wx-server-sdk");

cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
});

const db = cloud.database();
module.exports = async (event) => {
  let u = event.data; //取数据
  //检查用户是否存在
  let user = await db
    .collection("userinfo")
    .where({
      account: u.account,
    })
    .get();
  //判断是否存在用户信息
  if (user.data[0]) {
    let userInfo = user.data[0];
    return {
      success: true,
      msg: "获取用户信息成功",
      data: {
        nickname: userInfo.nickname,
        realname: userInfo.realname,
        gender: userInfo.gender,
        age: userInfo.age,
        phoneNumber: userInfo.phoneNumber,
        school: userInfo.school,
        classnum: userInfo.classnum,
        stunum: userInfo.stunum,
        region: userInfo.region,
        address: userInfo.address,
      },
    };
  }

  return {
    success: false,
    msg: "获取用户信息失败",
  };
};
