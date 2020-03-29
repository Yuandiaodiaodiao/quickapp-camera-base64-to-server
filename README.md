快应用拍照转base64发送到服务端解码保存为图片文件

## 初始化
在index.ux里更改  
```html
 <input class="input" type="text" placeholder="serverPath" value="http://192.168.31.39:8888"
      onchange="inputChanged" />
    <input class="input" type="text" placeholder="photoPath" value="internal://cache/photo634114754637472416.jpg"
      onchange="inputChanged" />
```
两个input的value和你自己的serverip对应 photoPath是默认读取图片的路径 如果你懒得每次打开app都手动拍照   
server.py里面改监听端口  
## use  
1.npm install    
2.npm run watch    
3.npm run server    
4.python server.py    
点击 拍照->读文件->转换b64->发送服务器  


## python依赖
pip install tornado  
pip install base64  
