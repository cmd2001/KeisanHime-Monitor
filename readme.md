# KeisanHime Monitor

计算姬(服务器)监控面板

**Still Under Heavy Development**

## Features(Todo List)

* [ ] 服务器系统状态检测，定期curl实现
* [ ] 服务状态检测，tcping实现
* [ ] 分组显示，组的额外信息：组名；机器的额外信息：hostname，域名，ip
* [ ] 登陆鉴权（sha512+盐）
* [ ] 对单个服务器作图：近一天，一周，一月，一年可用性情况
* [ ] smtp通知（仅针对系统），当机器宕机。定期检查+启发式检查（可能通过sleep最小等待时间实现，如何取消上一个sleep？我不知道，再考虑，但似乎不取消复杂度也对），并且对每个宕机标示是否发送过。
* [ ] json config checker

## License

GPL v3.
