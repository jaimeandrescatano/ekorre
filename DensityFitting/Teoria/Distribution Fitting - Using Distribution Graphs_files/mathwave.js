<!--
function showPopupImg (url, width, height) 
{
  var w = width + 22;
  var h = height + 32;
  var l = (screen.width - w) / 2;
  var t = (screen.height - h) / 2 - 40;
  window.open(url, 'view', 'width='+w+', height='+h+', left='+l+', top='+t+', scrollbars=no, status=no, resizable=yes, location=no').focus();
  return false;
}

function showPopupPage (url, width, height) 
{
  var w = width + 22;
  var h = height + 32;
  var l = (screen.width - w) / 2;
  var t = (screen.height - h) / 2 - 40;
  window.open(url, 'text_'+width+'x'+height, 'width='+w+', height='+h+', left='+l+', top='+t+', scrollbars=yes, status=no, resizable=yes, location=no').focus();
  return false;
}

startList = function() {
  var navNodes = new Array('menu-header');
  count = 0;
  if(document.all && document.getElementById) {
    for(z=0;z < navNodes.length;z++)
    {
      var arrNodes = new Array();
      arrNodes[0] = document.getElementById(navNodes[z]);
      for(i=0;i < arrNodes.length; i++)
      {     
        try 
        {        
          for(j=0;j < arrNodes[i].childNodes.length; j++)
          {
            node = arrNodes[i].childNodes[j];
            if(node.nodeName == "LI") 
            {
              node.onmouseover=function() 
              {          
                this.className+="Over";
              }
              node.onmouseout=function() 
              {
                this.className=this.className.replace("Over", "");
              }  
              count++;
            }
            arrNodes[arrNodes.length] = node;
          }
        }
        catch(e) 
        {
        }
      }
    }
  }
}

window.onload=startList;
//-->
