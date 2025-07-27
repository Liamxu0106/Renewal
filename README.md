# Climate Change Chat Assistant

一个基于气候变化框架的AI聊天助手，支持经济、公共卫生、道德伦理和不平等等多个视角的对话。

## 功能特点

- 🤖 **AI对话**: 基于OpenAI GPT-3.5-turbo的智能对话
- 🎯 **框架识别**: 自动识别用户选择的讨论框架
- 📱 **响应式设计**: 适配手机和桌面设备
- 💬 **格式化显示**: 支持加粗文本和换行
- 🌍 **多视角**: 支持经济、公共卫生、道德伦理、不平等四个框架

## 项目结构

```
climate-chat-app/
├── app.py                 # FastAPI后端
├── requirements.txt       # Python依赖
├── index.html            # 前端页面
├── README.md             # 项目说明
└── .gitignore           # Git忽略文件
```

## 部署步骤

### 第一步：准备GitHub仓库

1. **创建新仓库**
   - 登录GitHub
   - 点击"New repository"
   - 仓库名称：`climate-chat-app`
   - 选择"Public"
   - 不要初始化README（我们会手动添加）

2. **上传文件**
   - 将以下文件上传到仓库：
     - `app.py`
     - `requirements.txt`
     - `index.html`
     - `README.md`

### 第二步：部署后端到Render

1. **登录Render**
   - 访问 https://render.com
   - 使用GitHub账号登录

2. **创建Web Service**
   - 点击"New" → "Web Service"
   - 连接您的GitHub仓库

3. **配置设置**
   ```
   Name: climate-chat-api
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn app:app --host 0.0.0.0 --port $PORT
   Plan: Free
   ```

4. **添加环境变量**
   - 在"Environment"部分添加：
   ```
   Key: OPENAI_API_KEY
   Value: 您的OpenAI API密钥
   ```

5. **部署**
   - 点击"Create Web Service"
   - 等待部署完成（约5-10分钟）

6. **获取API URL**
   - 部署成功后，复制提供的URL
   - 格式：`https://your-app-name.onrender.com`

### 第三步：更新前端API地址

1. **编辑index.html**
   - 找到第47行：`const API_URL = "https://your-render-app-name.onrender.com/chat";`
   - 将`your-render-app-name`替换为您的实际Render应用名称

2. **示例**：
   ```javascript
   const API_URL = "https://climate-chat-api.onrender.com/chat";
   ```

### 第四步：部署前端到GitHub Pages

1. **创建GitHub Pages仓库**
   - 创建新仓库：`your-username.github.io`
   - 或者使用现有仓库的Pages功能

2. **上传前端文件**
   - 将更新后的`index.html`上传到仓库
   - 确保文件名为`index.html`

3. **启用GitHub Pages**
   - 进入仓库Settings
   - 找到"Pages"选项
   - Source选择"Deploy from a branch"
   - Branch选择"main"
   - 点击"Save"

4. **等待部署**
   - GitHub Pages需要几分钟时间部署
   - 访问：`https://your-username.github.io`

## 测试应用

1. **测试后端API**
   - 访问：`https://your-app-name.onrender.com`
   - 应该看到：`{"message": "Climate Chat API is running!"}`

2. **测试前端**
   - 访问您的GitHub Pages地址
   - 输入包含关键词的消息（如"economic"、"health"等）
   - 检查是否显示相应的框架回复

## 故障排除

### 常见问题

1. **404错误**
   - 检查GitHub Pages设置
   - 确保`index.html`在根目录
   - 等待5-10分钟重新部署

2. **API连接失败**
   - 检查Render应用是否正常运行
   - 验证API URL是否正确
   - 确认环境变量已设置

3. **CORS错误**
   - 后端已配置CORS，应该不会有问题
   - 如果仍有问题，检查API URL格式

### 调试步骤

1. **检查浏览器控制台**
   - 按F12打开开发者工具
   - 查看Console和Network标签

2. **测试API端点**
   - 使用Postman或curl测试API
   - 确保返回正确的JSON响应

## 自定义配置

### 修改框架回复
编辑`index.html`中的`frameworkResponses`对象

### 添加新框架
1. 在`frameworkKeywords`中添加关键词
2. 在`frameworkResponses`中添加回复内容
3. 在`frameworkNames`中添加显示名称

### 更改样式
修改`index.html`中的CSS样式部分

## 技术栈

- **后端**: FastAPI + Python
- **前端**: HTML + CSS + JavaScript
- **AI**: OpenAI GPT-3.5-turbo
- **部署**: Render (后端) + GitHub Pages (前端)

## 许可证

MIT License

## 支持

如有问题，请创建GitHub Issue或联系开发者。
