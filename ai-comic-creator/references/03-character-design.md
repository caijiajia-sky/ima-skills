# 角色设计深度参考

## 一、角色设计标准流程

```
确定角色定位 → 基础特征设计 → 服装设计 → 细节添加 → 建立角色卡
```

## 二、角色类型参考

| 类型 | 特点 | 适用内容 |
|------|------|---------|
| 治愈系 | 可爱、温暖 | 日常、宠物 |
| 热血系 | 帅气、力量感 | 冒险、运动 |
| 温柔系 | 温柔、清新 | 情感、爱情 |
| 搞笑系 | 夸张、有趣 | 喜剧、吐槽 |
| 专业系 | 可信、权威 | 科普、教育 |

## 三、AI角色设计提示词模板

### 3.1 基础描述模板
```
[年龄] + [性别] + [种族/肤色] + [脸型] + 
[眼睛] + [鼻子] + [嘴巴] + [发型] + [体型]
```

### 3.2 细节强化词

**眼睛**：large expressive eyes, detailed eyelashes, beautiful detailed irises, glassy eyes

**嘴唇**：full lips, natural pink color, slight smile, glossy lips, defined cupid's bow

**皮肤**：porcelain skin, detailed skin texture, healthy glow, clear skin

## 四、六种辨识度设计方案

### 方案一：缺陷锚定法
用面部缺陷词增加真实感和辨识度：
- 雀斑 freckles → 增加真实感
- 牙缝 gap teeth → 独特记忆点
- 不对称 asymmetrical face → 打破完美
- 疤痕 scar → 故事感
- 眼袋 eye bags → 疲惫感

### 方案二：基因融合法
用名人特征混搭创造新面孔：
- 舒淇的宽眼距 + 杜鹃的清冷感 = 高级脸
- 梁朝伟的深情眼神 + 姜文的硬汉轮廓 = 魅力男
- 选长相有极强特点的名人，不要选标准帅哥美女

### 方案三：动物拟人法
| 动物特征 | 提示词 | 角色类型 |
|---------|--------|---------|
| 狐狸 | fox-like eyes | 狡猾者 |
| 老鹰 | eagle nose | 锐利者 |
| 狮子 | lion-like hair | 霸道者 |
| 鼠 | sharp small eyes | 精明者 |

### 方案四：地域血统法
精确到民族血统，利用AI训练数据中的面部骨骼差异：
- 因纽特人 Inuit
- 蒙古人 Mongolian
- 西西里人 Sicilian
- 藏族 Tibetan

### 方案五：标志物绑定法
| 标志物 | 提示词 | 视觉效果 |
|--------|--------|---------|
| 护目镜 | goggles | 科技感 |
| 眼罩 | eyepatch | 神秘感 |
| 面具 | mask | 隐藏感 |
| 纹身 | tattoo | 辨识度 |
| 烟斗 | pipe | 复古感 |

### 方案六：画风对抗法
用艺术家风格解构面部，天然抵抗AI平均化：
- Egon Schiele 席勒 → 扭曲、瘦削、神经质
- Norman Rockwell 洛克威尔 → 夸张生动、美式幽默
- Junji Ito 伊藤润二 → 恐怖、线条密集

## 五、表情设计参考

| 表情 | 英文提示词 | 适用场景 |
|------|----------|---------|
| 开心 | bright smile, happy expression, curved eyes, rosy cheeks | 日常、治愈 |
| 生气 | angry expression, furrowed brows, frown, glaring eyes | 冲突、搞笑 |
| 悲伤 | sad, crying, tear, downcast eyes | 情感、悲剧 |
| 惊讶 | wide eyes, open mouth, raised eyebrows | 高潮、反转 |
| 害羞 | blushing cheeks, shy smile, looking away | 甜蜜、暧昧 |
| 痛苦 | furrowed brows, grimace, hand on painful area | 健康科普 |

## 六、服装设计参考

| 服装类型 | 英文提示词 | 适用场景 |
|---------|----------|---------|
| 校服 | school uniform, sailor collar | 校园、青春 |
| 和服 | kimono, traditional Japanese | 文化、历史 |
| 现代休闲 | casual outfit, streetwear | 日常、都市 |
| 礼服 | elegant dress, gown | 正式、梦幻 |
| 职业装 | business suit, uniform | 职场、专业 |
| 白大褂 | white coat, medical uniform | 医疗、科普 |

服装描述公式：`[服装类型] + [颜色] + [材质] + [款式] + [配饰]`

## 七、发型设计参考

| 发型 | 英文提示词 | 气质 |
|------|----------|------|
| 长直发 | long straight hair | 温柔、成熟 |
| 双马尾 | twin tails, pigtails | 可爱、活力 |
| 短发 | short hair, bob | 干练、清爽 |
| 卷发 | curly hair, wavy | 浪漫、复古 |
| 盘发 | updo, bun | 正式、优雅 |
| 微卷短发 | short wavy hair | 知性、中年 |

| 发色 | 英文提示词 | 气质 |
|------|----------|------|
| 黑色 | black hair | 经典、神秘 |
| 棕色 | brown hair | 自然、温柔 |
| 金色 | blonde hair | 活泼、明亮 |
| 粉色 | pink hair | 可爱、梦幻 |

## 八、一致性锁定技术对比

| 方案 | 操作 | 适合工具 | 一致性 | 难度 |
|------|------|---------|-------|------|
| 固定前缀法 | 固定角色描述开头 | 所有 | ⭐⭐⭐ | 低 |
| 参考图法 | 生成满意图后做参考 | 即梦/MJ | ⭐⭐⭐⭐ | 低 |
| Seed固定法 | 复用首张图的Seed | 所有支持 | ⭐⭐⭐⭐ | 中 |
| --cref锁脸 | Midjourney角色参考 | MJ | ⭐⭐⭐⭐ | 中 |
| LoRA训练 | 训练专属模型 | SD | ⭐⭐⭐⭐⭐ | 高 |

## 九、即梦AI角色一致性实操

### 第一步：生成角色原图
1. 选择图片生成，模型2.1或2.0
2. 尺寸9:16
3. 生成满意角色图
4. 选择偏向正面、手脚展示全的图片
5. 点击超清，导出

### 第二步：参考人物角色画图
1. 选择角色原图作为参考
2. 调整参考强度
3. 模型选择与生成角色一致的模型
4. 在提示词中更改动作或场景即可

## 十、检查清单

### 设计前
- [ ] 确定角色定位和风格
- [ ] 设定性格特点
- [ ] 确定受众群体

### 设计后
- [ ] 各视角是否一致
- [ ] 表情是否生动
- [ ] 服装是否统一
- [ ] 细节是否完整
- [ ] 标志性特征是否明显

更新时间：2026-05-31
