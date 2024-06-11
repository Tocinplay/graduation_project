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
  //判断是否存在用户信息，
  if (user.data[0]) {
    //存在则修改信息
    await db
      .collection("userinfo")
      .doc(user.data[0]._id)
      .update({
        data: {
          nickname: u.nickname,
          realname: u.realname,
          gender: u.gender,
          age: u.age,
          phoneNumber: u.phoneNumber,
          school: u.school,
          classnum: u.classnum,
          stunum: u.stunum,
          region: u.region,
          address: u.address,
          account: u.account,
        },
      });
    return {
      success: true,
      msg: "修改信息成功",
    };
  } else {
    //不存在则添加信息
    await db.collection("userinfo").add({
      data: {
        nickname: u.nickname,
        realname: u.realname,
        gender: u.gender,
        age: u.age,
        phoneNumber: u.phoneNumber,
        school: u.school,
        classnum: u.classnum,
        stunum: u.stunum,
        region: u.region,
        address: u.address,
        account: u.account,
      },
    });
    return {
      success: true,
      msg: "提交信息成功",
    };
  }
  
};
