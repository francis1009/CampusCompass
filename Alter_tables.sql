use SingaporeSchools;
-- updated region of school
select distinct School_Region from GeneralDetails;
ALTER TABLE GeneralDetails ADD Main_Region varchar(50);
select * from GeneralDetails;

update GeneralDetails set Main_Region = "North" where School_Region in ("Ang Mo Kio", "Woodlands", "Sembawang", "Yishun");
update GeneralDetails set Main_Region = "North-East" where School_Region in ("Hougang", "Punggol", "Seng Kang","Serangoon");
update GeneralDetails set Main_Region = "Central" where School_Region in ("Bukit Timah","Toa Payoh", "Bukit Merah", "Bishan", "Queenstown","Marine Parade","Novena", "Central");
update GeneralDetails set Main_Region = "West" where School_Region in ("Jurong East", "Clementi","Bukit Batok","Bukit Panjang","Choa Chu Kang","Jurong West");
update GeneralDetails set Main_Region = "East" where School_Region in ("Kallang", "Bedok", "Geylang", "Tampines", "Pasir Ris");

select count(*) from GeneralDetails where Main_Region is NULL;
select * from GeneralDetails;

-- update subjects
select * from subjects_offered;
ALTER TABLE subjects_offered ADD subject_category varchar(50);
select * from subjects_offered;
select distinct subject_offered from subjects_offered;

update subjects_offered set subject_category = "Language" where Subject_Offered in ("English Language", "Higher Chinese Language", "Malay Language (Special Program)", "Basic Chinese Language", "Basic Malay Language","Basic Tamil Language", "Chinese Language", "Higher Malay Language","Higher Tamil Language","Malay Language","Tamil Language","Chinese Language Syllabus B","Malay Language Syllabus B","Tamil Language Syllabus B","Chinese Language (Special Programme)","Conversational Malay Programme","Advanced Language Arts","Language Arts","Malay Language (Special Programme)","Bahasa Indonesia","Conversational Malay","Malay Special Programme");

update subjects_offered set subject_category = "Math" where Subject_Offered in ("Additional Mathematics", "Mathematics","Principles of Accounts","D1 Mathematics 2","D2 Mathematics 2","Mathematics 1","Mathematics B","Mathematics C","Advanced Inquiry in Mathematics","Advanced Mathematics","Fundamental Mathematics","Intermediate Mathematics","Integrated Mathematics 2");

update subjects_offered set subject_category = "Science" where Subject_Offered in ("Biology", "Chemistry", "Physics", "Computer Applications", "Design & Technology", "Mobile Robotics", "Science", "Science (Phy, Chem)","Nutrition and Food Science","Science (Chem, Bio)","Smart Electrical Technology","Lower Secondary Computer Education Programme","Computing","Stem Elective","Electronics","Science (Phy, Bio)","D2 Biology","D2 Chemistry","D2 Physics","S1 Stemviadt","Infocom Technology","Internet of Things Applications","Mechanical Design & Automation","Mobile Web Applications","Advanced Science","Integrated Sciences","Green Science","Innovation and Research Project","Information and Communications Technology","Biotechnology");

update subjects_offered set subject_category = "Humanities" where Subject_Offered in ("Appreciation of Chinese Culture", "Geography","Humanities (Ss, History)", "Literature in English", "Humanities (Ss, Geography)","Humanities (Ss, Literature in English)","Humanities (Ss, Literature in English)", "Social Studies","History","Regional Studies Programme","Humanities (Ss, Literature in Tamil)","Literature in Tamil","D1 Geography","D1 History","D1 Literature in Chinese","D1 Literature in English","D2 Geography","D2 History","D2 Literature in Chinese","D2 Literature in English","Humanities (Ss, Literature in Chinese)","Literature in Chinese","Advanced Humanities","Governance & Society","Chinese Literature","English Literature","Fundamental Humanities","Singapore Studies and Chinese Literature","Singapore Studies and English Literature","Singapore Studies and Geography","Singapore Studies and History","Humanities (Ss, Literature in Malay)","Economics","Bicultural Studies","Singapore Studies","Business Studies","Literature in Malay","Literature");

