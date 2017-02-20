

-- 量化清算数据库  
CREATE DATABASE IF NOT EXISTS qcd;
GRANT ALL ON qcd.* TO 'pmops'@'%';
GRANT ALL ON qcd.* TO 'pmops'@'localhost';
GRANT ALL ON qcd.* TO 'pmops'@'127.0.0.1';


USE qcd;

/* 关系：
券商  一对多  产品
产品  一对多  资金账户(trdacct)
资金账户(期货现货类型唯一)  一对多  总账户
总账户 一对多 子账户
子账户 包含 期货 和 现货
策略 一对多 子账户
*/

-- 1.券商表
DROP TABLE IF EXISTS broker;
CREATE TABLE `broker` (
  `bid`    INT NOT NULL,                       -- 券商ID
  `bname`  VARCHAR(32) NOT NULL,               -- 券商名称
  `blname` VARCHAR(128) NOT NULL DEFAULT 'na', -- 券商详细名称
  PRIMARY KEY (`bid`)
);
-- 2.产品表
DROP TABLE IF EXISTS product;
CREATE TABLE product(
  pid INT NOT NULL,                            -- 产品ID
  pname VARCHAR(32) NOT NULL,                  -- 产品名称
  plname VARCHAR(128) NOT NULL DEFAULT 'na',   -- 产品详细名称
  stat CHAR(1) NOT NULL,                       -- 状态(0:有效,1:无效)
  PRIMARY KEY (pid)
);
-- 资金账号表
DROP TABLE IF EXISTS acct;
CREATE TABLE acct(
  trdacct VARCHAR(10) NOT NULL,           -- 资金账户(交易账户)
  stkex CHAR(1) NOT NULL,                 -- 市场
  stkbd CHAR(2) NOT NULL,                 -- 板块
  bid INT NOT NULL,                       -- 券商ID
  pid INT NOT NULL,                       -- 产品ID
  PRIMARY KEY (trdacct)
);


-- 3.资金账户/总账户/子账户 对应关系在 trdacct表，分别对应 trdacct、cust_code、cuacct_code 字段

-- 4.策略表
DROP TABLE IF EXISTS tactics;
CREATE TABLE tactics(
   tsid  INT NOT NULL,           -- 策略ID
   tsname VARCHAR(32) NOT NULL,  -- 策略名称
   tsdesc VARCHAR(200) NOT NULL, -- 策略描述
   PRIMARY KEY(tsid)
);
-- 策略和子账户对应关系 表
DROP TABLE IF EXISTS tactics_cuacct_relation
CREATE TABLE tactics_cuacct_relation(
  tsid INT NOT NULL,           -- 策略ID
  cuacct_code BIGINT NOT NULL, -- 子账户ID
  PRIMARY KEY (tsid,cuacct_code)
);



