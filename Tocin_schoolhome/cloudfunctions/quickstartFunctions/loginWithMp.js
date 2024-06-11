let jwt = require('jsonwebtoken');
const cloud = require('wx-server-sdk');
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV
});
const db = cloud.database();

let appid = 'wx706f7181db3314d8';//小程序id
let appsecret = '70ba576a9e0add02f6af4e7037c6fc8e';//小程序密钥
let jwtSecret = 'tomix007';//jwt密钥

exports.main = async (event, context) => {
  let code = event.code;
  let url = `https://api.weixin.qq.com/sns/jscode2session?appid=${appid}&secret=${appsecret}&js_code=${code}&grant_type=authorization_code`;
  let response = await request(
    url,
    {dataType: 'json'}
  );
  let data = await response.json();
  let openId = data.openid;
  if(!openId){
    throw Error("获取openId失败");
  }
  let user  = await db.collection('users').doc(openId).get();
  let token = 'Bearer '+jwt.sign({openId}, jwtSecret);
  if(user.data[0]){
    return {
        user: user.data[0],
        token: token,
    };
  }else{
    let data = {
      _id: openId,
      createTime: Date().now(),
    };
    await db.collection('users').add(data);
    return {
        user: data,
        token: token,
    };
  }
    // if (!event.token){
    //     throw Error("未登录");
    // }
    // let auth = jwt.verify(event.token.replace('Bearer ', ''), jwtSecret);
    // let openId = auth.openId;
}