import mysql.connector as mysql

account = mysql.connect(user="root", password="123456789",
                        host="localhost", database="MidProj")

cursor = account.cursor()
# cursor.execute("create database MidProj")

cursor.execute(
    # show
    # select * from dept;
    # select * from student;
    # select * from course;
    # select * from section;
    # select * from takes;

    # 新增 table  IF NOT EXISTS 檢查有沒有存在 有:不做事 沒:做事
    # "create table COLLEGE    (CName varchar(10) PRIMARY KEY , COffice varchar(10) ,  CPhone int ,          DEAN varchar(10))"
    # "create table  INSTRUCTOR(Id    varchar(10) PRIMARY KEY , `Rank` varchar(10) ,   IName varchar(10),    IOffice varchar(10) , IPhone int,        EMPLOYS varchar(10) )"
    # "create table DEPT       (DName varchar(10),              DCode varchar(10)  ,   DOffice varchar(10),  DPhone int  ,      CONSTRAINT DNameDCode PRIMARY KEY (DName, DCode))"
    # "create table STUDENT    (Sid   varchar(10) ,             DOB varchar(10),       FName varchar(10) ,   MName varchar(10),    LName varchar(10), Addr varchar(20),   Phone varchar(10) ,            Major varchar(10) ,  HAS varchar(10) )"
    # "create table COURSE     (CCode varchar(10) ,             Credits varchar(10),   CoName varchar(10) ,  Level varchar(10) ,   CDesc varchar(10), OFFERS varchar(10) ,constraint CCodeCoName primary key(CCode,CoName) )"
    # "create table SECTION    (DaysTime varchar(10),           Bldg varchar(10) ,     RoomNo varchar(10),   Year int(4),     Sem varchar(10),   SecNo varchar(10) , SecId varchar(10) primary key , SECS varchar(10))"
    # (mix)
    # "create table TAKES        (SId varchar(10),SecID varchar(10), Grade int(3)   )"
    # "create table test (number int primary key, english varchar(2),sentence varchar(10))"
    # 刪掉table  #TRUNCATE  * DELETE FROM  table[name] (where...)刪掉內容
    # "DROP   table COURSE"
    # "DELETE FROM practice  "

    # -------------------------------------------------------------
    # ----name office phone inst..ID
    # """insert into  COLLEGE() value
    # ('文' , '東館1樓', 70000000,'T0001'),
    # ('理' , '東館2樓', 70000001,'T0002'),
    # ('法','東館3樓', 70000002,'T0003'),
    # ('商','西館1樓',   70000003,'T0004'),
    # ('工','西館2樓',   70000004,'T0005'),
    # ('醫','西館3樓',   70000005,'T0006'),
    # ('農','北館2樓',   70000006,'T0007'),
    # ('神學','北館3樓',   70000007,'T0008'),
    # ('教育','南館2樓', 70000008,'T0009'),
    # ('管理','南館3樓', 70000009,'T0010')

    # """  # college
    # -------------------------------------------------------------

    # ----id rand name office phone
    # """ insert into instructor() value
    # ('T0001','銅牌','文中安','東館1樓',900000000,'文系辦'),
    # ('T0002','銀牌','理事長','東館2樓',900000001,'理系辦'),
    # ('T0003','銅牌','法式香草','東館3樓',900000002,'法系辦') ,
    # ('T0004','金牌','商號委','西館1樓',900000003,'商系辦'),
    # ('T0005','鑽石','工商時間','西館2樓',900000004,'工系辦'),
    # ('T0006','大師','醫聊太','西館3樓',900000005,'醫系辦'),
    # ('T0007','銅牌','農莊被','北館2樓',900000006,'農系辦'),
    # ('T0008','金牌','神來也','北館3樓',900000007,'神學系辦'),
    # ('T0009','銀牌','教育較玉','南館2樓',900000008,'教育系辦'),
    # ('T0010','大師','時間管理大師','南館3樓',900000009,'管理系辦')

    # """  # instructor
    # "select * from instructor"
    # "show columns from instructor"
    # -------------------------------------------------------------

    # "DELETE FROM dept  "
    # ---- name code office phone adminBYcollege chair&date
    # "select * from dept"
    # """ insert into dept() value
    # ('文系辦','D000','東館1樓-01',700000000  ),
    # ('理系辦','D111','東館2樓-02',700000101  ),
    # ('法系辦','D222','東館3樓-03',700000202  ),
    # ('商系辦','D333','西館1樓-01',700000303  ),
    # ('工系辦','D444','西館2樓-02',700000404  ),
    # ('醫系辦','D555','西館3樓-03',700000505  ),
    # ('農系辦','D666','北館2樓-02',700000606  ),
    # ('神學系辦','D777','北館3樓-03',700000707),
    # ('教育系辦','D888','南館2樓-02',700000808),
    # ('管理系辦','D999','南館3樓-03',700000909)
    # """  # DEPT : 系辦

    # -------------------------------------------------------------

    # """
    # insert into student() value
    # ('stu01','A','Anna','A.','KNOX','宜蘭縣羅東鎮天津路107號'            ,90108468,'國文'                  ,'文系辦'        ),
    # ('stu02','B','RYAN','B.','AGUILAR','基隆市安樂區樂利二街80號'       ,90204318,'英文'              ,'文系辦'        ),
    # ('stu03','C','BROOKLYN','C.','WEEKS','台北市中正區凱達格蘭大道4巷3號',90301978,'應數'       ,'理系辦'        ),
    # ('stu04','D','JAYSON','D.','GORDON','彰化縣伸港鄉新港路28號'        ,90408719,'物理'               ,'理系辦'        ),
    # ('stu05','E','STEVEN','E.','AGUILAR','高雄市三民區建德路123巷6號'  ,90501113,'法律'           ,'法系辦'       ),
    # ('stu06','F','CONOR','F.','KIRK','高雄市仁武區八德東路124巷6號'    ,90608132,'會計'            ,'法系辦'        ),
    # ('stu07','G','THEA','G.','VANG','高雄市楠梓區惠民路124巷14號'      ,90709695,'財金'              ,'商系辦'        ),
    # ('stu08','H','ERIK','H.','DOYLE','桃園市龍潭區五福街164號'        ,90804666,'金濟'                 ,'商系辦'        ),
    # ('stu09','I','LIONEL','I.','WISE','新北市林口區仁愛路一段146巷14號',90901655,'資工'        ,'工系辦'        ),
    # ('stu10','J','NORAH','J.','CRANE','新北市汐止區福德二路137巷1號'  ,91004168,'電機'           ,'工系辦'        ),
    # ('stu11','K','ANDI','K.','ENGLAND','苗栗縣苗栗市愛國路67號'        ,91101111,'牙醫'               ,'醫系辦'         ),
    # ('stu12','L','ALEX','L.','MAY','嘉義縣民雄鄉大學路一段179巷27號'  ,91206339,'醫學'           ,'醫系辦'        ),
    # ('stu13','M','TYSON','M.','GIBSON','台南市新市區陽光大道38巷21號2樓',91308997,'農科'       ,'農系辦'        ),
    # ('stu14','N','JADA','N.','BELL','高雄市岡山區柳橋西路一段39號'      ,91407615,'農銷'             ,'農系辦'        ),
    # ('stu15','O','ADEN','O.','CANTU','新竹縣湖口鄉達生路54號'        ,91500011,'基督'                 ,'神學系辦'       ),
    # ('stu16','P','DALLAS','P.','WEISS','新北市中和區壽德街53號'      ,91606408,'伊斯蘭'             ,'神學系辦'       ),
    # ('stu17','Q','SANDRA','Q.','REID','新北市三峽區45巷15號'        ,91709880,'幼教'                  ,'教育系辦'      ),
    # ('stu18','R','MARGARET','R.','CRAFT','台南市北區和緯路三段135巷3號',91809603,'特教'       ,'教育系辦'       ),
    # ('stu19','S','CRYSTAL','S.','LINDSEY','台北市中山區建國北路三段282號',91901105,'商管'      ,'管理系辦'      ),
    # ('stu20','T','CURTIS','T.','JACKSON','台中市太平區永平路一段49巷10號',92007789,'原住民管學','管理系辦' )
    # """

    # -------------------------------------------------------------

    # """
    # insert into course() value
    # ('C@文1','3','筍子','L2','半'             ,'文系辦'     ),
    # ('C@文2','1','李白','L3','半'             ,'文系辦'     ),
    # ('C@理1','3','微積分','L1','全'            ,'理系辦'    ),
    # ('C@理2','2','力學','L3','半'             ,'理系辦'     ),
    # ('C@法1','3','法律','L2','全'              ,'法系辦'    ),
    # ('C@法2','2','律師','L3','半'             ,'法系辦'     ),
    # ('C@商1','1','股票','L1','半'             ,'商系辦'     ),
    # ('C@商2','2','經濟學','L1','半'           ,'商系辦'     ),
    # ('C@工1','3','程式','L4','全'             ,'工系辦'     ),
    # ('C@工2','2','電磁學','L4','半'           ,'工系辦'     ),
    # ('C@醫1','3','牙齒','L4','半'            ,'醫系辦'      ),
    # ('C@醫2','2','內科','L5','全'             ,'醫系辦'     ),
    # ('C@農1','1','農與科技','L3','半'         ,'農系辦'     ),
    # ('C@農2','1','農品銷售','L2','半'         ,'農系辦'     ),
    # ('C@神學1','1','聖經','L2','半'          ,'神學系辦'    ),
    # ('C@神學2','2','豬肉','L2','半'          ,'神學系辦'    ),
    # ('C@教育1','3','兒童','L2','半'          ,'教育系辦'    ),
    # ('C@教育2','1','心理學','L2','半'        ,'教育系辦'    ),
    # ('C@管理1','3','管理學','L1','半'         ,'管理系辦'   ),
    # ('C@管理2','1','原住民在地文化','L1','半','管理系辦'     )
    # """
    # "select * from course"

    # --------------------------------------------------

    # """
    # insert into section() value
    # ('上午','東1','001',1999,'1','S001',  '$01','C@文1'),
    # ('下午','東1','002',1999,'1','S002',  '$02','C@文2'),
    # ('上午','東2','001',2000,'1','S003',  '$03','C@理1'),
    # ('下午','東2','002',2000,'1','S004',  '$04','C@理2'),
    # ('上午','東3','001',2000,'2','S005',  '$05','C@法1'),
    # ('下午','東3','002',2000,'1','S006',  '$06','C@法2'),
    # ('上午','西1','001',2011,'1','S007',  '$07','C@商1'),
    # ('下午','西1','002',2011,'2','S008',  '$08','C@商2'),
    # ('上午','西2','001',2012,'1','S009',  '$09','C@工1'),
    # ('上午','西2','002',2012,'2','S010',  '$10','C@工2'),
    # ('下午','西3','001',2012,'2','S011',  '$11','C@醫1'),
    # ('上午','西3','002',2012,'2','S012',  '$12','C@醫2'),
    # ('下午','南1','001',2013,'2','S013',  '$13','C@農1'),
    # ('上午','南1','002',2013,'1','S014',  '$14','C@農2'),
    # ('下午','南2','001',2014,'2','S015',  '$15','C@神學1'),
    # ('上午','南2','002',2014,'1','S016',  '$16','C@神學2'),
    # ('下午','北1','001',2014,'1','S017',  '$17','C@教育1'),
    # ('上午','北1','002',2015,'1','S018',  '$18','C@教育2'),
    # ('下午','北2','001',2015,'2','S019',  '$19','C@管理1'),
    # ('上午','北2','002',2016,'2','S020',  '$20','C@管理2')
    # """

    # --------------------------------------------------


    # mix---

    # ---------------------------------------------------
    # """insert into TAKES() value
    # ('stu01','$01',100 ),
    # ('stu02','$02', 16 ),
    # ('stu03','$03', 28 ),
    # ('stu04','$04', 60 ),
    # ('stu05','$05', 48 ),
    # ('stu06','$06', 91 ),
    # ('stu07','$07', 48 ),
    # ('stu08','$08', 78 ),
    # ('stu09','$09', 61 ),
    # ('stu10','$10', 60 ),
    # ('stu11','$11', 35 ),
    # ('stu12','$12', 29 ),
    # ('stu13','$13', 59 ),
    # ('stu14','$14', 99 ),
    # ('stu15','$15', 86 ),
    # ('stu16','$16', 80 ),
    # ('stu17','$17', 55 ),
    # ('stu18','$18', 67 ),
    # ('stu19','$19', 82 ),
    # ('stu20','$20', 91 )
    # """


    # -------------------------------------------------

    # """insert into test() value
    # (0,'a','hiii'),
    # (1,'b','55sasd'),
    # (2,'c','www'),
    # (3,'d','operator++'),
    # (4,'e','i hate c+')
    # """

    # create table practice(`date` int primary key,`name` varchar(10), computer varchar(10));
    # "insert into practice() values(20200609,'hoho','acer'),(20200610,'jjpjp','hp'),('20210623','asdfhl','rog')"
    # "DELETE FROM practice where date=20200609" #只有VScode才可以做到
    # "delete from practice "
)