-- 1.账户信息文件
DROP TABLE IF EXISTS trdacct;
CREATE TABLE trdacct(
    sett_date      CHAR(8) NOT NULL,      -- 1.清算日期 ?  -- trdacct只是一个账户信息表，不会每天都变的，第一列的日期应该只是一个时间标识而已，没有具体的意义，但是可以说明该账户是什么时候创建的
    cust_code      BIGINT NOT NULL,   -- 2.客户代码
    cuacct_code    BIGINT NOT NULL,   -- 3.资产账户
    int_org        SMALLINT NOT NULL, -- 4.内部机构
    stkex          CHAR(1) NOT NULL,  -- 5.证券交易所:'0'深圳交易所,'1'上海交易所,'5'中国金融期货交易所,'6'上海期货交易所,'7'大连商品交易所,'8'郑州商品交易所
    stkbd          CHAR(2) NOT NULL,  -- 6.交易板块:'00'深圳Ａ股,'01' 深圳Ｂ股,'02'深圳三板A,'03'深圳三板B,'10'上海Ａ股,'11'上海Ｂ股,'50'中国金融期货交易所,'60'上海期货交易所,'70'大连商品交易所,'80'郑州商品交易所
    trdacct        VARCHAR(10) NOT NULL, -- 7.交易账户
    trdacct_sn     SMALLINT DEFAULT '0',  -- 8.交易账户序号
    trdacct_exid   VARCHAR(10),           -- 9.报盘交易账户  
    trdacct_type   CHAR(1) NOT NULL,      -- 10.交易账户类型:'0'境内帐户,'1'境外帐户
    trdacct_excls  CHAR(1) NOT NULL,      -- 11.交易账户类别:'0'个人帐户,'1'机构帐户,'2'个人信用帐户,'3'机构信用帐户,'4'个人基金帐户,'5'机构基金帐户,'6'产品普通账户,'7'产品基金账户,'8'产品信用账户
    trdacct_name   VARCHAR(32) NOT NULL,  -- 12交易账户名称
    trdacct_status CHAR(1) NOT NULL,      -- 13.交易账户状态:'0'正常,'1'挂失,'2'冻结,'3'司法冻结,'4'休眠,'9'注销
    treg_status    CHAR(1) NOT NULL,      -- 14.交易指定状态:'0'未指定,'1'首日指定,'2'已指定
    breg_status    CHAR(1) NOT NULL,      -- 15.回购指定状态:'0'未指定,'1'首日指定,'2'已指定
    stkpbu         VARCHAR(8) NOT NULL,   -- 16.交易单元  
    firmid         VARCHAR(8) NOT NULL,   -- 17.代理商号  
    id_type        CHAR(2) NOT NULL,      -- 18.证件类型:'00'身份证号,'01'护照号码,'02'军官证,'03'士兵证,'04'回乡证,'05'户口本,'09'其它证件,'10'工商营业执照,'11'社团法人注册登记证书,
                                                      -- '12'机关法人成立批文,'13'事业法人成立批文,'14'境外有效商业登记证明,'15'武警,'16'军队,'17'基金会,'18'技术监督局号码,'19'其它证件,'1a'组织机构代码证,'1b'税务登记证,'1z'批文
    id_code        VARCHAR(32) DEFAULT '', -- 19证件号码
    id_iss_agcy    VARCHAR(65) DEFAULT '', -- 20.发证机关
    id_exp_date    CHAR(8) DEFAULT '20200101', -- 21.证件有效日期  
    open_date      CHAR(8) DEFAULT '20110101', -- 22.开户日期 
    PRIMARY KEY(cust_code,cuacct_code,stkex,stkbd,trdacct)
);

-- 2.合约信息文件
DROP TABLE IF EXISTS instrumentinfo;
CREATE TABLE instrumentinfo(
    trd_date     CHAR(8) NOT NULL,        -- 日期
    instrument_id VARCHAR(32) NOT NULL, -- 合约名
    exchange_id VARCHAR(32) NOT NULL, -- 交易所
    maxlimit_ordervolume INT NOT NULL,-- 每笔订单最大合约手数 
    minlimit_ordervolume INT NOT NULL, -- 每笔订单最小合约手数
    volume_multiple INT NOT NULL, -- 合约乘数
    long_marginratio DECIMAL(12,10) NOT NULL, -- 多头保证金率
    short_marginratio DECIMAL(12,10) NOT NULL,-- 空头保证金率
    pre_settlement_price DECIMAL(17,3) NOT NULL, -- 昨日结算价(每天盘后拉,该字段就是今结价)
    PRIMARY KEY(trd_date,instrument_id)
);

-- 3.递延费费率文件
DROP TABLE IF EXISTS delayfeeinfo;
CREATE TABLE delayfeeinfo(
    trd_date     CHAR(8) NOT NULL,        -- 日期
    instrument_id VARCHAR(32) NOT NULL, -- 1.合约名
    delayfee_ratio DECIMAL(15,8) NOT NULL, -- 2.递延费率
    bs_direct CHAR(1) NOT NULL, -- 持仓方向 '0'买入  '1'卖出;多空标志(0:多,1:空)  1 : 空付多  0 : 多付空
    PRIMARY KEY(trd_date,instrument_id)
);

