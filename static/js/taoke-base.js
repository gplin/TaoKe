/*!
  @name taoke-base.js
  @author gplin
  @version 1.0.0
  @date 2013-10-20
*/
function stripTrailingSlash(str){
    if(str.substr(-1)=='/'){
        return str.substr(0,str.length-1);
    }
    return str;
}

// $(".footer ul li").popover({
//     placement:'top',
//     content:'bashishang.com',
//     trigger:'hover'
// });
$(".u_s_icon_32 img").grumble({
    text:'Bull-testic',
    angle:85,
    distance:100,
    showAfter:500
});