students = cursor.fetchall()
for student in students:
    print(student)


account.commit()


# Sel.. from.. where address LIKE "%hohs%"  hohs前有字串 後也有字串 但不知道是甚麼 就用%
# Sel.. from.. where ssn LIKE "___4________"   指定第4位是4 其他位置都不行 如果是用上面的%就是在任何地方的4都可以(前或後有東西之前提下)
# Sel.. from.. where date between 2000 and 2012
# select 1.9 * E.Salary from .....  直接對薪水相乘
# 排順序  select Bdate from employee where sec='M'  order by Bdate,XX,xXX #用年月日來排序  (反敘desc/正ASC)
# ex: ..............................................order by Bdate ASC(正) , year desc(反)

# update 更新   update  empl.... set XXXX='YYY' where ...=..    // XXX全部被改 如果加上(where)縮小範圍
# ex: update test set english='p' where number=0
#            [entity] [attribute]

# delete from XX where AAA='' 只刪掉AAAㄉ內容
# ex: delete from test where number=1

# alter table: ALTER TABLE "table_name"
# 新增欄位 ALTER TABLE Customer ADD    Gender char(1);
# 改欄位名 ALTER TABLE Customer CHANGE Address Addr char(50);
# 改限制   ALTER TABLE Customer MODIFY Addr char(30);  //addr int/char(2)  -> char(5)
# 刪欄位名 ALTER TABLE Customer DROP   Gender;






# 用VScode demo
# select * from practice
# update practice set computer="ideapad" where date=20200609