-- feerate 费率文件
DROP TABLE IF EXISTS feerateinfo;
CREATE TABLE feerateinfo(
    trd_date     CHAR(8) NOT NULL,   -- 日期
    exchange_id   VARCHAR(32) NOT NULL, -- 交易所
    instrument    VARCHAR(32) NOT NULL, -- 合约标识
    product_id    VARCHAR(8) NOT NULL, -- 品种代码 
    biz_type char(1) not null, -- 交易类型(业务标示:0开仓，1平仓，2平今，3平昨)
    feerate_by_amt DECIMAL(15,8) NOT NULL, -- 费率值，按成交金额比例收费
    feerate_by_qty DECIMAL(15,8) not null, -- 费率值，按每手收费
    PRIMARY KEY(trd_date,exchange_id,instrument,product_id,biz_type)
);

-- 出入金记录表
DROP TABLE IF EXISTS fund_transfer_record;
CREATE TABLE fund_transfer_record(
    trd_date CHAR(8) NOT NULL, -- 日期
    acct_type TINYINT NOT NULL, -- 账户类型(0:主账户,1:子账户)
    cust_code BIGINT NOT NULL, -- 客户代码
    cuacct_code BIGINT not null default 0, -- 资产账户(若账户类型为主账户，则该字段可为0)
    future_spot_type TINYINT not null, -- 账户内期货和现货的资金类型(0:期货 ，1:现货)
    out_fund DECIMAL(17,2) NOT NULL, -- 转出资金
    in_fund DECIMAL(17,2) NOT NULL, -- 转入资金
    PRIMARY KEY (trd_date,acct_type,cust_code,cuacct_code)
); 

-- 市场信息表
DROP TABLE IF EXISTS marketinfo;
CREATE TABLE marketinfo
(   
    stkex CHAR(1) NOT NULL,
    exchange_id VARCHAR(32) NOT NULL,
    market_name VARCHAR(32) NOT NULL,
    PRIMARY KEY (stkex)
);

-- 4.当日交易记录文件
DROP TABLE IF EXISTS fts_order;
CREATE TABLE fts_order(
    trd_date CHAR(8) NOT NULL,-- 1.交易日期 必送 格式：YYYYMMDD
    order_date CHAR(8) NOT NULL,-- 2.委托日期 必送 格式：YYYYMMDD
    order_time TIMESTAMP(2) NOT NULL, -- 3.委托时间 必送 格式：'YYYY-MM-DD HH24:MI:SS.FF'
    order_sn INT NOT NULL, -- 4.委托序号 必送
    order_id VARCHAR(10) NOT NULL,-- 5.合同序号 必送，对应股指期货报单号
    order_type CHAR(1) NOT NULL, -- 6.委托类型 必送 '0'限价委托,'1'市价委托
    mp_ordertype VARCHAR(1) NOT NULL, -- 7.市价委托类型 必送 0 限价委托,1 对方买入,2 本方买入,3 即时买入,4 五档买入,5 全额买入,6 转限买入,A 对方卖出,B 本方卖出,C 即时卖出,D 五档卖出,E 全额卖出,F 转限卖出
    cust_code BIGINT NOT NULL, --  8.客户代码 必送
    cuacct_code BIGINT NOT NULL, --  9.资产账户    
    int_org SMALLINT NOT NULL, -- 10.内部机构
    currency CHAR(1) NOT NULL, --  11.货币代码 '0'人民币,'1'港币,'2'美元
    trdacct VARCHAR(10) NOT NULL, --  12.交易账户 必送，对应股指期货交易编码
    trdacct_exid VARCHAR(10) NOT NULL, -- 13.报盘交易账户 必送
    stkex CHAR(1) NOT NULL, -- 14.证券交易所
    stkbd CHAR(2) NOT NULL, -- 15.交易板块
    stk_name VARCHAR(16) NOT NULL, --  16.证券名称，期货合约类型
    stk_code VARCHAR(32) NOT NULL, --  17.期货合约代码
    stk_biz SMALLINT NOT NULL, --  18.证券业务 900:期货买入开仓,901:期货卖出开仓,902:期货买入平昨仓,903:期货卖出平昨仓,908:期货买入平今仓,909:期货卖出平今仓
    bs_side CHAR(1) NOT NULL, -- 19.买卖方向 'B'买入  'S'卖出
    order_price decimal(17,3) NOT NULL, --  20.委托价格 必送
    order_qty INT NOT NULL, --  21.委托数量
    order_amt decimal(17,3) NOT NULL, --  22.委托金额
    withdrawn_qty INT NOT NULL, -- 23.已撤单数量 必送
    matched_qty INT NOT NULL, --  24.已成交数量
    matched_amt decimal(17,3)  NOT NULL, -- 25.已成交金额 
    commision decimal(17,3) NOT NULL, -- 25.手续费   (如果导入前不好计算，可直接导0，清算再计算手续费)
    order_status CHAR(1) NOT NULL, -- 27.委托状态 0未报,1正报,2已报,3已报待撤,4部成待撤,5部撤,6已撤,7部成待撤,8已成,9废单,A待报
    PRIMARY KEY(trd_date,order_sn)
);
-- 订单-历史表(一个月前的订单放入历史表？)
drop table if exists fts_order_his;
create table fts_order_his like fts_order;

