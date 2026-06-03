---
name: wechat-account-setup
description: 微信公众号账号接入与配置管理。当用户提到连接公众号、接入微信、配置公众号、接管公众号、设置白名单，或询问"微信公众号怎么配置"时触发。不适用于已配置好的文章发布场景（那是 wechat-article-publisher 的工作）。
---

# 微信公众号账号接入与配置

## 概述

管理微信公众号的接入配置，包括 AppID/AppSecret 配置、IP 白名单设置、access_token 获取与验证。

## 快速开始

### 已配置检测

每次对话开始时，检查是否存在配置文件：

```bash
cat /sandbox/workspace/skills/wechat-article-publisher/config.json
```

### 无配置时的接入流程

1. **获取凭证**
   - 用户提供 AppID 和 AppSecret
   - 或引导用户去 [微信公众平台](https://mp.weixin.qq.com) → 开发 → 基本配置 获取

2. **创建配置文件**

   在 `wechat-article-publisher` 技能目录创建 `config.json`：

   ```json
   {
     "appId": "用户的 AppID",
     "appSecret": "用户的 AppSecret",
     "ipWhitelist": ["服务器公网 IP"]
   }
   ```

3. **获取服务器 IP**

   ```bash
   curl -s https://ip.sb
   ```

4. **配置白名单**
   
   告知用户去微信公众平台 → 开发 → 基本配置 → IP白名单 添加服务器 IP

5. **验证连接**

   ```bash
   curl -s "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={AppID}&secret={AppSecret}"
   ```

   成功响应：`{"access_token": "xxx", "expires_in": 7200}`

### Token 管理

access_token 有效期 2 小时，每次 API 调用前需重新获取：

```bash
TOKEN=$(curl -s "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={AppID}&secret={AppSecret}" | python3 -c "import sys,json; print(json.load(sys.stdin).get('access_token',''))")
```

## 常见问题

| 问题 | 解决 |
|------|------|
| `errcode: 40013` | AppID 错误或未在白名单 |
| `errcode: 401 Unauthorized` | IP 未加入白名单 |
| `errcode: 48001` | API 未授权（需要更高权限） |

## 配置信息持久化

每次成功配置后，将 AppID 和配置路径写入 memory：

```bash
memory_write - content: "微信公众号 AppID: xxx，配置文件: skills/wechat-article-publisher/config.json"
```