update subjects_offered set subject_category = "Art" where Subject_Offered in ("Art","Music","Higher Music","Art (Special Programme)","Music Preparatory Course","Higher Art","Drama","Drama in Curriculum","Art (Ip)","Aesthetics(Art)","Aesthetics(Design & Technology)","Aesthetics(Food & Consumer Education)","Aesthetics(Music)","Performing Arts","Visual Arts","Art Elective Programme","Drama-In-Production","General Arts Programme (Art)","General Arts Programme (Music)","Music Programme","Aesthetics","Music Elective Programme","Art & Design","Music & Design","Puppetry","Advanced Music","Dance");


update subjects_offered set subject_category = "Others" where Subject_Offered in ("Food & Consumer Education","Physical Education", "Applied Learning Programme", "Elements of Business Skills","Design Elective","Cce","Via","Character and Citizenship Education","Retail Operations","Exercise & Sports Science","Active Citizenry Education","Life Skills Programme","Project Work","Character & Citizenship Education","Montfort Development Program","Sip: Basic Baking Skills","Culinary & Restaurant Operations","Every Crestan Can Code","Fabulous Merchandise Display","Input To Output","Let's Get Connected","Link Up the World","Passion To Serve","Retail & E-Commerce","Wheels of Wonder","Man and Ideas","Spire","Thinking","Inquiry & Advocacy","Alp","Values in Action","Student Initiated Learning","Cid 1","Cid 2","Cid3","Cid4","Portfolio Preparation Programme","Food & Nutrition","Ft","Food Studies","Changemakers","Design Studies","Sports and Wellness");

select count(*) from subjects_offered where subject_category is null;

select distinct(subject_offered) from subjects_offered where subject_category is null;

-- update cca
select * from cca_offered;
ALTER TABLE cca_offered ADD cca_category varchar(50);
select distinct cca from cca_offered;

update cca_offered set cca_category = "Sports" where cca like "%takraw%";
update cca_offered set cca_category = "Sports" where cca like "%climb%";
update cca_offered set cca_category = "Sports" where cca like "%frisbee%";
update cca_offered set cca_category = "Sports" where cca like "%country%";
update cca_offered set cca_category = "Sports" where cca like "%boat%";
update cca_offered set cca_category = "Sports" where cca like "%outdoor%";
update cca_offered set cca_category = "Sports" where cca like "%judo%";
update cca_offered set cca_category = "Sports" where cca like "%fencing%";
update cca_offered set cca_category = "Sports" where cca like "%rugby%";
update cca_offered set cca_category = "Sports" where cca like "%sailing%";
update cca_offered set cca_category = "Sports" where cca like "%cricket%";
update cca_offered set cca_category = "Sports" where cca like "%gym%";
update cca_offered set cca_category = "Sports" where cca like "%swimming%";
update cca_offered set cca_category = "Sports" where cca like "%ball%";
update cca_offered set cca_category = "Sports" where cca like "%golf%";
update cca_offered set cca_category = "Sports" where cca like "%taekwondo%";
update cca_offered set cca_category = "Sports" where cca like "%karate%";
update cca_offered set cca_category = "Sports" where cca like "%hockey%";
update cca_offered set cca_category = "Sports" where cca like "%wushu%";
update cca_offered set cca_category = "Sports" where cca like "%water%";
update cca_offered set cca_category = "Sports" where cca like "%shooting%";
update cca_offered set cca_category = "Sports" where cca like "%squash%";
update cca_offered set cca_category = "Sports" where cca like "%bowling%";
update cca_offered set cca_category = "Sports" where cca like "%tennis%";
update cca_offered set cca_category = "Sports" where cca like "%canoeing%";
update cca_offered set cca_category = "Sports" where cca like "%badminton%";
update cca_offered set cca_category = "Sports" where cca like "%field%";
update cca_offered set cca_category = "Sports" where cca like "%sports%";
update cca_offered set cca_category = "Sports" where cca like "%archery%";
update cca_offered set cca_category = "Sports" where cca like "%trampoline%";
update cca_offered set cca_category = "Arts" where cca like "%dance%";
update cca_offered set cca_category = "Arts" where cca like "%ensemble%";
update cca_offered set cca_category = "Arts" where cca like "%band%";
update cca_offered set cca_category = "Arts" where cca like "%orchestra%";
update cca_offered set cca_category = "Arts" where cca like "%choir%";
update cca_offered set cca_category = "Arts" where cca like "%drama%";
update cca_offered set cca_category = "Arts" where cca like "%art%";
update cca_offered set cca_category = "Arts" where cca like "%culture%";
update cca_offered set cca_category = "Arts" where cca like "%film%";
update cca_offered set cca_category = "Arts" where cca like "%opera%";
update cca_offered set cca_category = "Arts" where cca like "%jazz%";
update cca_offered set cca_category = "Arts" where cca like "%drums%";
update cca_offered set cca_category = "Arts" where cca like "%audio%";
update cca_offered set cca_category = "Uniform Group" where cca like "%NCC%";
update cca_offered set cca_category = "Uniform Group" where cca like "%Brigade%";
update cca_offered set cca_category = "Uniform Group" where cca like "%Guides%";
update cca_offered set cca_category = "Uniform Group" where cca like "%NPCC%";
update cca_offered set cca_category = "Uniform Group" where cca like "%NCDCC%";
update cca_offered set cca_category = "Uniform Group" where cca like "%scouts%";
update cca_offered set cca_category = "Uniform Group" where cca like "%Red Cross%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%Chess%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%Media%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%Weiqi%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%science%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%mathematics%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%education%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%home%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%robotics%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%photography%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%service%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%club%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%student%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%leadership%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%strat%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%chinese%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%CCA%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%stud%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%design%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%tech%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%library%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%jouralism%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%heritage%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%read%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%public%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%photo%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%project%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%entrepreneurship%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%journal%";
update cca_offered set cca_category = "Clubs and Societies" where cca like "%aero%";