-- 5.经纪商当日资金结算文件
DROP TABLE IF EXISTS cusfund;
CREATE TABLE cusfund(
    trd_date DATE NOT NULL, -- 日期 格式：YYYY-MM-DD
    account_id BIGINT NOT NULL, -- 客户资金账户
    fund_balance_total DECIMAL(20,6) NOT NULL, -- 资金权益总额
    available_fund DECIMAL(20,6) NOT NULL, -- 可用资金
    margin_call DECIMAL(20,6) NOT NULL, -- 需追加保证金
    risk_degree DECIMAL(5,4) NOT NULL, -- 风险度
    pre_balance_zr DECIMAL(20,6) NOT NULL, -- 上日结存(逐日盯市)
    pre_balance_zb DECIMAL(20,6) NOT NULL, -- 上日结存(逐笔对冲)
    balance_zr DECIMAL(20,6) NOT NULL, -- 当日结存(逐日盯市)
    balance_zb DECIMAL(20,6) NOT NULL, -- 当日结存(逐笔对冲)
    total_profit_zr DECIMAL(20,6) NOT NULL, -- 当日总盈亏(逐日盯市)--【平仓盈亏+持仓盯市盈亏 MTM P/L】
    total_profit_zb DECIMAL(20,6) NOT NULL, -- 当日总盈亏(逐笔对冲)--【平仓盈亏+持仓盯市盈亏 MTM P/L】
    float_profit_zb DECIMAL(20,6) NOT NULL, -- 浮动盈亏(逐笔对冲)--【持仓盯市盈亏 MTM P/L - 手续费】
    spec_charge_against DECIMAL(20,6) NOT NULL, -- 非货币冲抵金额
    is_trading_menber CHAR(1) NOT NULL, -- 是否为交易会员--N
    currency CHAR(3) NOT NULL, --  币种 '0'人民币,'1'港币,'2'美元
    currency_fund DECIMAL(20,6) NOT NULL,  -- 实有货币资金
    currency_charge_against DECIMAL(20,6) NOT NULL, -- 货币冲抵金额
    other_currency_mortgage_out DECIMAL(20,6) NOT NULL, -- 其他货币质出金额
    currency_mortgage_margin DECIMAL(20,6) NOT NULL, -- 货币质押保证金占用
    total_fund DECIMAL(20,6) NOT NULL, -- 当日总权利金
    PRIMARY KEY(trd_date,account_id)
);


