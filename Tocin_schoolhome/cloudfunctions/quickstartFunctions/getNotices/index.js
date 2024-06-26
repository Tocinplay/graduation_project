const cloud = require("wx-server-sdk");

cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
});

const db = cloud.database();
//const _ = db.command;
module.exports = async (event) => {
  try {
    //let wxContext = cloud.getWXContext();
    //let openId = wxContext.OPENID || "test";
    let res = await db
      .collection("notices").get();
    return {
      success: true,
      data: res.data,
    };
  } catch (error) {
    return {
      success: false,
      errorMessage: error,
    };
  }
};