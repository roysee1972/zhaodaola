# 找到啦 — 设计系统文档
# zhaodaola.top · DESIGN.md
# 基于 Stitch 规范，结合现有 12 关卡页面提取 + 8 个品牌设计系统最佳实践

---

## 1. 视觉主题与氛围

**一句话定义**: 温暖、沉静、有智慧感——像一个有阅历的长辈在跟你喝茶聊天。

**视觉气质**:
- 不是年轻人的潮酷风，也不是科技产品的冷峻感
- 是中国传统文化中的"温润如玉"——含蓄、内敛、有底蕴
- 让人静下心来审视自己的空间，不焦虑、不压迫
- 每个页面像翻开一本泛黄的笔记本，有纸张的质感

**设计哲学**:
- 信任靠一致性建立，不靠视觉冲击
- 内容是主角，装饰是配角
- 手机屏幕是主战场（480px 以内）
- 一次只让用户做一件事

**参考坐标**: Starbucks 的页面节奏 + Airbnb 的温暖信任感 + Apple 的留白哲学

---

## 2. 配色系统

### 2.1 四层色系结构（学自 Starbucks）

| 层级 | 角色 | 色值 | 用途 |
|------|------|------|------|
| **品牌色** | 智慧金 | `#c9a84c` | 主强调色、CTA按钮、金色装饰线、进度条 |
| **亮金色** | 活力金 | `#e8c870` | 按钮渐变终点、hover 状态、脉冲光效 |
| **深底色** | 温暖棕 | `#5a3e1b` | 正文主文字、深色功能带背景 |
| **浅底色** | 米黄纸 | `#f5e6c8` | 页面主背景、画布色 |

### 2.2 完整色板

**背景色梯度**:
| Token | 色值 | 用途 |
|-------|------|------|
| `--bg` | `#f5e6c8` | 主画布（温暖米黄，像老纸） |
| `--bg2` | `#eed9a4` | 二级背景（稍深，用于区块区分） |
| `--bg3` | `#e8d898` | 三级背景（最深，用于功能带） |
| `--card-bg` | `rgba(255,252,240,0.55)` | 卡片背景（半透明白，透出底色） |
| `--card-result` | `#fffdf5` | 结果页卡片（不透明暖白） |

**文字色层级**:
| Token | 色值 | 用途 |
|-------|------|------|
| `--text-dark` | `#5a3e1b` | 主文字、标题（温暖深棕，**不用纯黑**） |
| `--text-mid` | `#9a7a4a` | 副文字、说明（柔和褐色） |
| `--text-light` | `#b89a6a` | 辅助文字、标签、时间戳 |
| `--text-on-gold` | `#5a3e1b` | 金色按钮上的文字（深棕，不用白） |

**装饰与边框**:
| Token | 色值 | 用途 |
|-------|------|------|
| `--gold` | `#c9a84c` | 金色装饰线、图标、强调 |
| `--gold-light` | `#e8c870` | 金色渐变终点、光效 |
| `--border` | `rgba(139,90,43,0.18)` | 卡片边框、分隔线 |
| `--shadow` | `rgba(90,60,20,0.12)` | 阴影色（暖棕调，不用灰色） |

**诊断关卡辅助色**（每关一个，用于视觉区分，参考 Figma 彩色块思路）:
| 关卡 | 辅助色 | 色值 | 含义 |
|------|--------|------|------|
| 01 原生家庭 | 暖红 | `#c96b4c` | 家的温度 |
| 02 求知求学 | 书卷蓝 | `#6a8ca8` | 知识的冷静 |
| 03 初入人海 | 晨雾灰 | `#a8a090` | 世界的模糊 |
| 04 独立谋生 | 稻穗黄 | `#b8a040` | 劳作的收获 |
| 05 婚恋家庭 | 玫瑰棕 | `#b07878` | 感情的复杂 |
| 06 人到中年 | 秋叶橙 | `#c0884c` | 沉淀的温暖 |
| 07 金钱关系 | 铜钱绿 | `#7a9a6a` | 财富的生长 |
| 08 人际迷宫 | 雾霾蓝 | `#8898a8` | 关系的迷雾 |
| 09 兴趣爱好 | 活力橘 | `#d09050` | 热爱的火焰 |
| 10 心灵信仰 | 月光银 | `#a0a0a8` | 信仰的宁静 |
| 11 健康衰老 | 落叶金 | `#c0a860` | 生命的金黄 |
| 12 终篇传承 | 深棕木 | `#8a6a3a` | 传承的厚重 |

