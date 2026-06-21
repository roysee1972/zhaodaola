#!/usr/bin/env python3
"""Translate Chinese text in 4 HTML files to English."""
import re
import os

BASE = '/home/roysee/zhaodaola/wb0511/en'

def apply_replacements(filepath, replacements):
    """Read file, apply all (old, new) replacements, write back."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new, 1)
        else:
            # Try to find partial match for debugging
            pass
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Done: {filepath}")

# ============================================================
# File 4: 第四关-独立谋生.html (fully Chinese, needs full translation)
# ============================================================
def translate_file4():
    print("Translating 第四关-独立谋生.html ...")
    fp = os.path.join(BASE, '第四关-独立谋生.html')
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()

    # Fix lang
    c = c.replace('<html lang="zh-CN">', '<html lang="en">')

    # Meta description
    c = c.replace(
        'content="独立谋生关卡：经济独立与自我价值的碰撞，看见你在谋生路上的认知陷阱。"',
        'content="Earning a Living: The clash between financial independence and self-worth — see the cognitive traps on your path to making a living."'
    )

    # Title
    c = c.replace(
        '<title>第四关 · 独立谋生 — 找到啦</title>',
        '<title>Stage 4 · Earning a Living — Found It</title>'
    )

    # CSS comments - translate them
    css_comments = [
        ('/* ==================== 基础变量（与前几关保持一致）==================== */',
         '/* ==================== Base Variables (consistent with previous levels) ==================== */'),
        ('/* ==================== 全局 ==================== */',
         '/* ==================== Global ==================== */'),
        ('/* ==================== 页面容器 ==================== */',
         '/* ==================== Page Container ==================== */'),
        ('/* ==================== 通用组件 ==================== */',
         '/* ==================== Common Components ==================== */'),
        ('/* ==================== 进度条 ==================== */',
         '/* ==================== Progress Bar ==================== */'),
        ('/* ==================== P1: 入口页 ==================== */',
         '/* ==================== P1: Entry Page ==================== */'),
        ('/* ==================== P2: 困境瞬间选择页 ==================== */',
         '/* ==================== P2: Dilemma Moment Selection ==================== */'),
        ('/* ==================== P3: 冒险卡 ==================== */',
         '/* ==================== P3: Adventure Card ==================== */'),
        ('/* ==================== P4: 诊断测试 ==================== */',
         '/* ==================== P4: Diagnostic Test ==================== */'),
        ('/* ==================== P5: 诊断结果 ==================== */',
         '/* ==================== P5: Diagnosis Results ==================== */'),
        ('/* ==================== P6: 通关建议 ==================== */',
         '/* ==================== P6: Level Advice ==================== */'),
        ('/* ==================== P7: 隐藏关卡 ==================== */',
         '/* ==================== P7: Hidden Level ==================== */'),
        ('/* ==================== 彩蛋 ==================== */',
         '/* ==================== Easter Egg ==================== */'),
        ('/* ==================== 隐藏关卡入口 ==================== */',
         '/* ==================== Hidden Level Entry ==================== */'),
        ('/* ==================== 完成页 ==================== */',
         '/* ==================== Completion Page ==================== */'),
        ('/* ==================== 返回主页按钮 ==================== */',
         '/* ==================== Back to Home Button ==================== */'),
        ('/* ==================== 响应式 ==================== */',
         '/* ==================== Responsive ==================== */'),
        ('/* 装饰圆环 */', '/* Decorative Ring */'),
        ('/* 种子粒子动画 */', '/* Seed Particle Animation */'),
    ]
    for old, new in css_comments:
        c = c.replace(old, new)

    # HTML comments
    c = c.replace('<!-- 种子粒子装饰 -->', '<!-- Seed Particle Decorations -->')
    c = c.replace('<!-- 进度条 -->', '<!-- Progress Bar -->')
    c = c.replace('<!-- 返回主页按钮 -->', '<!-- Back to Home Button -->')
    c = c.replace('<!-- 彩蛋区域 -->', '<!-- Easter Egg Area -->')
    c = c.replace('<!-- enhance: 滚动淡入 + 回到顶部 -->', '<!-- enhance: scroll fade-in + back to top -->')
    c = c.replace('<!-- 访客计数器 -->', '<!-- Visitor Counter -->')

    # Back home button
    c = c.replace('title="返回主页"', 'title="Back to Home"')
    c = c.replace('<span>返回主页</span>', '<span>Back to Home</span>')

    # P1 Entry Page
    c = c.replace('<div class="level-badge">第四关 · 找到啦</div>', '<div class="level-badge">Stage 4 · Found It</div>')
    c = c.replace('<div class="deco-ring-inner">谋生</div>', '<div class="deco-ring-inner">Living</div>')
    c = c.replace('<h1 class="hero-title">独立谋生</h1>', '<h1 class="hero-title">Earning a Living</h1>')

    # Hero sub
    c = c.replace(
        '''<p class="hero-sub">
      你第一次说：<br>
      "我要自己挣。"
    </p>''',
        '''<p class="hero-sub">
      The first time you said:<br>
      "I want to earn my own money."
    </p>'''
    )

    # Text paragraphs on entry page
    c = c.replace(
        '''<p class="text-mid" style="margin-bottom: 12px; line-height: 1.9;">
      从伸手要钱，到伸手赚钱，<br>
      中间隔着的不只是一份工资，<br>
      是你第一次被世界打量、<br>
      被拒绝、被看见、被需要的全部过程。
    </p>''',
        '''<p class="text-mid" style="margin-bottom: 12px; line-height: 1.9;">
      From asking for money to earning it,<br>
      what lies between is more than just a paycheck —<br>
      it's the whole process of being sized up by the world,<br>
      being rejected, being seen, being needed.
    </p>'''
    )

    c = c.replace(
        '''<p class="text-mid" style="margin: 20px 0; line-height: 1.9;">
      这一关，不讲"年轻人要吃苦"。
      只是让你看见：<br>
      你是怎么从"伸手要"变成"伸手挣"的。
    </p>''',
        '''<p class="text-mid" style="margin: 20px 0; line-height: 1.9;">
      This level isn't about "young people must endure hardship."
      It just lets you see:<br>
      how you went from "asking" to "earning."
    </p>'''
    )

    c = c.replace('>开始探索</button>', '>Begin Exploration</button>')
    c = c.replace('>约需 6 分钟</p>', '>About 6 minutes</p>')

    # P2 Dilemma page
    c = c.replace(
        '<div class="level-badge">第四关 · 独立谋生</div>',
        '<div class="level-badge">Stage 4 · Earning a Living</div>'
    )
    # There are multiple of these, replace all
    c = c.replace(
        '<div class="level-badge">第四关 · 独立谋生</div>',
        '<div class="level-badge">Stage 4 · Earning a Living</div>'
    )

    c = c.replace(
        '<h2 style="font-size: 26px; font-weight: 700; color: var(--text-dark); letter-spacing: 3px; margin-bottom: 6px;">哪个瞬间，你最有感觉？</h2>',
        '<h2 style="font-size: 26px; font-weight: 700; color: var(--text-dark); letter-spacing: 3px; margin-bottom: 6px;">Which moment resonates with you the most?</h2>'
    )

    c = c.replace(
        '''<p class="text-mid mb-8" style="line-height: 1.8;">选 1-3 个你最有共鸣的谋生瞬间。<br>不用想，凭第一感觉选。</p>''',
        '<p class="text-mid mb-8" style="line-height: 1.8;">Select 1-3 moments that resonate most with you.<br>No need to overthink — go with your gut feeling.</p>'
    )

    # Layer titles
    c = c.replace('<div class="moment-layer-title">— 求职与起步 —</div>', '<div class="moment-layer-title">— Job Hunting & Starting Out —</div>')
    c = c.replace('<div class="moment-layer-title">— 第一次谋生 —</div>', '<div class="moment-layer-title">— First Time Earning —</div>')
    c = c.replace('<div class="moment-layer-title">— 压力与选择 —</div>', '<div class="moment-layer-title">— Pressure & Choices —</div>')

    c = c.replace('已选择 <span id="dilemmaCount">0</span> 个瞬间', 'Selected: <span id="dilemmaCount">0</span> moments')
    c = c.replace('>继续</button>', '>Continue</button>')

    # P3 Adventure card
    c = c.replace(
        '<h2 style="font-size: 20px; font-weight: 600; color: var(--text-dark); letter-spacing: 3px; margin-bottom: 6px;">抽一张冒险卡</h2>',
        '<h2 style="font-size: 20px; font-weight: 600; color: var(--text-dark); letter-spacing: 3px; margin-bottom: 6px;">Draw an Adventure Card</h2>'
    )
    c = c.replace(
        '<p class="text-mid" style="margin-bottom: 28px;">在开始诊断之前，让这张卡为你定个调。</p>',
        '<p class="text-mid" style="margin-bottom: 28px;">Before the diagnosis, let this card set the tone.</p>'
    )
    c = c.replace('>点击翻开</div>', '>Tap to Reveal</div>')
    c = c.replace('>冒险卡</div>', '>— Adventure Card</div>')
    c = c.replace('>点击卡牌翻开</p>', '>Tap the card to reveal</p>')
    c = c.replace('>开始诊断</button>', '>Start Diagnosis</button>')

    # P4 Question page
    c = c.replace('>第一题</div>', '>Question 1</div>')
    c = c.replace('>上一题</button>', '>Previous</button>')

    # P5 Result page
    c = c.replace('>诊断完成</div>', '>Diagnosis Complete</div>')
    c = c.replace('>你的谋生卡点画像</div>', '<div class="result-title">Your Livelihood Profile</div>')
    c = c.replace(
        '<div class="result-sub">第四关 · 独立谋生</div>',
        '<div class="result-sub">Stage 4 · Earning a Living</div>'
    )
    c = c.replace(
        '<div class="easter-egg-label">你发现了一个隐藏的思考</div>',
        '<div class="easter-egg-label">You discovered a hidden insight</div>'
    )
    c = c.replace('>查看通关建议</button>', '>View Level Advice</button>')

    # P6 Advice page
    c = c.replace(
        '<div class="advice-title">通关建议</div>',
        '<div class="advice-title">Level Advice</div>'
    )
    c = c.replace(
        '''<div class="advice-intro">
        谋生不是终点。<br>
        谋生是你和世界谈的第一笔交易。
      </div>''',
        '''<div class="advice-intro">
        Earning a living isn't the end goal.<br>
        It's the first deal you negotiate with the world.
      </div>'''
    )
    c = c.replace(
        '<button class="hidden-trigger" id="hiddenTrigger">以上不是你想说的？打开你的隐藏关卡 →</button>',
        '<button class="hidden-trigger" id="hiddenTrigger">Not what you wanted to say? Open your hidden level →</button>'
    )
    c = c.replace(
        '<div class="page-end-text">— 第四关 · 独立谋生 · 完 —</div>',
        '<div class="page-end-text">— Stage 4 · Earning a Living · Complete —</div>'
    )

    # P7 Hidden level
    c = c.replace(
        '<div class="level-badge">隐藏关卡</div>',
        '<div class="level-badge">Hidden Level</div>'
    )
    c = c.replace(
        '<div class="hidden-title">你的谋生初体验</div>',
        '<div class="hidden-title">Your First Earning Experience</div>'
    )
    c = c.replace(
        '''<div class="hidden-sub">
        这里是你的空间，写下你第一次「自己挣到钱」的故事。<br>
        不用修饰，真实就好。
      </div>''',
        '''<div class="hidden-sub">
        This is your space. Write about the first time you earned your own money.<br>
        No need to polish. Just be honest.
      </div>'''
    )

    # Hidden level steps
    c = c.replace('<div class="step-num">第一步</div>', '<div class="step-num">Step 1</div>')
    c = c.replace('<div class="step-num">第二步</div>', '<div class="step-num">Step 2</div>')
    c = c.replace('<div class="step-num">第三步</div>', '<div class="step-num">Step 3</div>')
    c = c.replace('<div class="step-num">第四步</div>', '<div class="step-num">Step 4</div>')

    c = c.replace(
        '<div class="step-label">我第一次真正"自己赚到钱"是什么时候？</div>',
        '<div class="step-label">When did I first truly "earn my own money"?</div>'
    )
    c = c.replace(
        '<textarea class="step-input" id="hidden1" placeholder="我记得……"></textarea>',
        '<textarea class="step-input" id="hidden1" placeholder="I remember..."></textarea>'
    )
    c = c.replace(
        '<div class="step-label">当时我对"钱"这件事是什么感觉？</div>',
        '<div class="step-label">How did I feel about "money" back then?</div>'
    )
    c = c.replace(
        '<textarea class="step-input" id="hidden2" placeholder="当时我觉得……"></textarea>',
        '<textarea class="step-input" id="hidden2" placeholder="At the time I felt..."></textarea>'
    )
    c = c.replace(
        '<div class="step-label">今天回过头看，我在"谋生"这件事上，最卡住我的是什么？</div>',
        '<div class="step-label">Looking back today, what holds me back the most in "earning a living"?</div>'
    )
    c = c.replace(
        '<textarea class="step-input" id="hidden3" placeholder="我最卡的地方是……"></textarea>',
        '<textarea class="step-input" id="hidden3" placeholder="What holds me back the most is..."></textarea>'
    )
    c = c.replace(
        '<div class="step-label">如果可以重来，我想对刚开始谋生的自己说什么？</div>',
        '<div class="step-label">If I could start over, what would I say to my younger self just beginning to earn a living?</div>'
    )
    c = c.replace(
        '<textarea class="step-input" id="hidden4" placeholder="我想对当时的自己说……"></textarea>',
        '<textarea class="step-input" id="hidden4" placeholder="I would tell my younger self..."></textarea>'
    )
    c = c.replace(
        '<button class="generate-btn" id="generateBtn">生成我的谋生觉醒卡片</button>',
        '<button class="generate-btn" id="generateBtn">Generate My Livelihood Awakening Card</button>'
    )
    c = c.replace(
        '<div class="card-preview-title">我的谋生初体验</div>',
        '<div class="card-preview-title">My First Earning Experience</div>'
    )
    c = c.replace(
        '<div class="card-preview-sub">第四关 · 独立谋生 · 找到啦</div>',
        '<div class="card-preview-sub">Stage 4 · Earning a Living · Found It</div>'
    )
    c = c.replace(
        '<button class="download-btn" id="downloadBtn">下载卡片</button>',
        '<button class="download-btn" id="downloadBtn">Download Card</button>'
    )

    # Completion page
    c = c.replace(
        '''<h2 style="font-size: 24px; font-weight: 700; color: var(--text-dark); letter-spacing: 4px; margin-bottom: 12px;">你已经通关</h2>''',
        '<h2 style="font-size: 24px; font-weight: 700; color: var(--text-dark); letter-spacing: 4px; margin-bottom: 12px;">Level Complete</h2>'
    )
    c = c.replace(
        '''<p class="text-mid" style="line-height: 2; margin-bottom: 24px;">
      从伸手要，到伸手挣，<br>
      每一步都是你和世界的真实对话。
    </p>''',
        '''<p class="text-mid" style="line-height: 2; margin-bottom: 24px;">
      From asking to earning,<br>
      every step is a real conversation with the world.
    </p>'''
    )
    c = c.replace('>重新开始</button>', '>Start Over</button>')

    # ===== JavaScript Data Section =====
    # JS comments
    c = c.replace(
        '/* ============================================================\n   数据：第四关 · 独立谋生\n   ============================================================ */',
        '/* ============================================================\n   Data: Stage 4 · Earning a Living\n   ============================================================ */'
    )
    c = c.replace('// 谋生困境瞬间（3层：求职与起步 / 第一次谋生 / 压力与选择）', '// Livelihood dilemma moments (3 layers: Job Hunting & Starting Out / First Earning / Pressure & Choices)')
    c = c.replace('// 第一层：求职与起步', '// Layer 1: Job Hunting & Starting Out')
    c = c.replace('// 第二层：第一次谋生', '// Layer 2: First Time Earning')
    c = c.replace('// 第三层：压力与选择', '// Layer 3: Pressure & Choices')
    c = c.replace('// 冒险卡（独立谋生）', '// Adventure Cards (Earning a Living)')
    c = c.replace('// 诊断题', '// Diagnostic Questions')
    c = c.replace('// 卡点完整数据', '// Complete Card Point Data')
    c = c.replace('// 彩蛋', '// Easter Eggs')
    c = c.replace(
        '/* ============================================================\n   状态\n   ============================================================ */',
        '/* ============================================================\n   State\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   页面导航（带错误处理）\n   ============================================================ */',
        '/* ============================================================\n   Page Navigation (with error handling)\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   困境瞬间选择\n   ============================================================ */',
        '/* ============================================================\n   Dilemma Moment Selection\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   冒险卡\n   ============================================================ */',
        '/* ============================================================\n   Adventure Card\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   诊断题\n   ============================================================ */',
        '/* ============================================================\n   Diagnostic Questions\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   诊断结果\n   ============================================================ */',
        '/* ============================================================\n   Diagnosis Results\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   通关建议\n   ============================================================ */',
        '/* ============================================================\n   Level Advice\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   隐藏关卡\n   ============================================================ */',
        '/* ============================================================\n   Hidden Level\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   启动 & 事件绑定\n   ============================================================ */',
        '/* ============================================================\n   Startup & Event Binding\n   ============================================================ */'
    )

    # Moment cards data
    moments_translations = [
        # Layer 1
        ('title: "投了20份简历，没有一个回音",\n    desc: "你认真改了每一份简历，写了每一封求职信。发出去之后，每天刷邮箱。一周后，你开始怀疑：是不是我的简历有什么问题？",\n    hint: "你就是那个每天刷邮箱的人。"',
         'title: "Sent out 20 resumes, got zero replies",\n    desc: "You carefully revised every resume, wrote every cover letter. After sending them out, you checked your email every day. A week later, you started wondering: is there something wrong with my resume?",\n    hint: "You are the one checking your inbox every day."'),
        ('title: "毕业了，不知道该干什么",\n    desc: "大学四年倏忽而过。拿到毕业证那天，你突然发现：读了这么多年书，却不知道自己真正想做什么、能做什么。",\n    hint: "你就是那个站在路口的毕业生。"',
         'title: "Graduated, but no idea what to do",\n    desc: "Four years of college flew by. On the day you got your diploma, you suddenly realized: after all those years of studying, you had no idea what you truly wanted to do or what you could do.",\n    hint: "You are the graduate standing at the crossroads."'),
        ('title: "第一份工作，和想象完全不一样",\n    desc: "你进去之前以为会是电视剧里的样子。进去之后，你发现每天做的是一些琐碎的、重复的、看不到意义的事。",\n    hint: "你就是那个坐在工位上发呆的人。"',
         'title: "Your first job was nothing like you imagined",\n    desc: "Before starting, you thought it would be like a TV drama. Once inside, you found yourself doing trivial, repetitive tasks that felt meaningless every day.",\n    hint: "You are the one staring blankly at your desk."'),
        ('title: "第一份工资，比想象中少很多",\n    desc: "你算了又算，扣掉房租和生活费，发现剩下的钱比你想象的少得多。你第一次意识到：赚钱真的不容易。",\n    hint: "你就是那个算完账发呆的人。"',
         'title: "Your first paycheck was much less than expected",\n    desc: "You calculated over and over. After deducting rent and living expenses, you found much less remained than you imagined. For the first time, you realized: earning money is truly not easy.",\n    hint: "You are the one staring into space after doing the math."'),
        # Layer 2
        ('title: "加班到很晚，但不知道为什么加班",\n    desc: "你不知道为什么今天要加班到这个点，也不知道明天会不会又是这样。你只知道：这是工作，应该的。",\n    hint: "你就是那个加班到深夜的人。"',
         'title: "Working overtime late, but not sure why",\n    desc: "You don\'t know why you have to work this late today, or whether tomorrow will be the same. You only know: this is work, it\'s expected.",\n    hint: "You are the one working late into the night."'),
        ('title: "付出和回报，总觉得不对等",\n    desc: "你做了很多，但拿到的却很少。你不是爱计较的人，但心里还是有一个声音在说：凭什么？",\n    hint: "你就是那个心里不平衡的人。"',
         'title: "Effort and reward always feel unequal",\n    desc: "You\'ve done a lot, but received so little. You\'re not the type to keep score, but there\'s still a voice inside asking: why?",\n    hint: "You are the one feeling the imbalance inside."'),
        ('title: "帮同事扛了活，他好像觉得理所当然",\n    desc: "你帮他做了一些本该他做的事。他没有说谢谢，好像这是你应该做的。",\n    hint: "你就是那个被当成理所当然的人。"',
         'title: "Helped a colleague with their work, and they took it for granted",\n    desc: "You helped them do things that were supposed to be their job. They didn\'t say thank you — as if it was your duty.",\n    hint: "You are the one being taken for granted."'),
        ('title: "换了几次方向，还是不确定",\n    desc: "你换了几份工作，试了几个方向，但还是不确定这是不是你要的。有时候你会想：是不是我太浮躁了？",\n    hint: "你就是那个一直在换方向的人。"',
         'title: "Changed direction several times, still uncertain",\n    desc: "You\'ve switched jobs, tried different paths, but still aren\'t sure this is what you want. Sometimes you wonder: am I too restless?",\n    hint: "You are the one always changing direction."'),
        # Layer 3
        ('title: "要养家了，钱不够用",\n    desc: "你结婚了，有孩子了，或者要照顾父母了。收入的压力突然变得很具体。你第一次感受到：钱不够用，是真的会很焦虑的事。",\n    hint: "你就是那个精打细算的人。"',
         'title: "Supporting a family, but money isn\'t enough",\n    desc: "You got married, had kids, or need to care for aging parents. The pressure of income suddenly became very real. For the first time, you felt: not having enough money truly causes anxiety.",\n    hint: "You are the one counting every penny."'),
        ('title: "在稳定和想要之间，左右为难",\n    desc: "有一份稳定的工作，但不是你想要的。想要去追一个梦想，但又不敢放弃现有的。",\n    hint: "你就是那个左右为难的人。"',
         'title: "Torn between stability and what you truly want",\n    desc: "You have a stable job, but it\'s not what you want. You want to chase a dream, but can\'t bring yourself to give up what you have.",\n    hint: "You are the one caught in the middle."'),
        ('title: "很努力，但钱总是不够花",\n    desc: "你已经比很多人努力了，但还是存不下钱。每个月到手的工资，好像怎么都不够。",\n    hint: "你就是那个精打细算的人。"',
         'title: "Working hard, but money is never enough",\n    desc: "You\'ve worked harder than many people, but still can\'t save. Every month\'s paycheck never seems to be enough.",\n    hint: "You are the one budgeting every month."'),
        ('title: "想安身立命，却没有落脚点",\n    desc: "你想在这个城市安定下来，但房价、户口、孩子上学……每一件事都在提醒你：你想安身，但这个城市好像不太欢迎你。",\n    hint: "你就是那个漂着的人。"',
         'title: "Wanting to settle down, but nowhere to land",\n    desc: "You want to put down roots in this city, but housing prices, residency permits, children\'s schooling... everything reminds you: you want to settle, but this city doesn\'t seem to welcome you.",\n    hint: "You are the one drifting."'),
    ]
    for old, new in moments_translations:
        c = c.replace(old, new)

    # Adventure cards
    adventure_cards_zh = [
        '"年轻时的穷，不是穷，是本钱。"',
        '"第一份工资多少不重要，重要的是你从中学到了什么。"',
        '"谋生这件事，有人早熟，有人晚熟，各有各的路。"',
        '"钱不是万能的，但没钱是万万不能的——这句话是真的。"',
        '"你不是在找一份工作，你是在找一种和世界打交道的方式。"',
        '"每个月的工资，不只是钱，是你用时间换来的生命。"',
        '"独立谋生，是你和世界谈的第一笔交易。谈得好不好，不只看钱。"',
        '"年轻时的迷茫不是病，是还没找到自己那块地。"',
        '"你羡慕的那些人，也有他们不说的难处。"',
        '"谋生的过程，也是在谋自己。"',
        '"真正的独立，不是不求人，是知道什么时候该求人。"',
        '"钱是工具，不是目的。你要的是用钱买来的那个东西。"',
    ]
    adventure_cards_en = [
        '"Poverty in youth isn\'t poverty — it\'s capital."',
        '"How much your first paycheck was doesn\'t matter. What matters is what you learned from it."',
        '"Earning a living: some mature early, some late — each has their own path."',
        '"Money isn\'t everything, but you can\'t do anything without it — this saying is true."',
        '"You\'re not just looking for a job — you\'re looking for a way to deal with the world."',
        '"Your monthly paycheck isn\'t just money — it\'s the life you traded your time for."',
        '"Earning your own living is the first deal you negotiate with the world. How well it goes depends on more than money."',
        '"Confusion in youth isn\'t a disease — you just haven\'t found your patch of land yet."',
        '"Those people you envy have their own unspoken struggles too."',
        '"The process of making a living is also the process of finding yourself."',
        '"True independence isn\'t never asking for help — it\'s knowing when to ask."',
        '"Money is a tool, not a goal. What you want is what money can buy."',
    ]
    for zh, en in zip(adventure_cards_zh, adventure_cards_en):
        c = c.replace(zh, en)

    # Questions data
    q_translations = [
        ('q: "你第一次认真考虑「我要自己赚钱」是什么时候？",', 'q: "When did you first seriously think about \'I want to earn my own money\'?",'),
        ('{ text: "很早了，读书时候就开始想办法赚钱了。", key: "01很早就开始谋生" },', '{ text: "Quite early — I started finding ways to earn money while still in school.", key: "01很早就开始谋生" },'),
        ('{ text: "毕业之后，开始真正意识到要自己养活自己。", key: "02毕业后开始谋生" },', '{ text: "After graduation, when I truly realized I needed to support myself.", key: "02毕业后开始谋生" },'),
        ('{ text: "有了家庭之后，责任变大了。", key: "03有家后开始认真" },', '{ text: "After starting a family, when responsibilities grew.", key: "03有家后开始认真" },'),
        ('{ text: "一直都知道，但没有认真想过这件事。", key: "04知道但不急" },', '{ text: "I always knew, but never seriously thought about it.", key: "04知道但不急" },'),
        ('{ text: "说不清，感觉是被推着往前走。", key: "05被推着走" },', '{ text: "Hard to say — it feels like I was pushed forward.", key: "05被推着走" },'),

        ('q: "当你第一次面对工作中的不公平，你会怎么做？",', 'q: "When you first faced unfairness at work, what did you do?",'),
        ('{ text: "忍着，觉得职场就是这样。", key: "06忍了" },', '{ text: "Endured it — that\'s just how the workplace is.", key: "06忍了" },'),
        ('{ text: "会生气，但不知道怎么表达。", key: "07生气但忍着" },', '{ text: "Got angry, but didn\'t know how to express it.", key: "07生气但忍着" },'),
        ('{ text: "会找机会说出来，哪怕冒点风险。", key: "08说出来" },', '{ text: "Found a chance to speak up, even at some risk.", key: "08说出来" },'),
        ('{ text: "会记下来，等机会来了再处理。", key: "09记下来等机会" },', '{ text: "Noted it down and waited for the right moment to deal with it.", key: "09记下来等机会" },'),
        ('{ text: "看情况，有时候忍，有时候说。", key: "10看情况" },', '{ text: "Depends on the situation — sometimes I endure, sometimes I speak up.", key: "10看情况" },'),

        ('q: "你目前对「赚钱」这件事，整体感觉是？",', 'q: "What is your overall feeling about \'earning money\' right now?",'),
        ('{ text: "只要努力，钱不是问题。", key: "11努力就有钱" },', '{ text: "As long as I work hard, money won\'t be a problem.", key: "11努力就有钱" },'),
        ('{ text: "赚钱很难，但我愿意努力。", key: "12难但努力" },', '{ text: "Earning money is hard, but I\'m willing to work for it.", key: "12难但努力" },'),
        ('{ text: "钱够用就好，不求大富大贵。", key: "13够用就好" },', '{ text: "Enough to get by is fine — I don\'t seek great wealth.", key: "13够用就好" },'),
        ('{ text: "有时候觉得钱很难赚，有时候又觉得还好。", key: "14时难时易" },', '{ text: "Sometimes earning money feels very hard, other times it\'s okay.", key: "14时难时易" },'),
        ('{ text: "不太愿意想这件事，想起来就焦虑。", key: "15想起来就焦虑" },', '{ text: "I don\'t like thinking about it — it makes me anxious.", key: "15想起来就焦虑" },'),

        ('q: "你在独立谋生这件事上，最大的卡点是什么？",', 'q: "What is your biggest obstacle in earning a living independently?",'),
        ('{ text: "不够自信，总觉得自己不够好。", key: "16不够自信" },', '{ text: "Not confident enough — I always feel I\'m not good enough.", key: "16不够自信" },'),
        ('{ text: "不知道该往哪个方向走。", key: "17方向迷茫" },', '{ text: "I don\'t know which direction to go.", key: "17方向迷茫" },'),
        ('{ text: "努力了但没有足够的回报。", key: "18回报不足" },', '{ text: "I work hard but don\'t get enough in return.", key: "18回报不足" },'),
        ('{ text: "缺乏资源和人脉。", key: "19资源不足" },', '{ text: "Lacking resources and connections.", key: "19资源不足" },'),
        ('{ text: "有时候很想放弃，但又不甘心。", key: "20想放弃又不甘" },', '{ text: "Sometimes I want to give up, but I can\'t accept that.", key: "20想放弃又不甘" },'),

        ('q: "如果可以改变一件事，你最想改变的是什么？",', 'q: "If you could change one thing, what would you most want to change?",'),
        ('{ text: "我希望我能更自信一些，不那么在意别人的眼光。", key: "21更自信" },', '{ text: "I wish I could be more confident and care less about what others think.", key: "21更自信" },'),
        ('{ text: "我希望我能找到一个真正适合自己的方向。", key: "22找到方向" },', '{ text: "I wish I could find a direction that truly suits me.", key: "22找到方向" },'),
        ('{ text: "我希望我的努力能得到更公平的回报。", key: "23公平回报" },', '{ text: "I wish my efforts could be rewarded more fairly.", key: "23公平回报" },'),
        ('{ text: "我希望我能放下对钱的焦虑。", key: "24放下焦虑" },', '{ text: "I wish I could let go of my anxiety about money.", key: "24放下焦虑" },'),
        ('{ text: "我希望我能学会更好地和这个社会打交道。", key: "25学会打交道" },', '{ text: "I wish I could learn to navigate society better.", key: "25学会打交道" },'),

        ('q: "你觉得自己对「独立谋生」的理解是什么？",', 'q: "What is your understanding of \'earning a living independently\'?",'),
        ('{ text: "自己赚钱自己花，不依赖别人。", key: "26不依赖" },', '{ text: "Earn your own money, spend your own money, don\'t depend on others.", key: "26不依赖" },'),
        ('{ text: "能够用自己的能力，换取应有的价值。", key: "27等价交换" },', '{ text: "Being able to exchange your abilities for their fair value.", key: "27等价交换" },'),
        ('{ text: "在这个世界上找到自己的位置。", key: "28找到位置" },', '{ text: "Finding your place in this world.", key: "28找到位置" },'),
        ('{ text: "能够负担自己选择的人生。", key: "29负担选择" },', '{ text: "Being able to afford the life you choose.", key: "29负担选择" },'),
        ('{ text: "说实话，我还在摸索。", key: "30还在摸索" },', '{ text: "Honestly, I\'m still figuring it out.", key: "30还在摸索" },'),
    ]
    for old, new in q_translations:
        c = c.replace(old, new)

    # cardPoints data
    cp_translations = [
        ('name: "很早就开始谋生",\n    desc: "你很早就开始面对「钱」这件事了。也许是因为家庭，也许是因为性格，你比同龄人更早知道：钱不是天上掉下来的。",\n    advice: "早起步的人，往往更有生存韧性。但也要注意：不要让「谋生」变成你唯一的事。你还值得拥有工作之外的东西。",',
         'name: "Started Earning Early",\n    desc: "You started facing the reality of money very early. Maybe because of family, maybe because of personality — you knew sooner than your peers that money doesn\'t fall from the sky.",\n    advice: "Early starters often have more resilience. But be careful: don\'t let earning a living become your only thing. You deserve more than just work.",'),
        ('name: "毕业后开始谋生",\n    desc: "毕业是你谋生的真正起点。你从象牙塔走出来，第一次真正面对社会的规则。这种转变，对每个人来说都不容易。",\n    advice: "毕业后的前几年，是建立「谋生操作系统」的关键期。你现在种下的习惯和观念，会影响你很多年。慢一点没关系，但要认真。",',
         'name: "Started After Graduation",\n    desc: "Graduation was your real starting point for earning a living. You stepped out of the ivory tower and faced society\'s rules for the first time. This transition isn\'t easy for anyone.",\n    advice: "The first few years after graduation are crucial for building your livelihood operating system. The habits and mindsets you plant now will affect you for years. Slow is fine, but be serious.",'),
        ('name: "有家后开始认真",\n    desc: "有了家庭之后，谋生就不只是你自己的事了。你要为另一个人、或者更多人负责。这种责任感，是压力，也是动力。",\n    advice: "有家的人，往往更有韧性。但也要记得：你不仅是支柱，你也是人。照顾好自己，才能照顾好家。",',
         'name: "Got Serious After Starting a Family",\n    desc: "Once you have a family, earning a living is no longer just about you. You\'re responsible for another person, or more. This sense of responsibility is both pressure and motivation.",\n    advice: "People with families often have more resilience. But remember: you\'re not just a pillar — you\'re also a person. Take care of yourself first to take care of your family.",'),
        ('name: "知道但不急",\n    desc: "你知道谋生是迟早的事，但还没有真正紧迫感。也许是因为有人兜底，也许是因为你还在摸索。这不是坏事，但也不能一直这样。",\n    advice: "不急是好的心态，但不能变成拖延。给自己设一个底线：在这个时间之前，我需要有一份稳定的收入来源。",',
         'name: "Know But Not Urgent",\n    desc: "You know earning a living is inevitable, but don\'t feel real urgency yet. Maybe someone has your back, maybe you\'re still exploring. It\'s not bad, but it can\'t last forever.",\n    advice: "Being unhurried is a good mindset, but don\'t let it become procrastination. Set a deadline: by this time, I need a stable income source.",'),
        ('name: "被推着走",\n    desc: "你的谋生之路，好像一直是「被推着」往前走。没有特别清晰的规划，也没有特别的紧迫感，只是事情来了就应对。",\n    advice: "被动谋生没有问题，但被动久了会累。试着偶尔停下来想一想：这是我想要的谋生方式吗？偶尔的主动思考，会让你更有方向感。",',
         'name: "Being Pushed Along",\n    desc: "Your path to earning a living seems to have been a matter of being pushed forward. No clear plan, no particular urgency — just dealing with things as they come.",\n    advice: "Passive earning isn\'t wrong, but it gets tiring after a while. Try stopping occasionally to think: is this the way I want to make a living? Occasional active thinking gives you more direction.",'),
        ('name: "忍了",\n    desc: "你选择了忍耐。职场不公平的事，你见过不少，但你选择不发作。这种忍，是成熟的体现，但也是委屈的积累。",\n    advice: "忍是智慧，但一直忍是压抑。找到一种方式，把忍下来的东西消化掉——运动、倾诉、或者写下来。忍不是目的，消化才是。",',
         'name: "Endured It",\n    desc: "You chose to endure. You\'ve seen plenty of unfairness at work, but chose not to react. This endurance is a sign of maturity, but it also accumulates grievance.",\n    advice: "Endurance is wisdom, but constant endurance becomes suppression. Find a way to process what you\'ve swallowed — exercise, talk it out, or write it down. Endurance isn\'t the goal; processing is.",'),
        ('name: "生气但忍着",\n    desc: "你心里有气，但你不知道怎么表达。你不是那种会当面冲突的人，所以你选择忍着。忍着忍着，气就憋在心里了。",\n    advice: "生气是正常的情绪，不是一种性格缺陷。下次生气的时候，试着找一个安全的方式表达——哪怕是发一条仅自己可见的微博。",',
         'name: "Angry But Holding Back",\n    desc: "You have anger inside, but don\'t know how to express it. You\'re not the type for confrontation, so you hold it in. Over time, the frustration builds up inside.",\n    advice: "Anger is a normal emotion, not a character flaw. Next time you\'re angry, try finding a safe way to express it — even posting something only you can see.",'),
        ('name: "说出来",\n    desc: "你会说出来。这需要勇气，尤其是在职场。但你选择了表达，哪怕有时候会得罪人。",\n    advice: "说出来是你的优势，但要注意方式。有时候「怎么说」比「说什么」更重要。学会在表达的同时保护自己。",',
         'name: "Speaks Up",\n    desc: "You speak up. This takes courage, especially at work. But you chose to express yourself, even if it sometimes ruffles feathers.",\n    advice: "Speaking up is your strength, but pay attention to how. Sometimes how you say it matters more than what you say. Learn to protect yourself while expressing yourself.",'),
        ('name: "记下来等机会",\n    desc: "你不会当场发作，但你会记下来。你知道有些事情需要时机，急不得。这种耐心，是成熟的表现。",\n    advice: "等待是好的策略，但不要让等待变成遗忘。定期回顾你记下来的那些事，想一想：现在是不是处理它们的时候？",',
         'name: "Notes It Down, Waits for the Right Moment",\n    desc: "You don\'t react on the spot, but you note it down. You know some things need the right timing and can\'t be rushed. This patience is a sign of maturity.",\n    advice: "Waiting is a good strategy, but don\'t let it become forgetting. Periodically review what you\'ve noted — is now the right time to deal with them?",'),
        ('name: "看情况",\n    desc: "你不是一个固定模式的人。你会根据情况来判断：什么时候该忍，什么时候该说。这种灵活性，是很好的生存能力。",\n    advice: "看情况是你的成熟，但也要小心：不要变成「没有立场」。在灵活的同时，保持自己内在的底线。",',
         'name: "Reads the Situation",\n    desc: "You\'re not a one-pattern person. You judge based on the situation: when to endure, when to speak up. This flexibility is a great survival skill.",\n    advice: "Reading the situation is your maturity, but be careful not to become someone with no position. Stay flexible while maintaining your inner bottom line.",'),
        ('name: "努力就有钱",\n    desc: "你对努力和回报的关系，还是比较乐观的。你相信：只要努力，钱不是问题。这种信念，是前进的动力。",\n    advice: "乐观是好的，但也要有现实的预期管理。不是所有努力都会立刻换来钱，但所有的努力都会以某种方式回报你。",',
         'name: "Hard Work Equals Money",\n    desc: "You\'re fairly optimistic about the relationship between effort and reward. You believe: as long as you work hard, money won\'t be a problem. This belief drives you forward.",\n    advice: "Optimism is good, but manage your expectations realistically. Not all effort immediately translates to money, but all effort pays you back in some way.",'),
        ('name: "难但努力",\n    desc: "你知道赚钱不容易，但你愿意努力。这种「清醒的努力」，比盲目乐观更难得。",\n    advice: "清醒的努力，是最好的状态。你不需要相信「努力就一定有回报」，你只需要相信：努力了，会比不努力更好一点。",',
         'name: "Hard But Trying",\n    desc: "You know earning money isn\'t easy, but you\'re willing to work for it. This kind of clear-eyed effort is rarer than blind optimism.",\n    advice: "Clear-eyed effort is the best state. You don\'t need to believe effort always pays off — just that effort makes things a little better than no effort.",'),
        ('name: "够用就好",\n    desc: "你不追求大富大贵，你觉得够用就好。这种知足，是很好的心态，但有时候也会让你失去一些进取的动力。",\n    advice: "知足是智慧，但「够用」的定义会随时间变化。定期想一想：现在的「够用」，未来还够用吗？",',
         'name: "Enough Is Enough",\n    desc: "You don\'t pursue great wealth — enough to get by is fine. This contentment is a healthy mindset, but sometimes it costs you some drive to push forward.",\n    advice: "Contentment is wisdom, but the definition of "enough" changes over time. Periodically ask yourself: will today\'s "enough" still be enough in the future?",'),
        ('name: "时难时易",\n    desc: "你对钱的感受，不是固定的。有时候觉得难，有时候又觉得还好。这种波动，让你对钱的焦虑也变得起伏不定。",\n    advice: "接受这种起伏。不同时期有不同的挑战，重要的是：在难的时候不放弃，在好的时候不挥霍。",',
         'name: "Sometimes Hard, Sometimes Easy",\n    desc: "Your feelings about money aren\'t fixed. Sometimes it feels hard, sometimes okay. This fluctuation makes your financial anxiety ebb and flow too.",\n    advice: "Accept the ups and downs. Different periods bring different challenges. What matters: don\'t give up when it\'s hard, and don\'t splurge when it\'s good.",'),
        ('name: "想起来就焦虑",\n    desc: "钱这件事，是你心里的一个痛点。你不愿意想它，但又会忍不住想。想起来就焦虑，焦虑完还是不知道怎么解决。",\n    advice: "焦虑说明你在乎。把焦虑写下来，变成具体的数字和计划。当焦虑变成具体的待办事项，它就没那么可怕了。",',
         'name: "Anxiety on My Mind",\n    desc: "Money is a sore spot in your heart. You don\'t want to think about it, but you can\'t help it. Thinking about it makes you anxious, and after the anxiety, you still don\'t know how to solve it.",\n    advice: "Anxiety shows you care. Write down your anxiety, turn it into concrete numbers and plans. When anxiety becomes a to-do list, it\'s not so scary anymore.",'),
        ('name: "不够自信",\n    desc: "你觉得自己不够好。这种自我怀疑，让你在谋生路上走得比实际需要的更艰难。",\n    advice: "自信不是天生的，是一次次做成事情之后积累的。给自己列一个小清单：过去一年，我做成过哪几件事？看见自己的过去，是建立自信的第一步。",',
         'name: "Not Confident Enough",\n    desc: "You feel you\'re not good enough. This self-doubt makes your path to earning a living harder than it actually needs to be.",\n    advice: "Confidence isn\'t innate — it\'s built by succeeding at things, one after another. Make a short list: what have I accomplished in the past year? Seeing your past is the first step to building confidence.",'),
        ('name: "方向迷茫",\n    desc: "你不知道该往哪个方向走。这种迷茫，是很多人都会经历的阶段。它不是问题，但它需要你主动去探索。",\n    advice: "方向不是想出来的，是试出来的。不用等一个「完美的方向」再开始，先做一些小尝试，在尝试中调整。",',
         'name: "Lost on Direction",\n    desc: "You don\'t know which direction to go. This confusion is a phase many people experience. It\'s not a problem, but it requires you to actively explore.",\n    advice: "Direction isn\'t figured out by thinking — it\'s found by trying. Don\'t wait for the perfect direction. Start with small experiments and adjust along the way.",'),
        ('name: "回报不足",\n    desc: "你觉得自己的付出没有得到应有的回报。这种不平衡感，是很多职场人都会有的感受。",\n    advice: "回报不足，有时候是真的，有时候是认知偏差。但不管是哪种，试着做两件事：1）提升自己的可替代性壁垒；2）学会让付出被看见。",',
         'name: "Insufficient Returns",\n    desc: "You feel your efforts aren\'t getting the reward they deserve. This sense of imbalance is something many working professionals experience.",\n    advice: "Insufficient returns are sometimes real, sometimes a cognitive bias. Either way, try two things: 1) raise your barriers to being replaced; 2) learn to make your efforts visible.",'),
        ('name: "资源不足",\n    desc: "你觉得自己的资源和人脉不够。这种感受是真实的，但也可能是「开始」的错觉——很多人都是从资源不足开始的。",\n    advice: "资源是可以积累的，不是一成不变的。给自己设一个「每月认识一个新朋友」的目标，一年下来，你的资源网络会完全不同。",',
         'name: "Lacking Resources",\n    desc: "You feel your resources and connections are insufficient. This feeling is real, but it might also be the illusion of starting out — many people begin with limited resources.",\n    advice: "Resources can be accumulated — they\'re not fixed. Set a goal to meet one new person each month. In a year, your network will be completely different.",'),
        ('name: "想放弃又不甘",\n    desc: "你有时候很想放弃，但又觉得已经走了这么远，放弃了太可惜。这种矛盾，让你很难受。",\n    advice: "放弃和不放弃，都是选择。关键是：你想放弃的是什么？是这件事，还是这个状态？想清楚这一点，答案就出来了。",',
         'name: "Want to Quit But Can\'t Accept It",\n    desc: "Sometimes you really want to give up, but you feel you\'ve come so far that quitting would be a waste. This contradiction is painful.",\n    advice: "Quitting and not quitting are both choices. The key: what do you want to quit? The thing itself, or the state you\'re in? Clarify this and the answer emerges.",'),
        ('name: "更自信",\n    desc: "你希望自己更自信。不要那么在意别人的眼光，更相信自己的判断。这种愿望，是成长的信号。",\n    advice: "自信不是「不在乎别人」，而是「在听别人意见的同时，相信自己的判断」。这是可以练习的——每次做决定之前，先写下来你自己的理由，再去问别人的意见。",',
         'name: "More Confidence",\n    desc: "You wish you were more confident. Caring less about others\' opinions, trusting your own judgment more. This desire is a signal of growth.",\n    advice: "Confidence isn\'t about not caring what others think — it\'s about trusting your own judgment while listening to others. This can be practiced: before each decision, write down your own reasons first, then ask others.",'),
        ('name: "找到方向",\n    desc: "你希望找到一个真正适合自己的方向。这种寻找，本身就是意义。方向不是一次找到的，是一次次排除之后剩下的。",\n    advice: "方向不是想出来的，是活出来的。多尝试，多体验，多反思。在这个过程中，适合你的方向会慢慢显现。",',
         'name: "Find Direction",\n    desc: "You want to find a direction that truly suits you. The search itself is meaningful. Direction isn\'t found once — it\'s what remains after eliminating alternatives.",\n    advice: "Direction isn\'t thought up — it\'s lived out. Try more, experience more, reflect more. In this process, the right direction will gradually reveal itself.",'),
        ('name: "公平回报",\n    desc: "你希望自己的努力能得到更公平的回报。这种诉求是正当的，但「公平」本身是一个复杂的概念。",\n    advice: "公平有时候需要争取，有时候需要接受，有时候需要换环境。试着分清楚：这件事，是需要你争取，还是需要你接受，还是需要你换一个地方？",',
         'name: "Fair Return",\n    desc: "You want your efforts to be rewarded more fairly. This is a legitimate desire, but fairness itself is a complex concept.",\n    advice: "Fairness sometimes needs to be fought for, sometimes accepted, sometimes requires a change of environment. Try to distinguish: does this situation require you to fight, accept, or move on?",'),
        ('name: "放下焦虑",\n    desc: "你希望放下对钱的焦虑。这是一种很高的境界——不是因为有钱才能放下，是因为心态变了。",\n    advice: "放下焦虑，不是假装钱不重要，而是：1）接受钱的不确定性；2）把钱和你的自我价值分开；3）把钱变成你实现其他目标的工具，而不是目标本身。",',
         'name: "Let Go of Anxiety",\n    desc: "You want to let go of your anxiety about money. This is a high state of mind — not because you have money, but because your mindset has shifted.",\n    advice: "Letting go of anxiety isn\'t pretending money doesn\'t matter. It\'s: 1) accepting financial uncertainty; 2) separating money from your self-worth; 3) making money a tool for other goals, not the goal itself.",'),
        ('name: "学会打交道",\n    desc: "你希望学会更好地和社会打交道。这种愿望，说明你意识到：谋生不仅是做事，也是做人。",\n    advice: "和社会打交道，不是讨好，而是建立互惠的关系。真诚、互利、保持边界——做到这三点，你会慢慢建立起自己的社会网络。",',
         'name: "Learn to Navigate Society",\n    desc: "You want to learn to navigate society better. This desire shows you realize: earning a living isn\'t just about doing work — it\'s also about dealing with people.",\n    advice: "Navigating society isn\'t about pleasing people — it\'s about building mutually beneficial relationships. Be genuine, be fair, maintain boundaries — do these three and you\'ll build your social network.",'),
        ('name: "不依赖",\n    desc: "你对独立谋生的理解是：自己赚钱自己花，不依赖别人。这是一种很朴素、也很真实的理解。",\n    advice: "不依赖是独立的第一步，但不是全部。真正的独立，是有能力依赖，也有能力不依赖——选择权在你手里。",',
         'name: "No Dependence",\n    desc: "Your understanding of earning a living independently is: earn your own, spend your own, don\'t depend on others. This is a simple and honest understanding.",\n    advice: "Not depending on others is the first step to independence, but not the whole picture. True independence is the ability to depend when needed and not depend when not — the choice is yours.",'),
        ('name: "等价交换",\n    desc: "你觉得独立谋生是用自己的能力，换取应有的价值。这种理解很成熟，说明你已经把谋生看作一种价值交换。",\n    advice: "等价交换是市场的逻辑，但在现实中，交换往往不是即时的。有时候多给一点，是在为未来存本金。",',
         'name: "Fair Exchange",\n    desc: "You see earning a living as exchanging your abilities for their fair value. This is a mature understanding — you\'ve come to see earning as a value exchange.",\n    advice: "Fair exchange is market logic, but in reality, exchanges are often not immediate. Sometimes giving a little extra is investing in your future.",'),
        ('name: "找到位置",\n    desc: "你觉得独立谋生是在这个世界上找到自己的位置。这种理解很深刻，说明你在思考谋生的意义，而不只是谋生的形式。",\n    advice: "找到位置是一个过程，不是一个结果。在找到之前，先让自己保持在场、保持尝试、保持开放。",',
         'name: "Find Your Place",\n    desc: "You see earning a living as finding your place in the world. This is a profound understanding — you\'re thinking about the meaning of earning, not just the form.",\n    advice: "Finding your place is a process, not a result. Before you find it, stay present, keep trying, stay open.",'),
        ('name: "负担选择",\n    desc: "你觉得独立谋生是能够负担自己选择的人生。这意味着：你承认选择是有代价的，你愿意为你的选择负责。",\n    advice: "负担选择，是成年人的标志。但也要记得：不是所有的代价都要你一个人扛。学会在需要的时候求助，也是独立的一部分。",',
         'name: "Afford Your Choices",\n    desc: "You see earning a living as being able to afford the life you choose. This means: you acknowledge choices have costs, and you\'re willing to take responsibility for your choices.",\n    advice: "Affording your choices is the mark of an adult. But remember: you don\'t have to bear every cost alone. Learning to ask for help when needed is also part of being independent.",'),
        ('name: "还在摸索",\n    desc: "你还在摸索对独立谋生的理解。这不是坏事——很多人一辈子都在摸索。重要的是：你一直在认真对待这件事。",\n    advice: "摸索本身，就是答案的一部分。你在认真思考谋生这件事，这件事本身就会慢慢给你答案。给自己一点时间。",',
         'name: "Still Figuring It Out",\n    desc: "You\'re still figuring out what earning a living independently means to you. This isn\'t bad — many people spend their whole lives figuring it out. What matters: you\'re taking it seriously.",\n    advice: "The exploration itself is part of the answer. The fact that you\'re seriously thinking about earning a living will gradually give you answers. Give yourself some time.",'),
    ]
    for old, new in cp_translations:
        c = c.replace(old, new)

    # Easter eggs
    c = c.replace(
        'title: "《智囊》· 范蠡",\n    text: "范蠡辅佐越王勾践灭吴复国后，功成身退，经商成为巨富。他知道：谋生不仅是赚钱，是知道什么时候进，什么时候退。真正的智慧，是在成功的时候选择离开。"',
        'title: "The Wisdom of Fan Li",\n    text: "After helping King Goujian of Yue defeat Wu and restore his kingdom, Fan Li retired from politics and became a wealthy merchant. He knew: earning a living isn\'t just about making money — it\'s knowing when to advance and when to retreat. True wisdom is choosing to leave at the height of success."'
    )
    c = c.replace(
        'title: "《智囊》· 吕不韦",\n    text: "吕不韦是战国时期的大商人，他说：「奇货可居。」他看见的不仅是眼前的利润，是未来的价值。谋生也是如此——有时候你看的不只是现在能赚多少，是这条路能把你带到哪里。"',
        'title: "The Wisdom of Lü Buwei",\n    text: "Lü Buwei was a great merchant of the Warring States period. He said: \'Rare goods are worth holding.\' He saw not just immediate profits, but future value. Earning a living is the same — sometimes you\'re not just looking at how much you can earn now, but where this path can take you."'
    )
    c = c.replace(
        'title: "心理学研究：禀赋效应",\n    text: "心理学家发现：人们对自己拥有的东西估值更高。这就是为什么很多人不愿意换工作、换方向——不是因为那个选择真的更好，是因为「已经拥有了」。打破禀赋效应，是理性谋生的第一步。"',
        'title: "Psychology: The Endowment Effect",\n    text: "Psychologists have found that people value things they own more highly. This is why many people are reluctant to switch jobs or change direction — not because the other choice is truly better, but because \'I already have this.\' Breaking the endowment effect is the first step to rational career decisions."'
    )
    c = c.replace(
        'title: "反脆弱",\n    text: "塔勒布说：反脆弱的东西，不是坚强，是从冲击中获益。谋生也是如此——那些能从小挫折中学习的人，比一直顺风顺水的人更有生命力。小的失败不是诅咒，是疫苗。"',
        'title: "Antifragile",\n    text: "Nassim Taleb says: antifragile things aren\'t just strong — they benefit from shocks. Earning a living is the same — those who learn from small setbacks have more vitality than those who\'ve always had smooth sailing. Small failures aren\'t curses; they\'re vaccines."'
    )

    # JS function strings
    c = c.replace("alert('页面加载出错，请刷新重试。');", "alert('Page loading error. Please refresh and try again.');")
    c = c.replace("alert('发生错误：' + e.message);", "alert('An error occurred: ' + e.message);")
    c = c.replace("'点击卡牌翻开'", "'Tap the card to reveal'")
    c = c.replace("'— 这张卡，陪你去诊断 —'", "'— This card accompanies you to the diagnosis —'")
    c = c.replace("`第${currentQuestion + 1}题`", "`Question ${currentQuestion + 1}`")
    c = c.replace("'继续' : '查看结果'", "'Continue' : 'View Results'")
    c = c.replace("alert('先写点什么吧，至少说一件你记得的谋生瞬间。');", "alert('Please write something first — at least one earning moment you remember.');")
    c = c.replace("`第${['一','二','三','四'][i]}步：${t}`", "`Step ${['One','Two','Three','Four'][i]}: ${t}`")

    # Result summary texts
    c = c.replace(
        '`你最核心的谋生卡点是「${topCp ? topCp.name : \'未知\'}」。看见它，你已经比很多人走得更远了。`',
        '`Your core livelihood block is \'${topCp ? topCp.name : \'Unknown\'}\'. Seeing it means you\'ve already gone further than many.`'
    )
    c = c.replace(
        '`你有 ${sorted.filter(s=>s[1]>=2).length} 个较深的卡点，它们交织在一起，塑造了你面对谋生时的反应模式。`',
        '`You have ${sorted.filter(s=>s[1]>=2).length} deeper blocks that interweave, shaping how you respond to earning a living.`'
    )
    c = c.replace(
        '"谋生不是你和世界的对抗，是你和世界的第一笔合作。对话不一定每次都愉快，但每次都有信息。"',
        '"Earning a living isn\'t a confrontation with the world — it\'s your first collaboration. The conversation isn\'t always pleasant, but it always has a message."'
    )

    # Result card score text
    c = c.replace('命中 ${score} 次', 'matched ${score} times')

    # Advice card label
    c = c.replace("'卡点 '", "'Block '")

    # Hidden level responses
    c = c.replace(
        '"你写的这些，是很多人不愿意面对的。你做了，这本身就是勇气。"',
        '"What you\'ve written is what many people refuse to face. You did it — that itself is courage."'
    )
    c = c.replace(
        '"那个从伸手要到伸手挣的人，一直在你心里。看见他，已经是和解的开始。"',
        '"The person who went from asking to earning has always been inside you. Seeing them is already the beginning of reconciliation."'
    )
    c = c.replace(
        '"有些卡点不是你一个人有的。你愿意把它写出来，本身就是治愈。"',
        '"Some blocks aren\'t yours alone. Being willing to write them down is itself healing."'
    )
    c = c.replace(
        '"不是所有人的谋生之路都顺遂。写过这张卡片的人，已经看见了自己的路。"',
        '"Not everyone\'s path to earning a living is smooth. Those who\'ve written this card have already seen their own path."'
    )

    # Hidden level action text
    c = c.replace(
        '`今天先做这一件事：${h4.split(\'，\')[0].split(\'。\')[0]}`',
        '`Start with this one thing today: ${h4.split(\',\')[0].split(\'.\')[0]}`'
    )
    c = c.replace(
        "'今天，就做一件事：下次觉得自己不够好的时候，先想一想你已经走到今天，已经很不容易了。'",
        "'Today, do just one thing: next time you feel you're not good enough, remind yourself how far you've already come — that alone is remarkable.'"
    )

    # Download card canvas text
    c = c.replace("ctx.fillText('我的谋生初体验', 300, 80);", "ctx.fillText('My First Earning Experience', 300, 80);")
    c = c.replace("ctx.fillText('第四关 · 独立谋生 · 找到啦', 300, 108);", "ctx.fillText('Stage 4 · Earning a Living · Found It', 300, 108);")
    c = c.replace("ctx.fillText('— 第四关 · 独立谋生 · 完 —', 300, 750);", "ctx.fillText('— Stage 4 · Earning a Living · Complete —', 300, 750);")
    c = c.replace("link.download = '我的谋生初体验.png';", "link.download = 'my-first-earning.png';")

    # Visitor counter
    c = c.replace('您是第', 'You are visitor #')
    c = c.replace('位访客', '')

    # Render moments function
    c = c.replace(
        'function renderMoments() {\n  const layer1',
        'function renderMoments() {\n  // Re-render all layers\n  const layer1'
    )

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)
    print("  Done: 第四关-独立谋生.html")


# ============================================================
# File 12: 第十二关-终篇传承.html (fully Chinese, needs full translation)
# ============================================================
def translate_file12():
    print("Translating 第十二关-终篇传承.html ...")
    fp = os.path.join(BASE, '第十二关-终篇传承.html')
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()

    # Fix lang
    c = c.replace('<html lang="zh-CN">', '<html lang="en">')

    # Meta description
    c = c.replace(
        'content="终篇传承关卡：你想留下什么？这是生命最后的追问。"',
        'content="Legacy & Passing On: What do you want to leave behind? The final question of life."'
    )

    # Title
    c = c.replace(
        '<title>第十二关 · 终篇传承 — 找到啦</title>',
        '<title>Stage 12 · Legacy & Passing On — Found It</title>'
    )

    # HTML comments
    c = c.replace('<!-- enhance: 滚动淡入 + 回到顶部 -->', '<!-- enhance: scroll fade-in + back to top -->')
    c = c.replace('<!-- 访客计数器 -->', '<!-- Visitor Counter -->')

    # Back home button
    c = c.replace('title="返回主页"', 'title="Back to Home"')
    c = c.replace('<span>返回主页</span>', '<span>Back to Home</span>')

    # P1 Entry Page
    c = c.replace('<div class="level-badge">第十二关 · 找到啦</div>', '<div class="level-badge">Stage 12 · Found It</div>')
    c = c.replace('<div class="deco-ring-inner">传承</div>', '<div class="deco-ring-inner">Legacy</div>')
    c = c.replace('<h1 class="hero-title">终篇 · 传承</h1>', '<h1 class="hero-title">Final Chapter · Legacy</h1>')

    c = c.replace(
        '''<p class="hero-sub">
      写遗书太早，写人生回顾刚刚好<br>
      这一关不谈死亡，帮你回望
    </p>''',
        '''<p class="hero-sub">
      Too early to write a will, but just right for a life review<br>
      This level doesn't talk about death — it helps you look back
    </p>'''
    )

    c = c.replace(
        '''<p class="text-mid" style="margin-bottom: 12px; line-height: 1.9;">
      你有没有想过：<br>
      如果今天就是最后一天，我会后悔什么？<br>
      我这辈子，到底留下了什么？<br>
      或者——我害怕被遗忘吗？
    </p>''',
        '''<p class="text-mid" style="margin-bottom: 12px; line-height: 1.9;">
      Have you ever wondered:<br>
      If today were my last day, what would I regret?<br>
      What have I actually left behind in this life?<br>
      Or — am I afraid of being forgotten?
    </p>'''
    )

    c = c.replace(
        '''<p class="text-mid" style="margin: 20px 0; line-height: 1.9;">
      死亡不是人生的对立面，是人生的一部分。<br>
      这一关，不给你答案，只陪你<br>
      看见自己走过的路。
    </p>''',
        '''<p class="text-mid" style="margin: 20px 0; line-height: 1.9;">
      Death isn't the opposite of life — it's part of it.<br>
      This level doesn't give you answers, it just accompanies you<br>
      in seeing the path you've walked.
    </p>'''
    )

    c = c.replace('onclick="goPage(\'dilemma\')">开始探索</button>', 'onclick="goPage(\'dilemma\')">Begin Exploration</button>')
    c = c.replace('>约需 5 分钟</p>', '>About 5 minutes</p>')

    # P2 Dilemma page
    c = c.replace('<div class="level-badge">第十二关 · 终篇传承</div>', '<div class="level-badge">Stage 12 · Legacy & Passing On</div>')
    c = c.replace('<div class="level-badge">第十二关 · 终篇传承</div>', '<div class="level-badge">Stage 12 · Legacy & Passing On</div>')

    c = c.replace(
        '<h2 class="hero-title" style="font-size: 26px;">在哪件事上，你最困惑？</h2>',
        '<h2 class="hero-title" style="font-size: 26px;">What confuses you the most?</h2>'
    )
    c = c.replace(
        '<p class="text-mid mb-8" style="line-height: 1.8;">选 1-3 条最触动你的。不需要勇敢，诚实就好。</p>',
        '<p class="text-mid mb-8" style="line-height: 1.8;">Select 1-3 items that resonate most with you. No courage needed — just honesty.</p>'
    )
    c = c.replace('已选择 <span id="dilemmaCount">0</span> 条', 'Selected: <span id="dilemmaCount">0</span>')
    c = c.replace('>继续</button>', '>Continue</button>')

    # P3 Adventure card
    c = c.replace(
        '<h2 style="font-size: 20px; font-weight: 600; color: var(--text-dark); letter-spacing: 3px; margin-bottom: 6px;">先抽一张冒险卡</h2>',
        '<h2 style="font-size: 20px; font-weight: 600; color: var(--text-dark); letter-spacing: 3px; margin-bottom: 6px;">Draw an Adventure Card First</h2>'
    )
    c = c.replace(
        '<p class="text-mid" style="margin-bottom: 28px;">在开始诊断之前，让这张卡为你定个调。</p>',
        '<p class="text-mid" style="margin-bottom: 28px;">Before the diagnosis, let this card set the tone.</p>'
    )
    c = c.replace('>点击翻开</div>', '>Tap to Reveal</div>')
    c = c.replace('>冒险卡</div>', '>— Adventure Card</div>')
    c = c.replace('>点击卡牌翻开</p>', '>Tap the card to reveal</p>')
    c = c.replace('>开始诊断</button>', '>Start Diagnosis</button>')

    # P4 Question page
    c = c.replace('>第一题</div>', '>Question 1</div>')
    c = c.replace('>上一题</button>', '>Previous</button>')

    # P5 Result page
    c = c.replace('>诊断完成</div>', '>Diagnosis Complete</div>')
    c = c.replace(
        '<div class="result-title">你的人生回望画像</div>',
        '<div class="result-title">Your Life Reflection Profile</div>'
    )
    c = c.replace(
        '<div class="result-sub">终篇传承 · 第十二关</div>',
        '<div class="result-sub">Legacy & Passing On · Stage 12</div>'
    )
    c = c.replace(
        '<div class="easter-egg-label">你发现了一个关于人生的小秘密</div>',
        '<div class="easter-egg-label">You discovered a little secret about life</div>'
    )
    c = c.replace('>查看通关建议</button>', '>View Level Advice</button>')

    # P6 Advice page
    c = c.replace(
        '<div class="advice-title">通关建议</div>',
        '<div class="advice-title">Level Advice</div>'
    )
    c = c.replace(
        '''<div class="advice-intro">
        终篇，不是终点，是一面镜子。<br>
        不需要想通生死，只需要看见自己。<br>
        这一关，帮你回望走过的路。
      </div>''',
        '''<div class="advice-intro">
        The final chapter isn't the end — it's a mirror.<br>
        You don't need to resolve life and death, just see yourself.<br>
        This level helps you look back at the path you've walked.
      </div>'''
    )

    # Link to stories
    c = c.replace(
        '📖 临终故事十二则：人类最后的遗言',
        '📖 Twelve End-of-Life Stories: Humanity\'s Last Words'
    )
    c = c.replace(
        '<button class="hidden-trigger" id="hiddenTrigger" onclick="goHidden()">\n      以上不是你想说的？打开你的隐藏关卡 →\n    </button>',
        '<button class="hidden-trigger" id="hiddenTrigger" onclick="goHidden()">\n      Not what you wanted to say? Open your hidden level →\n    </button>'
    )
    c = c.replace(
        '<div class="page-end-text">— 第十二关 · 终篇传承 · 完 —</div>',
        '<div class="page-end-text">— Stage 12 · Legacy & Passing On · Complete —</div>'
    )

    # P7 Hidden level
    c = c.replace('<div class="level-badge">隐藏关卡</div>', '<div class="level-badge">Hidden Level</div>')
    c = c.replace(
        '<div class="hidden-title">你的专属关卡</div>',
        '<div class="hidden-title">Your Personal Level</div>'
    )
    c = c.replace(
        '''<div class="hidden-sub">
        这里是你的空间，写下关于「终篇」你真正想说的。<br>
        不用修饰，不用在意文采。真实就好。
      </div>''',
        '''<div class="hidden-sub">
        This is your space. Write what you truly want to say about the "final chapter."<br>
        No need to polish. Just be honest.
      </div>'''
    )

    # Hidden level steps
    c = c.replace('<div class="step-num">第一步</div>', '<div class="step-num">Step 1</div>')
    c = c.replace('<div class="step-num">第二步</div>', '<div class="step-num">Step 2</div>')
    c = c.replace('<div class="step-num">第三步</div>', '<div class="step-num">Step 3</div>')
    c = c.replace('<div class="step-num">第四步</div>', '<div class="step-num">Step 4</div>')

    c = c.replace(
        '<div class="step-label">如果今天是你最后一天，你最想做的一件事是？</div>',
        '<div class="step-label">If today were your last day, what is the one thing you\'d most want to do?</div>'
    )
    c = c.replace(
        '<textarea class="step-input" id="hidden1" placeholder="如果时间只剩一天，我会……"></textarea>',
        '<textarea class="step-input" id="hidden1" placeholder="If I had only one day left, I would..."></textarea>'
    )
    c = c.replace(
        '<div class="step-label">你希望别人怎么记住你？用一句话。</div>',
        '<div class="step-label">How do you want others to remember you? In one sentence.</div>'
    )
    c = c.replace(
        '<textarea class="step-input" id="hidden2" placeholder="我希望被人记住的样子是……"></textarea>',
        '<textarea class="step-input" id="hidden2" placeholder="I want to be remembered as..."></textarea>'
    )
    c = c.replace(
        '<div class="step-label">这辈子你最骄傲的一个决定是什么？</div>',
        '<div class="step-label">What is the decision you are most proud of in your life?</div>'
    )
    c = c.replace(
        '<textarea class="step-input" id="hidden3" placeholder="我最骄傲的决定是……"></textarea>',
        '<textarea class="step-input" id="hidden3" placeholder="The decision I\'m most proud of is..."></textarea>'
    )
    c = c.replace(
        '<div class="step-label">给十年后的自己留一句话。</div>',
        '<div class="step-label">Leave a message for yourself ten years from now.</div>'
    )
    c = c.replace(
        '<textarea class="step-input" id="hidden4" placeholder="十年后的我，我想对你说……"></textarea>',
        '<textarea class="step-input" id="hidden4" placeholder="To my future self, I want to say..."></textarea>'
    )
    c = c.replace(
        '<button class="generate-btn" onclick="generateCard()">生成我的隐藏关卡卡片</button>',
        '<button class="generate-btn" onclick="generateCard()">Generate My Hidden Level Card</button>'
    )
    c = c.replace(
        '<div class="card-preview-title">我的人生回望书</div>',
        '<div class="card-preview-title">My Life Reflection Book</div>'
    )
    c = c.replace(
        '<div class="card-preview-sub">第十二关 · 终篇传承 · 找到啦</div>',
        '<div class="card-preview-sub">Stage 12 · Legacy & Passing On · Found It</div>'
    )
    c = c.replace(
        '<button class="download-btn" onclick="downloadCard()">下载卡片</button>',
        '<button class="download-btn" onclick="downloadCard()">Download Card</button>'
    )

    # Completion page
    c = c.replace(
        '<h2 style="font-size: 24px; font-weight: 700; color: var(--text-dark); letter-spacing: 4px; margin-bottom: 12px;">十二关，你走到了这里</h2>',
        '<h2 style="font-size: 24px; font-weight: 700; color: var(--text-dark); letter-spacing: 4px; margin-bottom: 12px;">Twelve Levels — You Made It Here</h2>'
    )
    c = c.replace(
        '''<p class="text-mid" style="line-height: 2; margin-bottom: 24px;">
      从原生家庭到终篇传承，<br>
      你已经走完了人生的整个圆。<br>
      这不是终点，是另一个起点。
    </p>''',
        '''<p class="text-mid" style="line-height: 2; margin-bottom: 24px;">
      From your family of origin to legacy and passing on,<br>
      you've walked the entire circle of life.<br>
      This isn't the end — it's another beginning.
    </p>'''
    )
    c = c.replace('>重新开始</button>', '>Start Over</button>')

    # ===== JavaScript Data Section =====
    # JS comments
    c = c.replace(
        '/* ============================================================\n   数据\n   ============================================================ */',
        '/* ============================================================\n   Data\n   ============================================================ */'
    )
    c = c.replace('// 困境（12条，3层：回望来路/此刻重量/留下什么）', '// Dilemmas (12 items, 3 layers: Looking Back / The Weight of Now / What to Leave Behind)')
    c = c.replace('// 冒险卡（12张）', '// Adventure Cards (12)')
    c = c.replace('// 诊断题（6题×5选项）', '// Diagnostic Questions (6 × 5 options)')
    c = c.replace('// 卡点完整数据（30个维度）', '// Complete Card Point Data (30 dimensions)')
    c = c.replace('// 彩蛋（4个，围绕终篇传承主题）', '// Easter Eggs (4, around legacy theme)')
    c = c.replace(
        '/* ============================================================\n   状态\n   ============================================================ */',
        '/* ============================================================\n   State\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   页面导航\n   ============================================================ */',
        '/* ============================================================\n   Page Navigation\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   困境选择\n   ============================================================ */',
        '/* ============================================================\n   Dilemma Selection\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   冒险卡\n   ============================================================ */',
        '/* ============================================================\n   Adventure Card\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   诊断题\n   ============================================================ */',
        '/* ============================================================\n   Diagnostic Questions\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   诊断结果\n   ============================================================ */',
        '/* ============================================================\n   Diagnosis Results\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   通关建议\n   ============================================================ */',
        '/* ============================================================\n   Level Advice\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   隐藏关卡\n   ============================================================ */',
        '/* ============================================================\n   Hidden Level\n   ============================================================ */'
    )
    c = c.replace(
        '/* ============================================================\n   启动\n   ============================================================ */',
        '/* ============================================================\n   Startup\n   ============================================================ */'
    )

    # Dilemma data
    d_translations = [
        ('"想到死亡会觉得害怕，但说不清到底怕的是什么。"', '"Thinking about death scares me, but I can\'t articulate what exactly I\'m afraid of."'),
        ('"总觉得还有什么事没做完，但又说不清是什么。"', '"I always feel there\'s something unfinished, but I can\'t say what."'),
        ('"看着父母老去，第一次意识到：下一个就是我。"', '"Watching my parents grow old, I realized for the first time: I\'m next."'),
        ('"如果今天就是最后一天，我会后悔很多事。"', '"If today were my last day, I\'d regret many things."'),
        ('"担心自己老了以后没人记得。"', '"I worry that when I\'m old, no one will remember me."'),
        ('"不确定自己这一生，到底留下了什么。"', '"I\'m not sure what I\'ve actually left behind in this life."'),
        ('"想写点什么给孩子或后人，但拿起笔又不知道写什么。"', '"I want to write something for my children or descendants, but when I pick up the pen, I don\'t know what to write."'),
        ('"害怕的不是死，是被遗忘。"', '"What I fear isn\'t death — it\'s being forgotten."'),
        ('"有时候觉得：我这辈子好像白活了。"', '"Sometimes I feel: my life has been wasted."'),
        ('"想要某种形式的「不朽」，但又不信宗教。"', '"I want some form of \'immortality,\' but I\'m not religious."'),
        ('"看到新闻里有人突然离世，会想：如果是我呢？"', '"When I see news of someone dying suddenly, I think: what if that were me?"'),
        ('"关于临终、遗嘱、葬礼——完全没想过，也不想想。"', '"End of life, wills, funerals — I\'ve never thought about it, and I don\'t want to."'),
    ]
    for old, new in d_translations:
        c = c.replace(old, new)

    # Adventure cards
    ac_translations = [
        ('"你每天在写自己的墓志铭，你写的是什么？"', '"Every day you\'re writing your own epitaph. What are you writing?"'),
        ('"死亡不是人生的对立面，是人生的一部分。海德格尔说的。"', '"Death isn\'t the opposite of life — it\'s part of life. Heidegger said that."'),
        ('"琼瑶选择自己的告别方式——这不是逃避，是对生命的最后一次掌控。"', '"Qiong Yao chose her own way to say goodbye — this wasn\'t escape, it was the last act of control over her life."'),
        ('"人这辈子会死三次：第一次是断气，第二次是葬礼，第三次是最后一个记得你的人也走了。你在第几次？"', '"A person dies three times: first when they stop breathing, second at the funeral, third when the last person who remembers you passes. Which stage are you at?"'),
        ('"最好的遗产不是钱，是一个让人想起你就微笑的故事。"', '"The best legacy isn\'t money — it\'s a story that makes people smile when they think of you."'),
        ('"写遗书太早，但给重要的人写几句话——刚刚好。"', '"Writing a will is too early, but writing a few words for the people who matter — that\'s just right."'),
        ('"你害怕的不是死亡本身，是你觉得还有很多事没做完。那……哪一件是最重要的？"', '"What you fear isn\'t death itself — it\'s feeling like there\'s still so much unfinished. So... which one matters most?"'),
        ('"有人因为你的存在，生活变好了一点点。这就够了。真的够了。"', '"Someone\'s life got a little better because you existed. That\'s enough. Really enough."'),
        ('"临终关怀里有个发现：临终者最后悔的从来不是『做错了什么』，而是『没做什么』。"', '"A finding from palliative care: what the dying regret most is never \'what I did wrong,\' but \'what I didn\'t do.\'"'),
        ('"数字时代的新问题：你的微信朋友圈、云盘、账号——在你死后会怎样？"', '"A new question of the digital age: what happens to your social media, cloud storage, and accounts after you die?"'),
        ('"你不需要被万人铭记。有几个人真心记得你，就是『不朽』。"', '"You don\'t need to be remembered by millions. A few people who truly remember you — that is \'immortality.\'"'),
        ('"终篇不是终点。你走过的每一步，都在别人生命里留下了脚印——只是你可能不知道。"', '"The final chapter isn\'t the end. Every step you\'ve taken has left footprints in others\' lives — you just may not know it."'),
    ]
    for old, new in ac_translations:
        c = c.replace(old, new)

    # Questions
    q_translations = [
        ('q: "想到『死亡』这件事，你的第一反应是？",', 'q: "What is your first reaction when you think about \'death\'?",'),
        ('{ text: "正常现象，每个人都会死，没什么好怕的。", key: "01平静接纳" },', '{ text: "It\'s normal — everyone dies, nothing to fear.", key: "01平静接纳" },'),
        ('{ text: "不太敢想，一想就觉得不舒服。", key: "02回避思考" },', '{ text: "I don\'t dare think about it — it makes me uncomfortable.", key: "02回避思考" },'),
        ('{ text: "偶尔会想，但想不通就不想了。", key: "03偶有触动" },', '{ text: "I think about it occasionally, but stop when I can\'t figure it out.", key: "03偶有触动" },'),
        ('{ text: "挺害怕的，尤其晚上睡不着的时候。", key: "04明显恐惧" },', '{ text: "Quite scared, especially at night when I can\'t sleep.", key: "04明显恐惧" },'),
        ('{ text: "已经认真想过很多次了，甚至做过一些准备。", key: "05主动面对" },', '{ text: "I\'ve thought about it seriously many times, and even made some preparations.", key: "05主动面对" },'),

        ('q: "如果今天就是你生命的最后一天，你会后悔？",', 'q: "If today were the last day of your life, what would you regret?",'),
        ('{ text: "不会后悔，我对自己的人生基本满意。", key: "06人生无憾" },', '{ text: "No regrets — I\'m basically satisfied with my life.", key: "06人生无憾" },'),
        ('{ text: "有些遗憾，但整体还好。", key: "07略有遗憾" },', '{ text: "Some regrets, but overall it\'s okay.", key: "07略有遗憾" },'),
        ('{ text: "后悔没多陪陪家人。", key: "08亏欠关系" },', '{ text: "I\'d regret not spending more time with family.", key: "08亏欠关系" },'),
        ('{ text: "后悔没有做自己真正想做的事。", key: "09辜负自己" },', '{ text: "I\'d regret not doing what I truly wanted to do.", key: "09辜负自己" },'),
        ('{ text: "不知道——从没认真想过这个问题。", key: "10从未审视" },', '{ text: "I don\'t know — I\'ve never seriously thought about this.", key: "10从未审视" },'),

        ('q: "关于『留下什么』，你现在的想法最接近？",', 'q: "Regarding \'what to leave behind,\' which is closest to your current thinking?",'),
        ('{ text: "希望能给孩子留点物质基础就够了。", key: "11留物质" },', '{ text: "I hope to leave my children some material foundation — that\'s enough.", key: "11留物质" },'),
        ('{ text: "希望别人记住我的为人，记得我是个好人。", key: "12留名声" },', '{ text: "I hope people remember my character — remember me as a good person.", key: "12留名声" },'),
        ('{ text: "希望能留下点什么——作品、思想、或者一段故事。", key: "13留精神" },', '{ text: "I hope to leave something behind — works, ideas, or a story.", key: "13留精神" },'),
        ('{ text: "没想过留什么，顺其自然吧。", key: "14无所谓" },', '{ text: "Haven\'t thought about it — whatever happens, happens.", key: "14无所谓" },'),
        ('{ text: "我觉得自己什么都留不下，有点慌。", key: "15焦虑虚无" },', '{ text: "I feel I can\'t leave anything behind — it makes me anxious.", key: "15焦虑虚无" },'),

        ('q: "关于『被遗忘』这件事，你的感受是？",', 'q: "How do you feel about \'being forgotten\'?",'),
        ('{ text: "被遗忘很正常，几代人之后谁还记得谁。", key: "16接受遗忘" },', '{ text: "Being forgotten is normal — a few generations later, who remembers who?", key: "16接受遗忘" },'),
        ('{ text: "不奢求被很多人记得，家人记得就好。", key: "17小范围即可" },', '{ text: "I don\'t need many to remember me — family remembering is enough.", key: "17小范围即可" },'),
        ('{ text: "希望至少有些人真心记得我，想起我会微笑。", key: "18渴望被记" },', '{ text: "I hope at least some people truly remember me and smile when they think of me.", key: "18渴望被记" },'),
        ('{ text: "害怕被彻底遗忘，那种感觉说不出的孤独。", key: "19恐惧遗忘" },', '{ text: "I fear being completely forgotten — that feeling is an indescribable loneliness.", key: "19恐惧遗忘" },'),
        ('{ text: "与其被人记住，不如活得精彩。", key: "20活在当下" },', '{ text: "Rather than being remembered, I\'d rather live brilliantly.", key: "20活在当下" },'),

        ('q: "关于临终、遗嘱、葬礼这些事，你的状态是？",', 'q: "Regarding end-of-life, wills, and funerals — what is your current state?",'),
        ('{ text: "完全没想过，觉得离我很远。", key: "21从未准备" },', '{ text: "Never thought about it — feels very far away.", key: "21从未准备" },'),
        ('{ text: "偶尔闪过念头，但马上转移注意力。", key: "22有意回避" },', '{ text: "The thought crosses my mind occasionally, but I quickly shift my attention.", key: "22有意回避" },'),
        ('{ text: "想过，但不知道从何开始准备。", key: "23迷茫无助" },', '{ text: "I\'ve thought about it, but don\'t know where to start preparing.", key: "23迷茫无助" },'),
        ('{ text: "已经和家人聊过这个话题了。", key: "24沟通过" },', '{ text: "I\'ve already talked about this with my family.", key: "24沟通过" },'),
        ('{ text: "已经做了基本的安排（遗嘱/保险/意愿书等）。", key: "25有备无患" },', '{ text: "I\'ve made basic arrangements (will/insurance/living will, etc.).", key: "25有备无患" },'),

        ('q: "如果你能知道死后会发生什么，你想知道吗？",', 'q: "If you could know what happens after death, would you want to know?",'),
        ('{ text: "不想知道，活着的事已经够忙了。", key: "26专注今生" },', '{ text: "No — living life is already busy enough.", key: "26专注今生" },'),
        ('{ text: "好奇，但没有特别强烈的愿望。", key: "27温和好奇" },', '{ text: "Curious, but not a strong desire.", key: "27温和好奇" },'),
        ('{ text: "挺想知道的，这困扰我很久了。", key: "28渴望答案" },', '{ text: "I\'d really like to know — this has bothered me for a long time.", key: "28渴望答案" },'),
        ('{ text: "我有自己的信仰，已经有答案了。", key: "29已有信仰" },', '{ text: "I have my own faith and already have an answer.", key: "29已有信仰" },'),
        ('{ text: "我觉得死后什么都没有，所以不想浪费时间想。", key: "30唯物主义" },', '{ text: "I think there\'s nothing after death, so I don\'t want to waste time thinking about it.", key: "30唯物主义" },'),
    ]
    for old, new in q_translations:
        c = c.replace(old, new)

    # cardPoints data
    cp_translations = [
        ('name: "平静接纳",     desc: "你对死亡有平常心，这是智慧的表现。不恐惧不代表不在乎，代表你看清了一个事实。", advice: "保持这份平静，同时用它来提醒自己：正因为生命有限，每一天才更值得好好过。"',
         'name: "Calm Acceptance",     desc: "You have a calm attitude toward death — a sign of wisdom. Not fearing it doesn\'t mean not caring; it means you\'ve seen a truth.", advice: "Keep this calm and let it remind you: because life is finite, every day is worth living well."'),
        ('name: "回避思考",     desc: "你选择不去想死亡这件事。这是一种自我保护机制，但保护太久会变成逃避。", advice: "不需要一下子就想通。试着从一个小的角度开始：如果只剩一年，哪三件事是你一定要做的？"',
         'name: "Avoidance",     desc: "You choose not to think about death. This is a self-protection mechanism, but protection too long becomes avoidance.", advice: "You don\'t need to figure it all out at once. Start small: if you had only one year left, what three things would you absolutely do?"'),
        ('name: "偶有触动",     desc: "死亡的话题会触碰到你，但你还没有深入去想。这是一个好的开始——你没有完全关闭这扇门。", advice: "下次再被触动的时候，不要马上转移注意力。停下来，让那个感觉待一会儿。它可能告诉你一些重要的事。"',
         'name: "Occasionally Moved",     desc: "The topic of death touches you, but you haven\'t thought deeply about it. This is a good start — you haven\'t completely closed the door.", advice: "Next time you\'re moved, don\'t immediately shift your attention. Pause and let the feeling stay a while. It may tell you something important."'),
        ('name: "明显恐惧",     desc: "你对死亡的恐惧已经影响到日常生活了。恐惧本身不是问题，被恐惧支配才是。", advice: "恐惧往往来自未知。试着读一本关于死亡的好书（如《最好的告别》），或者看一部相关电影。了解越多，恐惧越少。"',
         'name: "Overt Fear",     desc: "Your fear of death has begun to affect daily life. Fear itself isn\'t the problem — being controlled by it is.", advice: "Fear often comes from the unknown. Try reading a good book about death (like Being Mortal) or watching a related film. The more you understand, the less you fear."'),
        ('name: "主动面对",     desc: "你已经认真地面对过死亡这个话题了。这需要勇气，而你拥有它。", advice: "把你的经验和思考分享给身边信任的人。你可能比你自己想象的更能帮助那些还在恐惧中的人。"',
         'name: "Proactive Confrontation",     desc: "You\'ve already seriously faced the topic of death. This takes courage, and you have it.", advice: "Share your experience and thoughts with people you trust. You may be able to help those still in fear more than you imagine."'),
        ('name: "人生无憾",     desc: "你对自己的生命基本满意。这是很难得的状态——很多人终其一生都在追逐这种满意度。", advice: "无憾不代表无事可做。问问自己：还有什么小小的愿望没实现？去实现它。不是为了弥补，是为了快乐。"',
         'name: "No Regrets",     desc: "You\'re basically satisfied with your life. This is a rare state — many people spend their whole lives chasing this kind of satisfaction.", advice: "No regrets doesn\'t mean there\'s nothing left to do. Ask yourself: is there a small wish unfulfilled? Go fulfill it. Not to make up for something, but for joy."'),
        ('name: "略有遗憾",     desc: "你有一些遗憾，但不严重。这些遗憾更像是一种温柔的提醒，而不是沉重的负担。", advice: "挑一个最小的遗憾，今天就开始补救。哪怕只是打个电话、写张卡片。行动是最好的解药。"',
         'name: "Slight Regrets",     desc: "You have some regrets, but not serious ones. These regrets are more like gentle reminders than heavy burdens.", advice: "Pick the smallest regret and start making amends today. Even if it\'s just a phone call or writing a card. Action is the best remedy."'),
        ('name: "亏欠关系",     desc: "你最在意的是人际关系中的亏欠——家人、朋友、爱人。这说明你在乎联结。", advice: "不要等『有空』再去陪伴。这周末就去做一件事：和一个你在乎的人，好好吃顿饭、散散步。"',
         'name: "Relational Debt",     desc: "What you care about most is the debt in relationships — family, friends, loved ones. This shows you value connection.", advice: "Don\'t wait until you \'have time\' to be together. This weekend, do one thing: have a nice meal or take a walk with someone you care about."'),
        ('name: "辜负自己",     desc: "你最遗憾的是没有为自己而活。别人的期待、社会的压力，让你走了一条不是自己的路。", advice: "永远不会太晚。问自己一个问题：如果没有人会失望，我今天会做什么？然后去做那件事的一小部分。"',
         'name: "Betrayed Myself",     desc: "Your biggest regret is not living for yourself. Others\' expectations and society\'s pressure led you down a path that wasn\'t yours.", advice: "It\'s never too late. Ask yourself: if no one would be disappointed, what would I do today? Then do a small part of that thing."'),
        ('name: "从未审视",     desc: "你从来没有认真审视过自己的人生。忙碌可能是一种方式，让你不必面对这个问题。", advice: "找个安静的时间，给自己30分钟，什么都不做，只是想一想：我这辈子到目前为止，满意吗？不满意的是什么？"',
         'name: "Never Examined",     desc: "You\'ve never seriously examined your life. Being busy may be a way to avoid facing this question.", advice: "Find a quiet time, give yourself 30 minutes, do nothing — just think: am I satisfied with my life so far? What am I not satisfied with?"'),
        ('name: "留物质",       desc: "你觉得留下物质基础是最重要的遗产。这是很实在的想法，也是大多数人的选择。", advice: "物质重要，但也想想：除了钱，有没有什么东西是无形的却更有价值？比如你教给孩子的道理，或者你帮助过的人。"',
         'name: "Leave Material Things",       desc: "You think leaving a material foundation is the most important legacy. This is a practical thought, and the choice of most people.", advice: "Material things matter, but also think: besides money, is there something intangible yet more valuable? Like lessons you teach your children, or people you\'ve helped."'),
        ('name: "留名声",       desc: "你希望被记住是一个好人。名誉是你看重的遗产形式。", advice: "好名声不是靠经营来的，是靠日积月累的行为。继续保持善良，同时别忘了：做一个好人首先是要对自己也好一点。"',
         'name: "Leave a Good Name",       desc: "You want to be remembered as a good person. Reputation is the legacy form you value.", advice: "A good reputation isn\'t manufactured — it\'s built through consistent actions over time. Keep being kind, and remember: being a good person starts with being good to yourself."'),
        ('name: "留精神",       desc: "你希望留下的是精神层面的东西——作品、思想、故事。这是最高形式的遗产。", advice: "从今天开始记录。写下来、录下来、画下来。你不需要成为作家，你只需要真实地表达自己。这就是遗产。"',
         'name: "Leave a Legacy of Ideas",       desc: "You want to leave something spiritual — works, ideas, stories. This is the highest form of legacy.", advice: "Start recording today. Write it down, record it, draw it. You don\'t need to become a writer — you just need to express yourself authentically. That is legacy."'),
        ('name: "无所谓",       desc: "对『留下什么』你持开放态度。这不是冷漠，是一种豁达。", advice: "豁达很好。但如果有一天你突然很想留下什么，别压抑那个冲动。那可能是你内心在说话。"',
         'name: "Doesn\'t Matter",       desc: "You\'re open-minded about \'what to leave behind.\' This isn\'t indifference — it\'s a kind of openness.", advice: "Being open-minded is great. But if one day you suddenly feel a strong urge to leave something behind, don\'t suppress it. It might be your inner self speaking."'),
        ('name: "焦虑虚无",     desc: "你觉得自己可能什么都留不下，这种焦虑在啃噬你。虚无感是现代人的常见困境。", advice: "焦虑的反面不是确信，是行动。今天做一件小事——帮一个人、写一段话、种一棵树。行动会治愈虚无。"',
         'name: "Anxious Emptiness",     desc: "You feel you might not be able to leave anything behind, and this anxiety is eating at you. Emptiness is a common modern struggle.", advice: "The opposite of anxiety isn\'t certainty — it\'s action. Do one small thing today: help someone, write a paragraph, plant a tree. Action heals emptiness."'),
        ('name: "接受遗忘",     desc: "你能接受被遗忘的事实。这是一种深刻的智慧——承认有限性，才能活得更自由。", advice: "既然接受被遗忘，那就更自由地活。不用为了『被记住』而活——为自己而活，反而更容易被记住。"',
         'name: "Accepts Being Forgotten",     desc: "You can accept the fact of being forgotten. This is a deep wisdom — acknowledging finitude allows you to live more freely.", advice: "Since you accept being forgotten, live more freely. Don\'t live to be remembered — live for yourself, and paradoxically, you\'re more likely to be remembered."'),
        ('name: "小范围即可",   desc: "你不追求被大众铭记，只希望亲近的人记得你。这是温暖而现实的想法。", advice: "那就把精力放在这些人身上。多创造一些共同的回忆——旅行、聊天、一起做事。回忆是最真实的遗产。"',
         'name: "A Small Circle Is Enough",   desc: "You don\'t seek to be remembered by the masses — just by those close to you. This is a warm and realistic thought.", advice: "Then put your energy into those people. Create more shared memories — travel, talk, do things together. Memories are the most real legacy."'),
        ('name: "渴望被记",     desc: "你渴望被记住，被怀念。这不虚荣，是人作为社会性动物的本能需求。", advice: "被记住最好的方式不是刻意留下什么，而是真诚地对待每一个人、做好每一件事。影响力是在不知不觉中留下的。"',
         'name: "Yearning to Be Remembered",     desc: "You yearn to be remembered, to be missed. This isn\'t vanity — it\'s the instinctive need of a social being.", advice: "The best way to be remembered isn\'t to deliberately leave something behind, but to treat every person sincerely and do every task well. Influence is left without you noticing."'),
        ('name: "恐惧遗忘",     desc: "你害怕被彻底遗忘，这种恐惧背后是对意义的渴望。", advice: "与其担心被遗忘，不如想想：你现在做的哪些事可能在别人生命中留下痕迹？继续做那些事，就是对抗遗忘的方式。"',
         'name: "Fear of Being Forgotten",     desc: "You fear being completely forgotten. Behind this fear is a yearning for meaning.", advice: "Instead of worrying about being forgotten, think: which things you\'re doing now might leave traces in others\' lives? Keep doing those things — that\'s how you fight being forgotten."'),
        ('name: "活在当下",     desc: "你选择了活在当下，而非担忧身后名。这是一种有力量的生活态度。", advice: "保持。同时允许自己在某些时刻回望一下——不是纠结过去，而是确认自己走在想走的路上。"',
         'name: "Living in the Present",     desc: "You chose to live in the present rather than worry about your legacy. This is a powerful life attitude.", advice: "Keep it up. Also allow yourself to look back sometimes — not to dwell on the past, but to confirm you\'re on the path you want to walk."'),
        ('name: "从未准备",     desc: "你完全没有为『终点』做准备。大多数人都是这样——直到生活逼着你去想。", advice: "不需要马上立遗嘱。先做一件最小的事：打开手机备忘录，写下『如果我出事了，我希望家人知道的3件事』。这就够了，真的。"',
         'name: "Never Prepared",     desc: "You haven\'t prepared at all for the \'end.\' Most people are like this — until life forces you to think about it.", advice: "You don\'t need to write a will right away. Start with the smallest thing: open your phone\'s notes app and write \'If something happens to me, here are 3 things I want my family to know.\' That\'s enough. Really."'),
        ('name: "有意回避",     desc: "你有意识地避开这类话题。回避的背后通常是恐惧或不安。", advice: "找一个安全的方式来开始：看一部关于临终的电影（推荐《寻梦环游记》），和家人聊聊『如果』。从小处入手，没那么可怕。"',
         'name: "Intentional Avoidance",     desc: "You consciously avoid these topics. Behind avoidance is usually fear or unease.", advice: "Find a safe way to start: watch a movie about end of life (recommend Coco), talk with family about \'what if.\' Start small — it\'s not so scary."'),
        ('name: "迷茫无助",     desc: "你想做准备，但不知道怎么开始。这种迷茫很正常——学校从来不教这个。", advice: "从最实用的开始：查一下『生前预嘱』是什么，了解一下遗嘱的基本类型。知识本身就是一种力量。知道了就不怕了。"',
         'name: "Lost and Helpless",     desc: "You want to prepare, but don\'t know how to start. This confusion is normal — schools never teach this.", advice: "Start with the most practical: look up what a \'living will\' is, learn the basic types of wills. Knowledge itself is power. Once you know, you won\'t be afraid."'),
        ('name: "沟通过",       desc: "你和家人聊过这个话题了。这在华人社会中非常难得——大多数人连提都不敢提。", advice: "沟通是一次性的，但话题可以持续。定期更新彼此的想法，确保你们的理解和期望保持一致。"',
         'name: "Had the Conversation",       desc: "You\'ve talked about this with your family. This is very rare — most people don\'t even dare bring it up.", advice: "The conversation is a one-time event, but the topic can continue. Regularly update each other\'s thoughts to ensure your understanding and expectations stay aligned."'),
        ('name: "有备无患",     desc: "你已经做了基本的安排。这不仅是对自己负责，也是对家人的爱——你为他们省去了很多麻烦。", advice: "定期检查和更新你的安排。人生在变，安排也需要跟上变化。每两年review一次是个好习惯。"',
         'name: "Prepared and Ready",     desc: "You\'ve made basic arrangements. This isn\'t just responsibility to yourself — it\'s love for your family. You\'ve saved them a lot of trouble.", advice: "Review and update your arrangements regularly. Life changes, and your plans need to keep up. Reviewing every two years is a good habit."'),
        ('name: "专注今生",     desc: "你选择专注于当下的生活。这是务实的态度，也是很多人的选择。", advice: "专注今生不代表不能思考这个问题。偶尔停下来想一想，可能会让你更珍惜现在所拥有的。"',
         'name: "Focused on This Life",     desc: "You choose to focus on the present life. This is a pragmatic attitude, and the choice of many.", advice: "Focusing on this life doesn\'t mean you can\'t think about this question. Occasionally pausing to reflect may help you cherish what you have now."'),
        ('name: "温和好奇",     desc: "你对死后世界有适度的好奇心。这种开放的心态很好——既不信也不排斥。", advice: "保持好奇。可以读一些不同文化对这个问题的回答——不一定要接受任何一种，但多元视角会让你看得更清楚。"',
         'name: "Gentle Curiosity",     desc: "You have moderate curiosity about the afterlife. This open mindset is good — neither believing nor rejecting.", advice: "Stay curious. Read how different cultures answer this question — you don\'t have to accept any of them, but diverse perspectives help you see more clearly."'),
        ('name: "渴望答案",     desc: "你很想知道死后会发生什么。这个困惑可能在某些夜晚特别强烈。", advice: "与其寻找一个确定的答案，不如接受『没人知道』这个事实本身。各种宗教和哲学给出了不同的可能性，都可以参考，但都不必当成真理。"',
         'name: "Craving Answers",     desc: "You really want to know what happens after death. This question may be especially intense on certain nights.", advice: "Rather than seeking a definitive answer, accept the fact that \'nobody knows.\' Various religions and philosophies offer different possibilities — all worth considering, none need be taken as absolute truth."'),
        ('name: "已有信仰",     desc: "你有自己的信仰体系来回答这个问题。信仰给人安慰和方向。", advice: "信仰是个人选择。同时保持开放：别人的信仰和你不同，不代表你们不能互相尊重。终极问题上，谦卑比正确更重要。"',
         'name: "Has Faith",     desc: "You have your own belief system to answer this question. Faith gives comfort and direction.", advice: "Faith is a personal choice. Stay open: others having different beliefs doesn\'t mean you can\'t respect each other. On ultimate questions, humility matters more than being right."'),
        ('name: "唯物主义",     desc: "你认为死后什么都没有。这是理性且诚实的立场。", advice: "唯物主义不等于虚无主义。正因为只有这一次生命，每一刻才更加珍贵。用『只有一次』来驱动自己，而不是用来否定意义。"',
         'name: "Materialist",     desc: "You believe there\'s nothing after death. This is a rational and honest position.", advice: "Materialism isn\'t nihilism. Precisely because there\'s only this one life, every moment is more precious. Use \'only once\' to drive yourself, not to deny meaning."'),
    ]
    for old, new in cp_translations:
        c = c.replace(old, new)

    # Easter eggs
    c = c.replace(
        'title: "海德格尔 · 向死而生", text: "德国哲学家海德格尔说：人是唯一知道自己会死的生物。正因为我们知道生命有限，才有了『紧迫感』去真正地活。死亡不是人生的对立面，它赋予人生意义。"',
        'title: "Heidegger · Being-Toward-Death", text: "German philosopher Heidegger said: humans are the only beings that know they will die. Because we know life is finite, we have the urgency to truly live. Death isn\'t the opposite of life — it gives life meaning."'
    )
    c = c.replace(
        'title: "琼瑶的告别", text: "2024年，台湾作家琼瑶以自己的方式选择告别。她在遗书中写道：『我不想听天由命，我想自己做主。』——这不是放弃生命，而是对生命最后的主权宣告。她引发了全社会对『善终权利』的讨论。"',
        'title: "Qiong Yao\'s Farewell", text: "In 2024, Taiwanese writer Qiong Yao chose to say goodbye in her own way. In her letter she wrote: \'I don\'t want to leave it to fate — I want to be in charge.\' This wasn\'t giving up life — it was the last declaration of sovereignty over her life. She sparked a nationwide discussion about the right to a good death."'
    )
    c = c.replace(
        'title: "数字遗产", text: "你死后，微信怎么办？云盘里的照片呢？游戏账号？社交媒体？数字时代带来了新问题：人在物理世界中消失，但在数字空间里『活着』。有人开始设立『数字 executor（执行人）』——你考虑过吗？"',
        'title: "Digital Legacy", text: "After you die, what happens to your social media? Your photos in the cloud? Your game accounts? The digital age brings new questions: a person disappears from the physical world but remains \'alive\' in digital space. Some people have started appointing \'digital executors\' — have you considered it?"'
    )
    c = c.replace(
        'title: "世界的死亡地图", text: "藏人有天葬，认为身体最后的价值是供养万物；墨西哥有亡灵节（Dia de los Muertos），用色彩和音乐庆祝逝者；埃及人做木乃伊等待复活；日本有佛事传统……每种文化都在用自己的方式回答同一个问题。没有标准答案，但每一种都值得尊重。"',
        'title: "The World\'s Map of Death", text: "Tibetans practice sky burial, believing the body\'s final value is nourishing all living things; Mexico has Día de los Muertos, celebrating the departed with color and music; Egyptians made mummies awaiting resurrection; Japan has Buddhist memorial traditions... Every culture answers the same question in its own way. There\'s no standard answer, but each one deserves respect."'
    )

    # JS function strings
    c = c.replace("'点击卡牌翻开'", "'Tap the card to reveal'")
    c = c.replace("'— 这张卡，陪你去诊断 —'", "'— This card accompanies you to the diagnosis —'")
    c = c.replace("`第${currentQuestion + 1}题`", "`Question ${currentQuestion + 1}`")
    c = c.replace("'继续' : '查看结果'", "'Continue' : 'View Results'")
    c = c.replace("alert('先写点什么吧，至少说一件你卡住的事。');", "alert('Please write something first — at least one thing you\'re stuck on.');")
    c = c.replace("`第${['一','二','三','四'][i]}步：${t}`", "`Step ${['One','Two','Three','Four'][i]}: ${t}`")

    # Result summary texts
    c = c.replace(
        '`你最核心的卡点是「${topKey ? topKey.name : \'\'}」。其他的，是这个卡点的延伸。`',
        '`Your core block is \'${topKey ? topKey.name : \'Unknown\'}\'. The rest are extensions of this block.`'
    )
    c = c.replace(
        '`你有 ${sorted.filter(s => s[1] >= 2).length} 个较深的卡点，它们相互关联，互为表里。`',
        '`You have ${sorted.filter(s => s[1] >= 2).length} deeper blocks that are interconnected.`'
    )
    c = c.replace(
        '`你走过的每一步都在写你的故事——今天，你读到了其中一页。`',
        '`Every step you\'ve taken writes your story — today, you read one page of it.`'
    )

    # Result card score text
    c = c.replace('命中 ${score} 次', 'matched ${score} times')

    # Advice card label
    c = c.replace("'卡点 '", "'Block '")

    # Hidden level responses
    c = c.replace(
        '"你写的这些，说明你已经在面对了。光是在心里把它说清楚，就已经是改变的开始。"',
        '"What you\'ve written shows you\'re already facing it. Just putting it into words is the beginning of change."'
    )
    c = c.replace(
        '"困境不是一天形成的，解开它也不需要一天。你已经走出了第一步。"',
        '"Blocks didn\'t form in a day, and they don\'t need a day to unravel. You\'ve already taken the first step."'
    )
    c = c.replace(
        '"你说出口的那些，是很多人不敢面对的。你的勇气，比你自己知道的要大。"',
        '"What you\'ve put into words is what many people dare not face. Your courage is greater than you know."'
    )
    c = c.replace(
        '"不是所有人都愿意把这些写下来。你做了。光是这一步，就已经很不容易。"',
        '"Not everyone is willing to write these things down. You did. That step alone is remarkable."'
    )

    # Hidden level action text
    c = c.replace(
        "`今天先做这一件事：${h4.split('，')[0].split('。')[0]}`",
        "`Start with this one thing today: ${h4.split(',')[0].split('.')[0]}`"
    )
    c = c.replace(
        "'今天，就做一件事：给你的身体一个信号——我听到你了。'",
        "'Today, do just one thing: send your body a signal — I hear you.'"
    )

    # Download card canvas text
    c = c.replace("ctx.fillText('我的隐藏关卡', 300, 80);", "ctx.fillText('My Hidden Level', 300, 80);")
    c = c.replace("ctx.fillText('第十二关 · 终篇传承 · 找到啦', 300, 108);", "ctx.fillText('Stage 12 · Legacy & Passing On · Found It', 300, 108);")
    c = c.replace("ctx.fillText('— 第十二关 · 终篇传承 · 找到啦 —', 300, 750);", "ctx.fillText('— Stage 12 · Legacy & Passing On · Found It —', 300, 750);")
    c = c.replace("link.download = '我的隐藏关卡.png';", "link.download = 'my-hidden-level.png';")

    # Visitor counter
    c = c.replace('您是第', 'You are visitor #')
    c = c.replace('位访客', '')

    # renderDilemma function
    c = c.replace('困境 ${String(d.id).padStart(2,\'0\')}', 'Dilemma ${String(d.id).padStart(2,\'0\')}')

    # Also fix the hover quote in the flip card front
    c = c.replace(
        '"写遗书太早，写人生回顾刚刚好。"',
        '"Too early to write a will, but just right for a life review."'
    )

    # Also handle remaining Chinese in dilemma card rendering
    c = c.replace(
        '困境 ${String(d.id).padStart(2,\'0\')}',
        'Dilemma ${String(d.id).padStart(2,\'0\')}'
    )

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)
    print("  Done: 第十二关-终篇传承.html")


# ============================================================
# File 11: 第十一关-健康与衰老.html (mostly translated, needs remaining Chinese)
# ============================================================
def translate_file11():
    print("Translating 第十一关-健康与衰老.html ...")
    fp = os.path.join(BASE, '第十一关-健康与衰老.html')
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()

    # Remaining level badge text
    c = c.replace('第十一关 · 健康与aging', 'Level 11 · Health & Aging')

    # Flip card quote
    c = c.replace(
        '"身体是一本连续写了几十年的日记，翻开来，全是线索。"',
        '"Your body is a diary written over decades. Open it, and every page is a clue."'
    )

    # JS function strings
    c = c.replace("'点击卡牌翻开'", "'Tap the card to reveal'")
    c = c.replace("困境 ${String(d.id).padStart(2,'0')}", "Dilemma ${String(d.id).padStart(2,'0')}")

    # Question num
    c = c.replace("`第${currentQuestion + 1}题`", "`Question ${currentQuestion + 1}`")
    c = c.replace("'继续' : '查看结果'", "'Continue' : 'View Results'")

    # Result summary texts
    c = c.replace(
        '`你最核心的卡点是「${topKey ? topKey.name : \'\'}」。其他的，是这个卡点的延伸。`',
        '`Your core block is \'${topKey ? topKey.name : \'Unknown\'}\'. The rest are extensions of this block.`'
    )
    c = c.replace(
        '`你有 ${sorted.filter(s => s[1] >= 2).length} 个较深的卡点，它们相互关联，互为表里。`',
        '`You have ${sorted.filter(s => s[1] >= 2).length} deeper blocks that are interconnected.`'
    )
    c = c.replace(
        '`身体是一本连续写了几十年的日记，读懂它，比任何养生经都重要。`',
        '`Your body is a diary written over decades. Reading it matters more than any health advice.`'
    )

    # Result card score
    c = c.replace('matched ${score} times', 'matched ${score} times')  # already English

    # Advice card label
    c = c.replace("'卡点 '", "'Block '")

    # Advice section badge (already fixed above with bulk replace)

    # Download card text
    c = c.replace("ctx.fillText('我的隐藏关卡', 300, 80);", "ctx.fillText('My Hidden Level', 300, 80);")
    c = c.replace("ctx.fillText('第十一关 · 健康与aging · 找到啦', 300, 108);", "ctx.fillText('Level 11 · Health & Aging · Found It', 300, 108);")
    c = c.replace("ctx.fillText('— 第十一关 · 健康与aging · 找到啦 —', 300, 750);", "ctx.fillText('— Level 11 · Health & Aging · Found It —', 300, 750);")
    c = c.replace("link.download = '我的隐藏关卡.png';", "link.download = 'my-hidden-level.png';")

    # Step labels - check for remaining Chinese
    c = c.replace("Step ${['一','二','三','四'][i]}", "Step ${['One','Two','Three','Four'][i]}")

    # Hidden level action text
    c = c.replace(
        "`今天先做这一件事：${h4.split('，')[0].split('。')[0]}`",
        "`Start with this one thing today: ${h4.split(',')[0].split('.')[0]}`"
    )
    c = c.replace(
        "'今天，就做一件事：给你的身体一个信号——我听到你了。'",
        "'Today, do just one thing: send your body a signal — I hear you.'"
    )

    # Hidden level responses (mixed Chinese/English)
    c = c.replace(
        '"困境Knowing doesn\'t mean 一天形成的，解开它也不需要一天。你已经走出了第一步。"',
        '"Blocks didn\'t form in a day, and they don\'t need a day to unravel. You\'ve already taken the first step."'
    )
    c = c.replace(
        '"你说出口的那些，是很多人不敢面对的。你的勇气，比你自己knowing的要大。"',
        '"What you\'ve put into words is what many people dare not face. Your courage is greater than you know."'
    )
    c = c.replace(
        '"Knowing doesn\'t mean 所有人都愿意把这些写下来。你做了。光是这一步，就已经很不容易。"',
        '"Not everyone is willing to write these things down. You did. That step alone is remarkable."'
    )

    # Card points with mixed Chinese/English
    # These have "aging" mixed with Chinese
    cp_fixes = [
        ('name: "接纳aging"', 'name: "Accepts Aging"'),
        ('desc: "Your first feeling about aging有平常心，这是成熟的表现。aging不可怕，怕的是抗拒。"',
         'desc: "Your first reaction to aging shows equanimity — a sign of maturity. Aging isn\'t scary; what\'s scary is resisting it."'),
        ('name: "Mild Concern"', 'name: "Mild Concern"'),  # already English
        ('desc: "Your first feeling about aging有些担心，但还没有被恐惧支配。这种担忧是有益的——它提醒你做点什么。"',
         'desc: "You feel some concern about aging, but aren\'t controlled by fear. This worry is helpful — it reminds you to do something."'),
        ('"把担忧转化为行动：开始关注自己的饮食、睡眠 and 运动。担心本身不解决问题，行动才解决。"',
         '"Turn worry into action: start paying attention to your diet, sleep, and exercise. Worry itself doesn\'t solve problems — action does."'),
        ('name: "Avoidant Fear"', 'name: "Avoidant Fear"'),  # already English
        ('desc: "Your first feeling about aging有恐惧，而且选择了回避。恐惧本身是正常的，但回避会让你错过预防的机会。"',
         'desc: "You feel fear about aging, and you chose to avoid it. Fear itself is normal, but avoidance makes you miss chances for prevention."'),
        ('name: "Quality Sleep"', 'name: "Quality Sleep"'),  # already
        ('desc: "你能睡个好觉，这是很大的福气。睡眠是最好的抗aging药，也是最好的补药。"',
         'desc: "You can sleep well — that\'s a great blessing. Sleep is the best anti-aging medicine and the best tonic."'),
        ('desc: "睡前2小时避免咖啡、浓茶 and 剧烈运动。给自己建立一个『sleep ritual』：: wash up, lights off, soft music."',
         'desc: "Avoid coffee, strong tea, and vigorous exercise 2 hours before bed. Build yourself a sleep ritual: wash up, lights off, soft music."'),
        ('name: "Aware But Inactive"', 'name: "Aware But Inactive"'),
        ('desc: "你knowing运动重要，但还没真正动起来。知识 and 行动之间，隔着一道鸿沟。"',
         'desc: "You know exercise is important, but haven\'t really started. Between knowledge and action lies a gap."'),
        ('name: "Knowing Not Doing"', 'name: "Knowing Not Doing"'),
        ('"Knowing doesn\'t mean 『knowing』 means 『doing』。找一个人陪你一起运动，或者找一个目标——有人陪、有目标，才能坚持。"',
         '"Knowing doesn\'t mean doing. Find someone to exercise with, or find a goal — companionship and goals help you persist."'),
        ('name: "Physical Limitations"', 'name: "Physical Limitations"'),
        ('desc: "你的身体状况确实限制了你运动的能力。这Knowing doesn\'t mean 你的问题，接受它，然后找到适合你的方式。"',
         'desc: "Your physical condition does limit your ability to exercise. This isn\'t your fault — accept it, then find what works for you."'),
        ('"即使不能剧烈运动，也可以做柔 and 的运动：散步、太极、拉伸、游泳。关键是动起来，Knowing doesn\'t mean 动得多猛。"',
         '"Even if you can\'t do vigorous exercise, you can do gentle exercise: walking, tai chi, stretching, swimming. The key is to move, not how intensely."'),
        ('name: "Optimistic Mindset"', 'name: "Optimistic Mindset"'),
        ('desc: "Your first feeling about 健康没有特别的担忧，这是好事。但乐观不应该变成大意。"',
         'desc: "You have no particular worries about your health — that\'s good. But optimism shouldn\'t become carelessness."'),
        ('desc: "你担心Chronic diseases (blood pressure, blood sugar, etc.).这是最常见的健康威胁，也是最可控的。"',
         'desc: "You worry about chronic diseases (blood pressure, blood sugar, etc.). These are the most common health threats, and also the most controllable."'),
        ('"慢性病管理，靠的是生活习惯，Knowing doesn\'t mean 靠感觉。控制饮食、增加运动、遵医嘱吃药，三管齐下，可以 and 慢性病 and 平共处。"',
         '"Managing chronic disease relies on lifestyle habits, not feelings. Control diet, increase exercise, take prescribed medication — all three together can help you coexist peacefully with chronic disease."'),
        ('desc: "Your first feeling about 重大疾病有恐惧。这个恐惧是合理的——但过度恐惧会影响生活质量。"',
         'desc: "You feel fear about major diseases. This fear is reasonable — but excessive fear affects quality of life."'),
        ('desc: "你担心No one to care for me when old.这是很多人不敢说出口的恐惧。"',
         'desc: "You worry about having no one to care for you when old. This is a fear many people don\'t dare voice."'),
        ('desc: "你担心Cognitive decline (dementia).这个恐惧越来越普遍——因为我们都看到了身边人的例子。"',
         'desc: "You worry about cognitive decline (dementia). This fear is increasingly common — because we\'ve all seen examples close to us."'),
        ('name: "精spirit充实"', 'name: "Fulfilled Spirit"'),
        ('desc: "你的精spirit状态很好，有奔头。这是最难得的——很多人有钱有闲，但没有奔头。"',
         'desc: "Your spirit is fulfilled with purpose. This is rare — many people have money and time, but no sense of direction."'),
        ('"继续保持。同时注意身体：精spirit充实的人容易透支身体，觉得自己还行。别忘了，你Knowing doesn\'t mean 铁打的。"',
         '"Keep it up. Also watch your body: people with fulfilled spirits tend to overdraw their physical health. Don\'t forget, you\'re not made of iron."'),
        ('desc: "你的精spirit状态基本安稳，不算充实但也不迷茫。这是最常见的状态。"',
         'desc: "Your spirit is basically settled — not fulfilled, but not lost either. This is the most common state."'),
        ('name: "精spirit平淡"', 'name: "Flat Spirit"'),
        ('desc: "你A bit lost, nothing particular I want to do.这种平淡，是很多中年人的真实写照。"',
         'desc: "You feel a bit lost with nothing particular you want to do. This flatness is a true portrait of many middle-aged people."'),
        ('"平淡的反面Knowing doesn\'t mean 轰轰烈烈，是『meaning』。找一个你能帮到的人、做一件你觉得有价值的小事——meaning，会慢慢回来的。"',
         '"The opposite of flatness isn\'t excitement — it\'s meaning. Find someone you can help, do one small thing you find valuable — meaning will gradually return."'),
        ('name: "Body-Mind Exhaustion"', 'name: "Body-Mind Exhaustion"'),
        ('desc: "你经常觉得累，不只是身体累，是心累。这种疲惫，是身体 and 心理的双重警报。"',
         'desc: "You often feel tired — not just physically, but mentally. This exhaustion is a dual alarm from body and mind."'),
        ('"先停下来。Knowing doesn\'t mean 等有时间了再休息，是现在就休息。哪怕每天15分钟的放空，也比硬撑强。你的身体在求救。"',
         '"Stop first. Don\'t wait until you have time to rest — rest now. Even 15 minutes of mental blankness per day is better than pushing through. Your body is crying for help."'),
        ('desc: "你Often feel life is pointless.这Knowing doesn\'t mean 小问题——如果这个感觉持续超过两周，需要认真对待。"',
         'desc: "You often feel life is pointless. This isn\'t a small problem — if this feeling persists for more than two weeks, it needs serious attention."'),
        ('"先排除抑郁症的可能。如果是抑郁症，寻求专业帮助；如果Knowing doesn\'t mean ，那意味着你的生活需要调整——加意义，减消耗，增联结。"',
         '"First rule out depression. If it\'s depression, seek professional help; if not, it means your life needs adjustment — add meaning, reduce drain, increase connection."'),
    ]
    for old, new in cp_fixes:
        c = c.replace(old, new)

    # Question 5 - mixed Chinese
    c = c.replace(
        'q: "Your first feeling about 自己健康最大的担心是？",',
        'q: "What is your biggest health concern?",'
    )

    # Question 6 - Chinese
    c = c.replace(
        'q: "你现在的精spirit状态，最接近哪一种？",',
        'q: "Which best describes your current spiritual state?",'
    )

    # Question options with mixed Chinese
    c = c.replace('睡得不错，醒来精spirit好。', 'Sleep well, wake up feeling great.')
    c = c.replace('经常睡不好，第二天精spirit差。', 'Often sleep poorly, feel drained the next day.')

    # Option keys with "精神"
    c = c.replace('"26精spirit充实"', '"26SpiritFulfilled"')
    c = c.replace('"27基本安定"', '"27BasicallySettled"')
    c = c.replace('"28精spirit平淡"', '"28SpiritFlat"')
    c = c.replace('"29身心疲惫"', '"29BodyMindExhausted"')
    c = c.replace('"30存在空虚"', '"30ExistentialEmptiness"')

    # Also fix the card points keys
    c = c.replace('"26精spirit充实":', '"26SpiritFulfilled":')
    c = c.replace('"27基本安定":', '"27BasicallySettled":')
    c = c.replace('"28精spirit平淡":', '"28SpiritFlat":')
    c = c.replace('"29身心疲惫":', '"29BodyMindExhausted":')
    c = c.replace('"30存在空虚":', '"30ExistentialEmptiness":')

    # Question option texts
    c = c.replace('"01精力充沛"', '"01Energetic"')
    c = c.replace('"02基本正常"', '"02BasicallyNormal"')
    c = c.replace('"03轻度疲劳"', '"03MildFatigue"')
    c = c.replace('"04中度疲劳"', '"04ModerateFatigue"')
    c = c.replace('"05严重疲劳"', '"05SevereFatigue"')
    c = c.replace('"06接纳aging"', '"06AcceptAging"')
    c = c.replace('"07轻度担忧"', '"07MildConcern"')
    c = c.replace('"08主动应对"', '"08ProactiveApproach"')
    c = c.replace('"09回避恐惧"', '"09AvoidantFear"')
    c = c.replace('"10现实接受"', '"10RealityAccepted"')
    c = c.replace('"11睡眠优质"', '"11QualitySleep"')
    c = c.replace('"12睡眠尚可"', '"12DecentSleep"')
    c = c.replace('"13睡眠问题"', '"13SleepProblems"')
    c = c.replace('"14严重失眠"', '"14SevereInsomnia"')
    c = c.replace('"15药物依赖"', '"15MedicationDependent"')
    c = c.replace('"16规律运动"', '"16RegularExercise"')
    c = c.replace('"17意识清醒"', '"17AwareButInactive"')
    c = c.replace('"18知行不一"', '"18KnowingNotDoing"')
    c = c.replace('"19客观限制"', '"19PhysicalLimitations"')
    c = c.replace('"20无动意愿"', '"20NoMotivation"')
    c = c.replace('"21心态乐观"', '"21OptimisticMindset"')
    c = c.replace('"22慢性病风险"', '"22ChronicDiseaseRisk"')
    c = c.replace('"23重病恐惧"', '"23MajorDiseaseFear"')
    c = c.replace('"24老年焦虑"', '"24OldAgeAnxiety"')
    c = c.replace('"25认知衰退"', '"25CognitiveDecline"')

    # Also fix cardPoints keys
    for key_pair in [
        ('"01精力充沛":', '"01Energetic":'),
        ('"02基本正常":', '"02BasicallyNormal":'),
        ('"03轻度疲劳":', '"03MildFatigue":'),
        ('"04中度疲劳":', '"04ModerateFatigue":'),
        ('"05严重疲劳":', '"05SevereFatigue":'),
        ('"06接纳aging":', '"06AcceptAging":'),
        ('"07轻度担忧":', '"07MildConcern":'),
        ('"08主动应对":', '"08ProactiveApproach":'),
        ('"09回避恐惧":', '"09AvoidantFear":'),
        ('"10现实接受":', '"10RealityAccepted":'),
        ('"11睡眠优质":', '"11QualitySleep":'),
        ('"12睡眠尚可":', '"12DecentSleep":'),
        ('"13睡眠问题":', '"13SleepProblems":'),
        ('"14严重失眠":', '"14SevereInsomnia":'),
        ('"15药物依赖":', '"15MedicationDependent":'),
        ('"16规律运动":', '"16RegularExercise":'),
        ('"17意识清醒":', '"17AwareButInactive":'),
        ('"18知行不一":', '"18KnowingNotDoing":'),
        ('"19客观限制":', '"19PhysicalLimitations":'),
        ('"20无动意愿":', '"20NoMotivation":'),
        ('"21心态乐观":', '"21OptimisticMindset":'),
        ('"22慢性病风险":', '"22ChronicDiseaseRisk":'),
        ('"23重病恐惧":', '"23MajorDiseaseFear":'),
        ('"24老年焦虑":', '"24OldAgeAnxiety":'),
        ('"25认知衰退":', '"25CognitiveDecline":'),
    ]:
        c = c.replace(key_pair[0], key_pair[1])

    # Easter eggs
    c = c.replace(
        'title: "Huangdi Neijing · Ancient Truths", text: "The Yellow Emperor asked Qi Bo: why could people in ancient times live to 100 without decline? Qi Bo answered: 『"Eat and drink in moderation, maintain regular routines, avoid overexertion." 』——Wellness advice from two thousand years ago that still works today."',
        'title: "Huangdi Neijing · Ancient Truths", text: "The Yellow Emperor asked Qi Bo: why could people in ancient times live to 100 without decline? Qi Bo answered: \'Eat and drink in moderation, maintain regular routines, avoid overexertion.\' Wellness advice from two thousand years ago that still works today."'
    )
    c = c.replace(
        'title: "Harvard 75-Year Study", text: "哈佛大学追踪了724人75年，结论是：决定一个人健康 and 幸福的，Knowing doesn\'t mean 财富、Knowing doesn\'t mean 成就，而是——良好的人际关系。孤独，是健康最大的杀手。"',
        'title: "Harvard 75-Year Study", text: "Harvard tracked 724 people for 75 years. The conclusion: what determines a person\'s health and happiness isn\'t wealth or achievement — it\'s good relationships. Loneliness is the biggest killer of health."'
    )
    c = c.replace(
        'title: "spirit经可塑性", text: "大脑在你的一生中都在改变。每一次学习、每一次思考、每一次运动，都在重塑你的spirit经网络。60岁学画、70岁学琴，不晚——你的大脑还在等你给它惊喜。"',
        'title: "Neuroplasticity", text: "Your brain changes throughout your entire life. Every time you learn, think, or exercise, you reshape your neural networks. Learning to paint at 60, learning piano at 70 — it\'s not too late. Your brain is still waiting for you to surprise it."'
    )
    c = c.replace(
        'title: "The Telomere Effect", text: "诺贝尔奖得主布莱克本发现：决定你aging速度的，是端粒的长度。而保护端粒最好的方法，是：减少慢性压力、保持乐观、适度运动、良好睡眠。"',
        'title: "The Telomere Effect", text: "Nobel laureate Elizabeth Blackburn discovered: what determines your aging speed is telomere length. The best way to protect telomeres: reduce chronic stress, stay optimistic, exercise moderately, sleep well."'
    )

    # Alert text
    c = c.replace("alert('Please write something first — at least one thing you're stuck on.');", "alert('Please write something first — at least one thing you're stuck on.');")

    # Step labels in hidden level - check for remaining Chinese
    # These should already be English

    # Hidden level action
    c = c.replace(
        "`今天先做这一件事：${h4.split('，')[0].split('。')[0]}`",
        "`Start with this one thing today: ${h4.split(',')[0].split('.')[0]}`"
    )
    c = c.replace(
        "'Today, do just one thing: send your body a signal — I hear you.'",
        "'Today, do just one thing: send your body a signal — I hear you.'"
    )

    # renderDilemma
    c = c.replace("困境 ${String(d.id).padStart(2,'0')}", "Dilemma ${String(d.id).padStart(2,'0')}")

    # Visitor counter
    c = c.replace('您是第', 'You are visitor #')
    c = c.replace('位访客', '')

    # JS comments
    c = c.replace('   数据\n', '   Data\n')
    c = c.replace('// 困境选择\n', '// Dilemma Selection\n')
    c = c.replace('   页面导航\n', '   Page Navigation\n')
    c = c.replace('   冒险卡\n', '   Adventure Card\n')
    c = c.replace('   诊断题\n', '   Diagnostic Questions\n')
    c = c.replace('   诊断结果\n', '   Diagnosis Results\n')
    c = c.replace('   通关建议\n', '   Level Advice\n')
    c = c.replace('   隐藏关卡\n', '   Hidden Level\n')
    c = c.replace('   启动\n', '   Startup\n')
    c = c.replace('   状态\n', '   State\n')

    # Option text in Q5
    c = c.replace('"Chronic diseases (blood pressure, blood sugar, etc.)."', '"Chronic diseases (blood pressure, blood sugar, etc.)."')

    # Q6 option keys that reference 精神
    c = c.replace('{ text: "Fulfilled, with purpose.", key: "26精spirit充实" }', '{ text: "Fulfilled, with purpose.", key: "26SpiritFulfilled" }')
    c = c.replace('{ text: "Ordinary, but stable.", key: "27基本安定" }', '{ text: "Ordinary, but stable.", key: "27BasicallySettled" }')
    c = c.replace('{ text: "A bit lost, nothing particular I want to do.", key: "28精spirit平淡" }', '{ text: "A bit lost, nothing particular I want to do.", key: "28SpiritFlat" }')
    c = c.replace('{ text: "Tired, but don\'t know why.", key: "29身心疲惫" }', '{ text: "Tired, but don\'t know why.", key: "29BodyMindExhausted" }')
    c = c.replace('{ text: "Often feel life is pointless.", key: "30存在空虚" }', '{ text: "Often feel life is pointless.", key: "30ExistentialEmptiness" }')

    # Step labels in generateCard
    c = c.replace("Step ${['一','二','三','四'][i]}", "Step ${['One','Two','Three','Four'][i]}")

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)
    print("  Done: 第十一关-健康与衰老.html")


# ============================================================
# File 5: 第五关-婚恋家庭.html (mostly translated, needs remaining Chinese)
# ============================================================
def translate_file5():
    print("Translating 第五关-婚恋家庭.html ...")
    fp = os.path.join(BASE, '第五关-婚恋家庭.html')
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()

    # Since this file is already mostly translated, let me search for remaining Chinese
    # The file content was truncated in the read_file output, so I need to check what's remaining

    # Visitor counter
    c = c.replace('您是第', 'You are visitor #')
    c = c.replace('位访客', '')

    # CSS comments that might be in Chinese
    c = c.replace('/* ==================== 基础变量（与前几关保持一致）==================== */',
                  '/* ==================== Base Variables (consistent with previous levels) ==================== */')
    c = c.replace('/* ==================== 全局 ==================== */',
                  '/* ==================== Global ==================== */')

    # HTML comments
    c = c.replace('<!-- enhance: 滚动淡入 + 回到顶部 -->', '<!-- enhance: scroll fade-in + back to top -->')
    c = c.replace('<!-- 访客计数器 -->', '<!-- Visitor Counter -->')

    # Check for any remaining Chinese text by searching
    # Most of the JS data in this file should already be in English based on the preview

    # Let me check for specific patterns
    # renderDilemma function
    c = c.replace("困境 ${String(d.id).padStart(2,'0')}", "Dilemma ${String(d.id).padStart(2,'0')}")

    # Question num
    c = c.replace("`第${currentQuestion + 1}题`", "`Question ${currentQuestion + 1}`")

    # Continue/View Results
    c = c.replace("'继续' : '查看结果'", "'Continue' : 'View Results'")

    # Advice card label
    c = c.replace("'卡点 '", "'Block '")

    # Result score text
    c = c.replace('命中 ${score} 次', 'matched ${score} times')

    # Step labels
    c = c.replace("Step ${['一','二','三','四'][i]}", "Step ${['One','Two','Three','Four'][i]}")

    # Hidden level alert
    c = c.replace("alert('先写点什么吧，至少说一件你卡住的事。');", "alert('Please write something first — at least one thing you're stuck on.');")

    # Download card text
    c = c.replace("ctx.fillText('我的隐藏关卡', 300, 80);", "ctx.fillText('My Hidden Level', 300, 80);")
    c = c.replace("link.download = '我的隐藏关卡.png';", "link.download = 'my-hidden-level.png';")

    # Check for remaining Chinese patterns
    import re
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]')
    remaining = []
    for i, line in enumerate(c.split('\n'), 1):
        # Skip CSS comments, HTML comments
        if line.strip().startswith('/*') or line.strip().startswith('//') or line.strip().startswith('<!--'):
            continue
        if chinese_pattern.search(line):
            remaining.append(f"  Line {i}: {line.strip()[:100]}")

    if remaining:
        print(f"  WARNING: {len(remaining)} lines still have Chinese in 第五关-婚恋家庭.html:")
        for r in remaining[:20]:
            print(r)

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)
    print("  Done: 第五关-婚恋家庭.html")


# ============================================================
# Main
# ============================================================
if __name__ == '__main__':
    translate_file5()
    translate_file11()
    translate_file4()
    translate_file12()
    print("\nAll translations complete!")