-- 6.经纪商当日持仓结算文件
DROP TABLE IF EXISTS holddata;
CREATE TABLE holddata(
    trd_date DATE NOT NULL, -- 日期 格式：YYYY-MM-DD
    account_id BIGINT NOT NULL, -- 客户资金账户
    instrument_id VARCHAR(32) NOT NULL, -- 合约代码 
    direction CHAR(1) NOT NULL, -- 买卖标志 '0'买入  '1'卖出
    hedge_flag CHAR(1) NOT NULL, -- 投机套保标志
    position_volume INT NOT NULL, -- 持仓量
    trading_margin DECIMAL(20,6) NOT NULL, -- 交易保证金（保证金占用）
    position_profit_zr DECIMAL(20,6) NOT NULL, -- 持仓盈亏（逐日盯市）
    position_profit_zb DECIMAL(20,6) NOT NULL, -- 持仓盈亏（逐笔对冲）
    position_average DECIMAL(20,6) NOT NULL, -- 持仓均价
    pre_settlement_price DECIMAL(20,6) NOT NULL, -- 昨结算价
    settlementprice DECIMAL(20,6) NOT NULL, -- 今结算价
    trans_code    VARCHAR(10) NOT NULL, -- 交易编码 
    exchange_id VARCHAR(32) NOT NULL, -- 交易所
    is_trading_menber CHAR(1) NOT NULL, -- 是否为交易会员--N
    currency CHAR(3) NOT NULL,-- 币种 '0'人民币,'1'港币,'2'美元
    PRIMARY KEY(trd_date,account_id,instrument_id)
);


-- 7.FTS_FUND_OCCUR      //期货清算后账户资金信息
DROP TABLE IF EXISTS fts_future_fund;
CREATE TABLE fts_future_fund(
    sett_date CHAR(8) NOT NULL,-- 清算日期 格式：YYYYMMDD
    int_org SMALLINT NOT NULL,-- 内部机构 8888
    cust_code BIGINT NOT NULL,-- 客户代码 
    currency CHAR(1) NOT NULL,-- 货币代码 '0'人民币,'1'港币,'2'美元
    fund_val DECIMAL(20,6) NOT NULL,-- 当日结存 不计浮动盈亏
    buy_margin DECIMAL(20,6) NOT NULL,-- 买入持仓保证金 
    sell_margin DECIMAL(20,6) NOT NULL,-- 卖出持仓保证金 
    margin DECIMAL(20,6) NOT NULL,-- 持仓保证金 买+卖
    close_pl DECIMAL(20,6) NOT NULL,-- 平仓盈亏 
    position_pl DECIMAL(20,6) NOT NULL,-- 持仓盈亏 
    commision DECIMAL(20,6) NOT NULL,-- 手续费 当日手续费总额，包含交割手续费
    fund_bln DECIMAL(20,6) NOT NULL,-- 可用保证金 日内盈利不计入
    interests DECIMAL(20,6) NOT NULL,-- 客户权益 浮动盈亏计入
    remark VARCHAR(128) NOT NULL,-- 备注信息 备用
    PRIMARY KEY(sett_date,cust_code)
);


-- 8.FTS_FUND_SUB_OCCUR  //期货清算后子账户资金信息
DROP TABLE IF EXISTS fts_future_fund_sub;
CREATE TABLE fts_future_fund_sub(
    sett_date CHAR(8) NOT NULL,-- 清算日期 格式：YYYYMMDD
    int_org SMALLINT NOT NULL,-- 内部机构 8888
    cust_code BIGINT NOT NULL,-- 客户代码 
    cuacct_code BIGINT NOT NULL,   -- 资产账户
    currency CHAR(1) NOT NULL,-- 货币代码 '0'人民币,'1'港币,'2'美元
    fund_val DECIMAL(20,6) NOT NULL,-- 当日结存 不计浮动盈亏
    buy_margin DECIMAL(20,6) NOT NULL,-- 买入持仓保证金 
    sell_margin DECIMAL(20,6) NOT NULL,-- 卖出持仓保证金 
    margin DECIMAL(20,6) NOT NULL,-- 持仓保证金 买+卖
    close_pl DECIMAL(20,6) NOT NULL,-- 平仓盈亏 
    position_pl DECIMAL(20,6) NOT NULL,-- 持仓盈亏 
    commision DECIMAL(20,6) NOT NULL,-- 手续费 当日手续费总额，包含交割手续费
    fund_bln DECIMAL(20,6) NOT NULL,-- 可用保证金 日内盈利不计入
    interests DECIMAL(20,6) NOT NULL,-- 客户权益 浮动盈亏计入
    remark VARCHAR(128) NOT NULL,-- 备注信息 备用
    PRIMARY KEY(sett_date,cust_code,cuacct_code)
);