### 2.3 禁区
- ❌ 紫色渐变、霓虹色、冷色调大面积
- ❌ 纯黑 `#000000` 做文字（用 `#5a3e1b` 深棕代替）
- ❌ 纯白 `#ffffff` 做背景（用 `#f5e6c8` 米黄代替）
- ❌ 灰色阴影（用暖棕调 `--shadow` 代替）
- ❌ 辅助色做主 CTA（金色是唯一主 CTA 颜色）

---

## 3. 排版规则

### 3.1 字体栈

```css
/* 主字体 — 中文衬线，书卷气 */
--font: 'Noto Serif SC', 'STSong', 'SimSun', serif;

/* 辅助字体 — 用于标签、小字（可选） */
--font-sans: 'Noto Sans SC', 'PingFang SC', 'Microsoft YaHei', sans-serif;
```

**字体选择原则**:
- 正文和标题统一用衬线体（`--font`），营造"翻开笔记本"的感觉
- 标签、按钮、辅助信息可用无衬线体（`--font-sans`），但不是必须
- **禁止**: Inter, Roboto, Arial, Helvetica, 任何西方无衬线字体做正文

### 3.2 字号层级

| Token | 大小 | 粗细 | 行高 | 字距 | 用途 |
|-------|------|------|------|------|------|
| `hero-title` | 38px | 700 | 1.3 | 6px | 入口页大标题（"初入人海"） |
| `section-title` | 24px | 600 | 1.4 | 3px | 结果页段落标题 |
| `card-title` | 18px | 600 | 1.5 | 2px | 卡片标题（困境/盲区名称） |
| `body` | 15px | 400 | 1.8 | 1px | 正文（描述文字、诊断说明） |
| `body-sm` | 14px | 400 | 1.7 | 0 | 辅助正文、注释 |
| `label` | 13px | 500 | 1.4 | 2px | 标签文字（关卡名、分类） |
| `caption` | 11px | 400 | 1.4 | 4px | 眉标、徽章文字（"第三关"） |
| `button` | 15px | 600 | 1.0 | 4px | 按钮文字 |

**排版原则**:
- 正文行高 1.8-2.0，给中文阅读足够的呼吸空间
- 标题用字距(4-6px)营造仪式感，正文用小字距(1px)保持紧凑
- 标题 700 粗细，正文 400，层级靠粗细+字号共同区分
- **正文宽度不超过 520px**（手机阅读舒适区约 15-18 个汉字/行）

---

## 4. 组件样式

### 4.1 按钮

**主按钮（CTA）**:
```css
.btn {
  display: inline-block;
  padding: 12px 36px;
  background: linear-gradient(135deg, var(--gold), var(--gold-light));
  color: var(--text-dark);            /* 深棕文字，不用白 */
  font-family: var(--font);
  font-size: 15px;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  letter-spacing: 4px;
  transition: all 0.2s;
  box-shadow: 0 2px 8px rgba(201,168,76,0.3);
}
.btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 16px rgba(201,168,76,0.4);
}
.btn:active { transform: translateY(0); }
.btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
  transform: none !important;
  box-shadow: none !important;
}
```

**幽灵按钮（次要操作）**:
```css
.btn-ghost {
  background: transparent;
  border: 1px solid var(--gold);
  color: var(--text-mid);
  box-shadow: none;
}
.btn-ghost:hover { background: rgba(201,168,76,0.1); }
```

**按钮规则**:
- 圆角 8px（矩形感，不用药丸形）
- 按钮字距 4px（中文的仪式感）
- 金色渐变 + 暖棕阴影（不用灰色阴影）
- 按钮上文字用深棕（不用白色，保持温暖感）

### 4.2 卡片

**诊断选项卡**:
```css
.option-card {
  background: var(--card-bg);         /* rgba(255,252,240,0.55) */
  border: 1.5px solid var(--border);
  border-radius: 8px;
  padding: 16px 20px;
  cursor: pointer;
  transition: all 0.25s ease;
}
.option-card:hover {
  border-color: var(--gold);
  transform: translateY(-2px);
  box-shadow: 0 4px 16px var(--shadow);
}
.option-card.selected {
  border-color: var(--gold);
  background: rgba(201,168,76,0.08);
}
```

**结果卡（盲区/建议）**:
```css
.result-card {
  background: var(--card-result);     /* #fffdf5 */
  border: 1.5px solid var(--border);
  border-left: 4px solid var(--gold); /* 金色左边框 = 找到啦签名 */
  border-radius: 8px;
  padding: 20px 24px;
}
```

