const cloud = require("wx-server-sdk");

cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
});

const db = cloud.database();
module.exports = async (event) => {
  let u = event.data; //取数据
  console.log(u);
  //检查用户是否存在
  let user = await db.collection("user").where({
    account: u.account,
  }).get();
  if (user.data.length > 0) {
    return {
      success: false,
      msg: "用户已存在",
    };
  }
  //用户ID从微信之中直接获取
  let wxContent = cloud.getWXContext();
  let openId = wxContent.OPENID;
  //用户ID递增
  let res = await db.collection("user").count();
  let userId = parseInt(res.total) + 1;

  await db.collection("user").add({
    data: {
      userId,
      openId,
      account: u.account,
      password: u.password,
      admin: false,
    },
  });
  return {
    success: true,
    msg: "注册成功"
  };
}