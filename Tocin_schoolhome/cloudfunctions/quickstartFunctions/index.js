const getOpenId = require('./getOpenId/index');
const getNotices = require('./getNotices/index');
const addNotices = require('./addNotices/index');
const loginWithMp = require('./loginWithMp');
const login = require('./login');
const register = require('./register');
const fetchUserInfo = require('./fetchUserInfo');
const addUserInfo = require('./addUserInfo');
// 云函数入口函数
exports.main = async (event, context) => {
  switch (event.type) {
    case "getOpenId":
      return await getOpenId.main(event, context);
    case "getNotices":
      return await getNotices(event, context);
    case "addNotices":
      return await addNotices(event, context);
    case "loginWithMp":
      return await loginWithMp(event, context);
    case "login":
      return await login(event, context);
    case "register":
      return await register(event, context);
    case "fetchUserInfo":
        return await fetchUserInfo(event, context);
    case "addUserInfo":
          return await addUserInfo(event, context);
    default:
      return {
        success: false,
        errorMessage: "没有对应的函数名",
      };
  }
};
        
