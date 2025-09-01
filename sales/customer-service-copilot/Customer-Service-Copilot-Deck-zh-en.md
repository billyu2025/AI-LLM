Slide 1 — Executive Summary / 核心概要

ZH｜面向香港零售/餐饮/酒店的 Customer Service Copilot（网页/WhatsApp），4–6 周交付，聚焦提升客服效率与转化率，私有化部署、数据驻留合规（PDPO）。
EN｜Customer Service Copilot for HK Retail/F&B/Hospitality (Web & WhatsApp). 4–6 week pilot. Focus on faster response, higher conversion, and lower workload. Private deployment with HK data residency & PDPO alignment.

Value / 价值
- ZH｜首次响应 <3s；常见问题自动解答覆盖率 >80%；转人工率下降 20–40%；可量化节省人力成本。
- EN｜First response <3s; >80% FAQ auto-answer coverage; 20–40% reduction in human handover; measurable labor savings.

Why Now / 何以当下
- ZH｜WhatsApp 已成为港人首选沟通渠道；门店与官网流量碎片化，自动化与一致性成为关键。
- EN｜WhatsApp dominates HK communication; fragmented traffic across stores and web requires automation and consistency.

—

Slide 2 — Use Cases & Outcomes / 典型场景与成效

Use Cases / 场景
- ZH｜FAQ 问答（营业时间、门店、配送/退换、会员积分、优惠券规则）
- ZH｜预约/下单意图识别与表单收集（姓名、电话、时间、门店/客房）
- ZH｜订单/工单状态查询（可先用伪集成，后续再对接）
- EN｜FAQ, booking/order intent capture, status inquiries (mock-first, integrate later)

Expected Outcomes / 预期指标
- ZH｜平均处理时长 -30% 至 -50%；转化率 +10–20%；NPS/CSAT 提升
- EN｜Average handling time -30–50%; Conversion +10–20%; NPS/CSAT improved

Channels / 渠道
- ZH｜网页小部件、WhatsApp Business（BSP：Twilio/Infobip/MessageBird/360dialog等）
- EN｜Web widget and WhatsApp Business via BSP partners (Twilio/Infobip/MessageBird/360dialog)

—

Slide 3 — Architecture & Compliance / 架构与合规

Deployment / 部署
- ZH｜香港区云 VPC 或本地化环境；API 网关隔离；零信任访问
- EN｜HK region VPC or on-prem; API gateway isolation; zero-trust access

Data & Models / 数据与模型
- ZH｜私有化 RAG（向量库 + 检索），可选开源/商用 LLM；中英粤三语
- EN｜Private RAG (vector DB + retrieval); open/commercial LLM options; Cantonese/English/Chinese

Security & PDPO / 安全与隐私
- ZH｜仅存储必要会话与知识库；数据加密；可签 DPA；提供 PIA 模板与安全问卷回应
- EN｜Minimal data retention; encryption; DPA available; PIA template & security questionnaire ready

Integration / 集成
- ZH｜优先轻集成：网站/菜单/FAQ 抓取；表单-邮件/Sheets；订单/CRM 对接后置
- EN｜Lightweight first: crawl website/menu/FAQ; form-to-email/Sheets; defer deep CRM/OMS

—

Slide 4 — 4–6 Week Pilot Plan / 试点计划

Scope / 范围
- ZH｜1 个品牌/门店集；网页+WhatsApp 两渠道；FAQ 100–300 条；2 个业务表单
- EN｜1 brand/store group; Web + WhatsApp; 100–300 FAQ; 2 business intake forms

Milestones / 里程碑
- Week 1｜ZH：资料收集（官网/政策PDF/菜单），部署环境，初始知识库；EN：Data intake, env setup
- Week 2｜ZH：意图与对话流配置，首轮训练与质检；EN：Intents & flows, first QA
- Week 3｜ZH：网页小部件接入，WhatsApp 沙箱；EN：Web widget + WhatsApp sandbox
- Week 4｜ZH：上线试运行，指标埋点，验收；EN：Go-live pilot, telemetry, acceptance
- 可选 2 周扩展｜渠道/知识库扩充、Cantonese 口语优化

Deliverables / 交付物
- ZH｜可运行的 Web/WhatsApp 助手、知识库后台、日志与质检看板、验收报告
- EN｜Running assistants, KB console, logs & QA dashboard, acceptance report

—

Slide 5 — Commercials / 商务条款

Pricing / 价格（参考）
- ZH｜PoC：HKD 100k–200k（4–6 周，明确范围）；后续订阅 HKD 8k–20k/月/品牌或门店集
- EN｜PoC: HKD 100k–200k; Subscription HKD 8k–20k/month per brand/store group

Assumptions / 假设
- ZH｜单一品牌；数据可用；无深度系统对接；支持 1–2 次知识扩充
- EN｜Single brand; data available; no deep system integrations; 1–2 KB expansions

Funding / 资助
- ZH｜TVP 科技券、RTTP 培训；可配合客户申请以降低现金流压力
- EN｜TVP/RTTP eligible formats to reduce upfront cash for SMEs

Legal / 法务
- ZH｜NDA、MSA、SOW、DPA、PDPO 对齐；付款里程碑 40/40/20 或 30/50/20
- EN｜NDA, MSA, SOW, DPA, PDPO alignment; 40/40/20 or 30/50/20 milestone billing

—

Slide 6 — Next Steps / 下一步

Required from Client / 客户需提供
- ZH｜品牌与门店清单、FAQ/菜单/政策PDF、品牌语调、渠道接入（WhatsApp 号/网页权限）
- EN｜Brand/store list, FAQ/menu/policy PDFs, tone of voice, channel access

Workshop / 研讨
- ZH｜90 分钟启动会：目标指标、范围确认、安全与合规核对
- EN｜90-min kickoff: goals, scope, security & compliance

Decision / 决策
- ZH｜确认试点范围与报价 → 签署 NDA/SoW → 启动
- EN｜Confirm pilot & quote → NDA/SoW → Kickoff

Contact / 联系方式
- ZH｜WhatsApp/微信/电邮：请见封面名片
- EN｜WhatsApp/WeChat/Email: see cover card

