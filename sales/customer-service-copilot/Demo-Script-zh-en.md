Demo Script — Customer Service Copilot（Web & WhatsApp）/ 演示脚本（中英）

Scenario / 场景
- Brand｜DemoTea HK（示例品牌）
- Channels｜Web widget + WhatsApp Business
- Languages｜Cantonese + English + Chinese

Part A — Web Widget Flow / 网页小部件
1) Greeting｜EN: Hi! How can I help today? ZH：你好！请问有什么可以帮到你？
2) FAQ｜User asks opening hours & nearest store → Assistant answers with store list and map links; shows source from KB
   - ZH 提示：答案下方显示“来源：官网-门店页/更新于YYYY-MM-DD”
3) Booking Intent｜User: I want to book a table for 4 this Friday 7pm at Causeway Bay
   - Assistant collects name/phone/time/branch; confirms summary; sends email/Sheet entry
4) Policy QA｜Return/refund policy question → RAG answer with confidence; fallback to human if confidence < threshold
5) Handover｜User types “talk to human” → live chat handover stub (explain production uses agent console/Zendesk)

Part B — WhatsApp Flow / WhatsApp 演示
1) Opt-in｜Show business-initiated template or user-initiated chat
2) Multilingual｜User sends Cantonese; assistant replies in Cantonese, preserves tone
3) Promo｜User asks about current promotions → assistant pulls promo KB or CMS stub
4) Reservation｜Same as web: collect info; provide booking reference; suggest add-to-calendar link
5) Escalation｜Detect negative sentiment → proactive offer human handover; tag conversation

Operational Notes / 运营要点
- Data｜Initial KB from website/menu/FAQ PDFs; admin console for updates
- Quality｜Weekly QA sampling, coverage & accuracy dashboard, continuous tuning
- Security｜HK VPC, PDPO alignment, minimal data retention, DPA available
- BSP｜Twilio/Infobip/MessageBird/360dialog; production connects via client’s number or sub-account

Success Metrics / 成功指标（演示口径）
- First response <3s; Auto-answer coverage >80%; Human handover -20–40%
- Booking/completion rate uplift 10–20%

Closing / 收尾话术
- ZH｜如果这套流程适合贵司，我们可以在 4–6 周内完成一轮试点，上线可见指标与报告。
- EN｜If this fits, we can deliver a 4–6 week pilot with measurable outcomes and a clear report.

