create schema SingaporeSchools;
use SingaporeSchools;
#drop table GeneralDetails;
create Table GeneralDetails (
	School_Code int not null,
    School_Name varchar(100) not null,
    School_Region varchar(50) not null,
    School_Address varchar(150) not null,
    School_Postal_Code varchar(50) not null,
    School_Mode varchar(50) not null,
    School_Nature varchar(50) not null,
    School_Type varchar(50) not null,
    School_Number varchar(10) not null,
    School_Email varchar(50) not null,
    School_Website varchar(150) not null,
    School_Image_Source varchar(200) not null,
    Primary Key (School_Code)
    );
#drop table PSLE_Score_Details
create table PSLE_Score_Details (
	School_Code int not null,
    IP_Affiliation varchar(10) not null,
    IP_NonAffiliation varchar(10) not null,
    Express_Affiliation varchar(10) not null,
    Express_NonAffiliation varchar(10) not null,
    NA_Affiliation varchar(10) not null,
    NA_NonAffiliation varchar(10) not null,
    NT_Affiliation varchar(10) not null,
    NT_NonAffiliation varchar(10) not null,
    Primary Key (School_Code),
    Constraint PSLE_Score_Details_fk1 Foreign Key (School_Code) References GeneralDetails(School_Code)
    );

#drop table Subjects_Offered
create table Subjects_Offered (
	School_Code int not null,
    Subject_Offered varchar(50) not null,
    Primary Key (School_Code, Subject_Offered),
    Constraint Subjects_Offered_fk1 Foreign Key (School_Code) References GeneralDetails(School_Code)
    );
    
#drop table dsa_opportunities    
create table dsa_opportunities (
	school_code int not null,
    dsa_cca varchar(100) not null,
    Primary Key (school_code, dsa_cca),
    constraint dsa_opportunities_fk1 foreign key (school_code) references generaldetails(school_code)
    );

#drop table cca_offered
create table cca_offered (
	school_code int not null,
    cca varchar(50),
    Primary Key (school_code, cca),
    constraint cca_offered_fk1 foreign key (school_code) references generaldetails(school_code)
    );

#drop table special_ed_support
create table special_ed_support (
	school_code int not null,
    support_scheme varchar(100) not null,
    Primary Key (school_code, support_scheme),
    constraint special_ed_support_fk1 foreign key (school_code) references generaldetails(school_code)
    );
    
    
#drop table electives;
create table electives (
	school_code int not null,
    elective_name varchar(50) not null,
    elective_sub_header varchar(50),
    elective_sub_sub_header varchar(50),
    primary key (school_code, elective_name, elective_sub_sub_header),
    constraint elective_fk1 foreign key (school_code) references generaldetails(school_code)
    );

#drop table affiliations    
create table affiliations (
	school_code int not null,
    affiliated_school varchar(50) not null,
    primary key (school_code, affiliated_school),
    constraint affiliations_fk1 foreign key (school_code) references generaldetails(school_code)
    );
    

delete from affiliations;
delete from cca_offered;
delete from dsa_opportunities;
delete from electives;
delete from generaldetails;
delete from psle_score_details;
delete from special_ed_support;
delete from subjects_offered;

select * from affiliations;
select * from cca_offered;
select * from dsa_opportunities;
select * from electives;
select * from generaldetails;
select * from psle_score_details;
select * from special_ed_support;
select * from subjects_offered;