select count(*) from cca_offered where cca_category is null;
select distinct(cca) from cca_offered where cca_category is null;
select distinct(count(cca)) from cca_offered where cca_category is null;
select distinct(cca) from cca_offered where cca_category is null;

select * from dsa_opportunities;


-- update dsa_opportunities
ALTER TABLE dsa_opportunities ADD dsa_category varchar(50);
select distinct dsa_cca from dsa_opportunities;
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%takraw%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%climb%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%frisbee%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%country%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%boat%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%outdoor%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%judo%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%fencing%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%rugby%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%sailing%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%cricket%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%gym%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%swimming%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%ball%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%golf%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%taekwondo%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%karate%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%hockey%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%wushu%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%water%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%shooting%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%squash%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%bowling%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%tennis%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%canoeing%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%badminton%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%field%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%sports%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%archery%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%trampoline%";
update dsa_opportunities set dsa_category = "Sports" where dsa_cca like "%track%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%dance%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%ensemble%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%band%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%orchestra%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%choir%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%drama%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%art%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%culture%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%film%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%opera%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%jazz%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%drums%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%audio%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%music%";
update dsa_opportunities set dsa_category = "Arts" where dsa_cca like "%theatre%";
update dsa_opportunities set dsa_category = "Uniform Group" where dsa_cca like "%NCC%";
update dsa_opportunities set dsa_category = "Uniform Group" where dsa_cca like "%Brigade%";
update dsa_opportunities set dsa_category = "Uniform Group" where dsa_cca like "%Guides%";
update dsa_opportunities set dsa_category = "Uniform Group" where dsa_cca like "%NPCC%";
update dsa_opportunities set dsa_category = "Uniform Group" where dsa_cca like "%NCDCC%";
update dsa_opportunities set dsa_category = "Uniform Group" where dsa_cca like "%scouts%";
update dsa_opportunities set dsa_category = "Uniform Group" where dsa_cca like "%Red Cross%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%Chess%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%Media%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%Weiqi%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%scien%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%mathematics%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%education%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%home%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%robotics%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%photography%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%service%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%club%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%student%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%leadership%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%strat%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%chinese%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%dsa_cca%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%stud%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%design%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%tech%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%library%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%jouralism%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%heritage%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%read%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%public%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%photo%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%project%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%entrepreneurship%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%journal%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%aero%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%bilingualism%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%stem%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%innovation%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%language%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%debat%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%bilingualism%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%Research%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%Research%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%com%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%human%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%electr%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%coding%";
update dsa_opportunities set dsa_category = "Clubs and Societies" where dsa_cca like "%prog%";

select count(*) from dsa_opportunities where dsa_category is null;
select distinct(dsa_cca) from dsa_opportunities where dsa_category is null;
select distinct(count(dsa_cca)) from dsa_opportunities where dsa_category is null;
select distinct(dsa_cca) from dsa_opportunities where dsa_category is null;

select * from dsa_opportunities;

select count(*) from cca_offered;
select count(distinct school_code) from cca_offered;

select count(distinct school_code) from generaldetails;

select * from cca_offered;

