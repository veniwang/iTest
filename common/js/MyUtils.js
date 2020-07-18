function GetHtmlQueryString(name){
     var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
     var r = window.location.search.substr(1).match(reg);
     if(r!=null)return  unescape(r[2]); return null;
}

function isValidMail(str){
    var myreg = /(\S)+[@]{1}(\S)+[.]{1}(\w)+/;
    if (str.length == 0){
        return false;
    }else{
        if(!myreg.test(str)){
            return false;
        }
    }
    return true;
}