-- 9.FTS_FUTURE_HOLD    //期货清算后账户持仓信息   子账户一个合约只会有一个方向的持仓，主账户一个合约允许有两个方向的持仓
DROP TABLE IF EXISTS fts_hold;
CREATE TABLE fts_hold(
    sett_date     CHAR(8) NOT NULL, -- 清算日期 格式：YYYYMMDD
    int_org       SMALLINT NOT NULL, --  内部机构 8888
    cust_code     BIGINT NOT NULL, --  客户代码 
    currency      CHAR(1) NOT NULL, --  货币代码 '0'人民币,'1'港币,'2'美元
    stkex         CHAR(1) NOT NULL, --  证券交易所 '0'深圳交易所,'1'上海交易所,'5'中国金融期货交易所,'6'上海期货交易所,'7'大连商品交易所,'8'郑州商品交易所
    stkbd         CHAR(2) NOT NULL, -- 交易板块 '00'深圳A股,'01'深圳B股,'02'深圳三板A,'03'深圳三板B,'10'上海A股,'11'上海B股,'50'中国金融期货交易所,'60'上海期货交易所,'70'大连商品交易所,'80'郑州商品交易所
    trans_code    VARCHAR(10) NOT NULL, -- 交易编码 
    product_id    VARCHAR(8) NOT NULL, -- 品种代码 
    instrument_id VARCHAR(32) NOT NULL, -- 合约代码 
    bs_direct     CHAR(1) NOT NULL, -- 持仓方向 'B'买入  'S'卖出
    buy_qty       int NOT NULL, -- 买入数量 即：开仓数量(当天)
    sell_qty      int NOT NULL, -- 卖出数量 即：平仓数量(当天)
    buy_price     DECIMAL(20,6) NOT NULL, -- 买入均价 (当天)
    sell_price    DECIMAL(20,6) NOT NULL, -- 卖出均价 (当天)
    hold_bal      int NOT NULL, -- 客户持仓 
    average_price DECIMAL(20,6) NOT NULL, -- 持仓均价 
    clear_price   DECIMAL(20,6) NOT NULL, -- 结算价格 
    position_pl   DECIMAL(20,6) NOT NULL, -- 持仓盈亏 
    close_pl      DECIMAL(20,6) NOT NULL, -- 平仓盈亏 
    commision     DECIMAL(20,6) NOT NULL, -- 手续费 包含交割手续费
    remark        VARCHAR(128) NOT NULL, -- 备注信息 备用
    PRIMARY KEY(sett_date,cust_code,instrument_id,bs_direct)
);

-- 10.FTS_FUTURE_SUB_HOLD  //期货清算后子账户持仓信息   子账户一个合约只会有一个方向的持仓，主账户一个合约允许有两个方向的持仓
DROP TABLE IF EXISTS fts_hold_sub;
CREATE TABLE fts_hold_sub(
    sett_date     CHAR(8) NOT NULL, -- 清算日期 格式：YYYYMMDD
    int_org       SMALLINT NOT NULL, --  内部机构 8888
    cust_code     BIGINT NOT NULL, --  客户代码 
    cuacct_code   BIGINT NOT NULL,   -- 资产账户
    currency      CHAR(1) NOT NULL, --  货币代码 '0'人民币,'1'港币,'2'美元
    stkex         CHAR(1) NOT NULL, --  证券交易所 '0'深圳交易所,'1'上海交易所,'5'中国金融期货交易所,'6'上海期货交易所,'7'大连商品交易所,'8'郑州商品交易所
    stkbd         CHAR(2) NOT NULL, -- 交易板块 '00'深圳A股,'01'深圳B股,'02'深圳三板A,'03'深圳三板B,'10'上海A股,'11'上海B股,'50'中国金融期货交易所,'60'上海期货交易所,'70'大连商品交易所,'80'郑州商品交易所
    trans_code    VARCHAR(10) NOT NULL, -- 交易编码 
    product_id    VARCHAR(8) NOT NULL, -- 品种代码 
    instrument_id VARCHAR(32) NOT NULL, -- 合约代码 
    bs_direct     CHAR(1) NOT NULL, -- 持仓方向 'B'买入  'S'卖出
    buy_qty       int NOT NULL, -- 买入数量 即：开仓数量
    sell_qty      int NOT NULL, -- 卖出数量 即：平仓数量
    buy_price     DECIMAL(20,6) NOT NULL, -- 买入均价 
    sell_price    DECIMAL(20,6) NOT NULL, -- 卖出均价 
    hold_bal      int NOT NULL, -- 客户持仓 
    average_price DECIMAL(20,6) NOT NULL, -- 持仓均价 
    clear_price   DECIMAL(20,6) NOT NULL, -- 结算价格 
    position_pl   DECIMAL(20,6) NOT NULL, -- 持仓盈亏 
    close_pl      DECIMAL(20,6) NOT NULL, -- 平仓盈亏 
    commision     DECIMAL(20,6) NOT NULL, -- 手续费 包含交割手续费
    remark        VARCHAR(128) NOT NULL, -- 备注信息 备用
    PRIMARY KEY(sett_date,cust_code,cuacct_code,instrument_id,bs_direct)
);




