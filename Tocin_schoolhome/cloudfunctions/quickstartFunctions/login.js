const cloud = require("wx-server-sdk");

cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
});

const db = cloud.database();
module.exports = async (event) => {
  let u = event.data;//取数据
  //检查用户是否存在
  let user = await db.collection("user").where({
    account: u.account,
  }).get();
  //判断账号密码是否一致
  if(user.data[0] && user.data[0].account === u.account && user.data[0].password === u.password){
    return {
      success: true,
      data: user.data[0]
    };
  }
  
  return {
    success: false,
    msg: "登录失败"
  };
}