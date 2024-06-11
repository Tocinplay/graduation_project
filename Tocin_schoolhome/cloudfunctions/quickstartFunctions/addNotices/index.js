const cloud = require("wx-server-sdk");

cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV,
});

const db = cloud.database();
module.exports = async (event) => {
  try {
    let date = new Date()
    // let createTime = date()
    let res = await db
      .collection("notices").add({
        data: {
          class: event.class,
          author: event.author,
          content: event.content,
          time: date,
        },
      });
    return {
      success: true,
      data: result._id,
    };
  } catch (error) {
    return {
      success: false,
      errorMessage: error,
    };
  }
};