-- 11.      //现货清算后账户资金信息
DROP TABLE IF EXISTS fts_spot_fund;
CREATE TABLE fts_spot_fund(
    sett_date CHAR(8) NOT NULL,-- 清算日期 格式：YYYYMMDD
    int_org SMALLINT NOT NULL,-- 内部机构 8888
    cust_code BIGINT NOT NULL,-- 客户代码 
    currency CHAR(1) NOT NULL,-- 货币代码 '0'人民币,'1'港币,'2'美元
    fund_val DECIMAL(20,6) NOT NULL,-- 当日结存 不计浮动盈亏
    buy_margin DECIMAL(20,6) NOT NULL,-- 买入持仓保证金 
    sell_margin DECIMAL(20,6) NOT NULL,-- 卖出持仓保证金 
    margin DECIMAL(20,6) NOT NULL,-- 持仓保证金 买+卖
    close_pl DECIMAL(20,6) NOT NULL,-- 平仓盈亏 
    position_pl DECIMAL(20,6) NOT NULL,-- 持仓盈亏 
    commision DECIMAL(20,6) NOT NULL,-- 手续费 当日手续费总额，包含交割手续费
    fund_bln DECIMAL(20,6) NOT NULL,-- 可用保证金 日内盈利不计入
    interests DECIMAL(20,6) NOT NULL,-- 客户权益 浮动盈亏计入
    remark VARCHAR(128) NOT NULL,-- 备注信息 备用
    PRIMARY KEY(sett_date,cust_code)
);

-- 12.  //现货清算后子账户资金信息
DROP TABLE IF EXISTS fts_spot_fund_sub;
CREATE TABLE fts_spot_fund_sub(
    sett_date CHAR(8) NOT NULL,-- 清算日期 格式：YYYYMMDD
    int_org SMALLINT NOT NULL,-- 内部机构 8888
    cust_code BIGINT NOT NULL,-- 客户代码 
    cuacct_code BIGINT NOT NULL,   -- 资产账户
    currency CHAR(1) NOT NULL,-- 货币代码 '0'人民币,'1'港币,'2'美元
    fund_val DECIMAL(20,6) NOT NULL,-- 当日结存 不计浮动盈亏
    buy_margin DECIMAL(20,6) NOT NULL,-- 买入持仓保证金 
    sell_margin DECIMAL(20,6) NOT NULL,-- 卖出持仓保证金 
    margin DECIMAL(20,6) NOT NULL,-- 持仓保证金 买+卖
    close_pl DECIMAL(20,6) NOT NULL,-- 平仓盈亏 
    position_pl DECIMAL(20,6) NOT NULL,-- 持仓盈亏 
    commision DECIMAL(20,6) NOT NULL,-- 手续费 当日手续费总额，包含交割手续费
    fund_bln DECIMAL(20,6) NOT NULL,-- 可用保证金 日内盈利不计入
    interests DECIMAL(20,6) NOT NULL,-- 客户权益 浮动盈亏计入
    remark VARCHAR(128) NOT NULL,-- 备注信息 备用
    PRIMARY KEY(sett_date,cust_code,cuacct_code)
);