**卡片规则**:
- 圆角 8px，不用大圆角（保持端庄感）
- 半透明背景透出底色（有纸张叠加感）
- 结果卡左侧 4px 金色边框是找到啦的视觉签名
- 最多一层阴影，不用多重阴影堆叠

### 4.3 装饰元素

**金色分隔线**（页面签名元素）:
```css
.gold-line {
  width: 120px;
  height: 1px;
  background: linear-gradient(to right, transparent, var(--gold), transparent);
  margin: 0 auto 24px;
}
```

**装饰圆环**（入口页专用）:
```css
.deco-ring {
  width: 160px; height: 160px;
  border: 1.5px solid var(--border);
  border-radius: 50%;
  margin: 0 auto 40px;
  display: flex; align-items: center; justify-content: center;
  box-shadow:
    0 0 30px rgba(180,160,120,0.15),
    inset 0 0 30px rgba(180,160,120,0.08);
}
```

**页面内边框**（全局装饰）:
```css
body::after {
  content: '';
  position: fixed; inset: 8px;
  border: 1.5px solid var(--border);
  pointer-events: none; z-index: 0;
}
```

### 4.4 徽章/标签

```css
.level-badge {
  display: inline-block;
  font-size: 11px;
  letter-spacing: 5px;
  color: var(--text-light);
  border: 1px solid var(--border);
  padding: 4px 14px;
  border-radius: 20px;
}
```

### 4.5 进度条

```css
.progress-bar-wrap {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  height: 3px;
  background: rgba(201,168,76,0.15);
}
.progress-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--gold), var(--gold-light));
  transition: width 0.5s ease;
}
```

---

## 5. 布局原则

### 5.1 容器

```css
.page {
  max-width: 780px;       /* 桌面端最大宽度 */
  margin: 0 auto;
  padding: 40px 24px 80px;
}
```

**布局规则**:
- 手机优先，主战场 360-480px
- 桌面端居中，最大 780px（不用 1280px 的宽屏布局）
- 段间距: 标题后 12px，段落间 24px，区块间 40px
- 左右内边距 24px（手机端），40px（桌面端）

### 5.2 页面结构

每个关卡页面遵循统一结构（学自 Starbucks 的页面节奏）:

```
┌─────────────────────────┐
│    进度条（固定顶部）      │ ← 3px 金色渐变
├─────────────────────────┤
│                         │
│    眉标徽章（"第三关"）    │ ← 11px, 轻
│    大标题（"初入人海"）    │ ← 38px, 重, 金色强调字
│    金色分隔线             │ ← 签名元素
│    引导文字               │ ← 15px, 柔和
│    装饰圆环               │ ← 入口页专用
│    [开始按钮]             │ ← 金色渐变
│                         │
├─────────────────────────┤
│    层级标题               │ ← "第一层：选择困境"
│    选项卡片 × N           │ ← 半透明，可点选
│                         │
├─────────────────────────┤
│    层级标题               │ ← "第二层：诊断盲区"
│    诊断题 × N             │ ← 多选，卡片式
│                         │
├─────────────────────────┤
│    [查看结果] 按钮         │ ← 金色CTA
│                         │
├─────────────────────────┤
│    结果页                 │ ← 白底卡片，金色左边框
│      你的卡点：xxx        │
│      盲区诊断：xxx        │
│      建议：xxx            │
│    [下一关] [分享]        │
│                         │
└─────────────────────────┘
```

### 5.3 单列原则
- 永远单列布局，不用多栏网格
- 选项卡片垂直堆叠，不用水平排列
- 一次只展示一个层级（渐进式展开）

---

## 6. 深度与层次

### 6.1 层级方法

**学自 Apple：用颜色交替做深度，不用阴影堆叠。**

| 层级 | 方法 | 用途 |
|------|------|------|
| 第0层 | `--bg` (#f5e6c8) | 页面画布 |
| 第1层 | `--card-bg` (半透明白) | 选项卡片浮在画布上 |
| 第2层 | `--card-result` (#fffdf5) + 金色左边框 | 结果卡片（最高层级） |
| 装饰层 | `body::after` 内边框 | 全局画框效果 |

### 6.2 阴影规则
- 只用一种阴影：`0 2px 8px rgba(90,60,20,0.12)`（暖棕调）
- hover 时加深：`0 4px 16px rgba(90,60,20,0.15)`
- 不用多层阴影、不用大面积投影
- **阴影颜色永远是暖棕调，不用灰色**

### 6.3 动效
- 页面切换: `fadeIn 0.6s ease`（淡入+上移12px）
- 卡片 hover: `translateY(-2px)` + 阴影加深
- 按钮 hover: `translateY(-1px)` + 阴影加深
- 按钮 active: `translateY(0)` 回弹
- 装饰圆环: `pulse 3s ease-in-out infinite`（脉冲光效）
- **动效原则**: 克制、自然、不抢注意力。只有 hover 和页面切换有动效，不用滚动触发动画

---

## 7. 设计禁区（Do's and Don'ts）

### ✅ Do
- 每个页面有明确的视觉节奏：眉标→标题→分隔线→内容→操作
- 结果卡用金色左边框（找到啦的视觉签名）
- 正文行宽不超过 520px（约 15-18 汉字/行）
- 用 CSS 变量管理所有颜色（便于主题切换）
- 按钮字距 4px（中文的仪式感）
- 文字颜色用温暖深棕 `#5a3e1b`，不用纯黑
- 背景用温暖米黄 `#f5e6c8`，不用纯白
- 每关入口页有装饰圆环（品牌仪式感）
- 阴影用暖棕调，不用灰色

### ❌ Don't
- 不用全屏 Hero 大图（没有图片素材，用排版和装饰营造仪式感）
- 不用无限滚动（每个关卡是独立的完整旅程）
- 不用弹窗/模态框做诊断结果（结果直接展示在页面中）
- 不用多栏网格布局（始终单列）
- 不用药丸形按钮（圆角 8px 保持端庄）
- 不用超过两种字号做层级（标题+正文即可）
- 不用滚动触发的动画/视差效果
- 不用渐变背景（除了按钮金色渐变和分隔线渐隐）
- 不用 emoji 做图标（用 CSS 装饰或 SVG）
- 不用"点击这里"之类的引导文字（按钮自身就是引导）
- 不用加载动画/skeleton screen（纯静态页面，无需等待）

---

## 8. 响应式行为

### 8.1 断点

| 断点 | 宽度 | 适配 |
|------|------|------|
| 手机 | < 480px | 主战场：单列全宽，padding 24px |
| 大手机/小平板 | 480-768px | 同手机，内容区更宽松 |
| 平板 | 768-1024px | 居中，max-width 780px |
| 桌面 | > 1024px | 居中，max-width 780px |

### 8.2 触控目标
- 按钮最小高度 44px
- 选项卡片最小高度 56px
- 卡片之间间距 12px（防止误触）

### 8.3 字号缩放
- 手机端 hero-title: 32px（桌面 38px）
- 手机端 body: 15px（不变）
- 手机端 padding: 24px（桌面 40px）

---

## 9. Agent 指令速查

### 快速参考

```
配色速查:
  背景    #f5e6c8 (米黄)
  背景2   #eed9a4 (深米)
  背景3   #e8d898 (最深)
  文字    #5a3e1b (深棕)
  副文字  #9a7a4a (褐)
  浅文字  #b89a6a (浅褐)
  金色    #c9a84c (品牌金)
  亮金    #e8c870 (活力金)
  边框    rgba(139,90,43,0.18)
  阴影    rgba(90,60,20,0.12)

字体: 'Noto Serif SC', 'STSong', 'SimSun', serif
正文字号: 15px, 行高 1.8
标题字号: 38px(英雄) / 24px(段落) / 18px(卡片)
按钮圆角: 8px
卡片圆角: 8px
容器宽度: max-width 780px
基础间距: 24px(段间) / 40px(块间)
```

### 设计关键词
`温暖` `沉静` `智慧` `中式美学` `纸质感` `仪式感` `含蓄` `内敛`

### 禁区速查
`❌ 紫色渐变` `❌ 纯黑文字` `❌ 纯白背景` `❌ 灰色阴影`
`❌ 药丸按钮` `❌ 全屏Hero` `❌ 多栏布局` `❌ 滚动动画`
`❌ 弹窗结果` `❌ emoji图标` `❌ 加载骨架`

### 可借鉴的设计系统
- **Starbucks**: 四层色系组织 + 页面节奏 + 金色特殊时刻
- **Airbnb**: 温暖调性 + 单一强调色 + 信任靠一致性
- **Figma**: 每关一个辅助色做视觉区分
- **Apple**: 深度靠颜色交替而非阴影堆叠
